import pymongo

try:
    # client = pymongo.MongoClient('mongodb://localhost:27017/flask_api_db')
    client = pymongo.MongoClient(
        host='db_mongo',
        port=27018,
        serverSelectionTimeoutMS=1000
    )
    # personsDB = client['Persons']
    # tblTest = personsDB['tblTest']
    db = client.get_database('flask_api_db')
    print('DB: ', db, flush=True)
    db.create_collection('myCollection')
    print('TUTAJ', flush=True)

    testData = [
        {'id': 1, 'Name': 'A', 'LastName': 'AA', 'Age': 20},
        {'id': 2, 'Name': 'B', 'LastName': 'BB', 'Age': 50},
    ]

    # tbl = tblTest.insert_many(testData)


    # print('DANE: ', tbl.inserted_ids, flush=True)
except:
    print('Połączenie nie działa')
