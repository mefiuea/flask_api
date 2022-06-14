import os

import pymongo
from flask import Flask, Response
import json

app = Flask(__name__)

# try:
#     # mongo = MongoClient(
#     #     host='db_mongo',
#     #     port=27017,
#     #     serverSelectionTimeoutMS=1000
#     # )
#     # db = mongo.flask_api_db
#     # db = mongo.get_database('flask_api_db')
#     # print('DATABASE NAME:', db, flush=True)
#
#     # mongo = PyMongo(app)
#     # mongo.server_info()
# except:
#     print('PROBLEM')


@app.route('/')
def index():
    return 'Hello'


@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = {'name': 'Maciej', 'lastName': 'Test'}
        print('tutaj', flush=True)
        # db_response = db.insert_one(user)
        # persons.insert_one(user)
        print('tutaj2', flush=True)

        # for element in db_response:
        #     print('INFO:')
        #     print(element)

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
    app.run(debug=True, host='0.0.0.0', port=8100)
