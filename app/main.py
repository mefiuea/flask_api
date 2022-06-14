from flask import Flask
import pymongo
from pymongo import errors

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host='db_mongo',
        port=27018,
        serverSelectionTimeoutMS=1000
    )
    mongo.server_info()
except errors.ServerSelectionTimeoutError as err:
    print(err)
    print('PROBLEM')


@app.route('/')
def index():
    return 'Hello'


@app.route('/users', methods=['POST'])
def create_user():
    return 'X'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
