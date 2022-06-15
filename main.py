import os

import pymongo
from flask import Flask, Response, jsonify
import json

app = Flask(__name__)

try:
    MONGO_DB_USER = os.environ.get('MONGO_DB_USER')
    MONGO_DB_PASSWORD = os.environ.get('MONGO_DB_PASSWORD')
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
    uri = f'mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@db_mongo:27017/?authMechanism=DEFAULT&authSource={MONGO_DB_NAME}'
    mongo_client = pymongo.MongoClient(uri)
    mongo_client.admin.command('ismaster')  # to check if the connection has been established - show errors in terminal
    info = mongo_client.server_info()
    db = mongo_client.get_database('flask_api_db')
    print('DB: ', db, flush=True)
    print('OK', flush=True)
    print('SERVER INFO', info, flush=True)
except:
    print('Error', flush=True)


@app.route('/')
def index():
    return 'Test2'


@app.route('/users/', methods=['POST'])
def create_user():
    try:
        user = {'name': 'A', 'lastName': 'AA'}
        db_response = db.users.insert_one(user)
        return Response(
            response=json.dumps({'message': 'user created', 'id': f'{db_response.inserted_id}'}),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print('*' * 30, flush=True)
        print(ex, flush=True)
        print('*' * 30, flush=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
