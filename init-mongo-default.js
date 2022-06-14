db.log.insertOne({"message": "Database created."});

db = db.getSiblingDB('admin');

db.auth('AdminName', 'AdminPassword')

db = db.getSiblingDB('user_db');

db.createUser(
    {
        user: 'some_user',
        pwd: 'user_password',
        roles: [
            {
                role: 'dbOwner',
                db: 'user_db'
            }
        ]
    }
)

db.createCollection('collection_test');
