from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


MONGO = os.getenv("MONGO")


def push_to_mongodb(
    df, collection_name="your_collection", database_name="your_database"
):
    """
    Pushes the DataFrame records to MongoDB.

    Parameters:
    - df: pandas DataFrame
    - collection_name: str, the name of the MongoDB collection to use
    - database_name: str, the name of the MongoDB database to use
    """
    # Establish a connection to MongoDB
    client = MongoClient(MONGO)

    # Select the database
    db = client[database_name]

    # Select the collection
    collection = db[collection_name]

    # Convert the DataFrame to a list of dictionaries (records)
    records = df.to_dict(orient="records")

    # Insert records into the MongoDB collection
    collection.insert_many(records)

    # Close the MongoDB connection
    client.close()
