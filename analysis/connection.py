from pymongo import MongoClient
import ssl

# Set the connection parameters
mongo_host = "localhost"  # localhost because the tunnel is created locally
mongo_port = 27017
mongo_user = "admin"
mongo_password = "admin_password"
mongo_db = "mydatabase"

# Create an SSL context
ssl_context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='connection.key')

# Create a connection to the MongoDB instance using the SSL tunnel
with MongoClient(host=mongo_host, port=mongo_port, ssl_context=ssl_context, username=mongo_user, password=mongo_password, authSource=mongo_db) as client:
    database = client[mongo_db]

    # Example: Insert a document into a collection
    collection = database["mycollection"]
    document = {"key": "value"}
    result = collection.insert_one(document)

    print(f"Inserted document with ID: {result.inserted_id}")