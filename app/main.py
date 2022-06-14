import os

from flask import Flask, Response
import json
from pymongo import MongoClient, errors

app = Flask(__name__)

try:
    mongo = MongoClient(
        host='db_mongo',
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.flask_api_db
    mongo.server_info()
except errors.ServerSelectionTimeoutError as err:
    print('PROBLEM')
    print(err)


@app.route('/')
def index():
    return 'Hello'


@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = {'name': 'Maciej', 'lastName': 'Test'}
        db_response = db.users.insert_one(user)
        print('tutaj', flush=True)

        for element in db_response:
            print('INFO:')
            print(element)

        return Response(
            response=json.dumps(
                {'message': 'user created', 'id': f'test'}
            ),
            status=200,
            mimetype='application/json'
        )

    except Exception as ex:
        print('INFO:')
        print(ex)
        return 'Error'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
