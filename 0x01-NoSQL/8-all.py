#!/usr/bin/env python3
""" script that lists all documents in a collection"""

from pymongo import MongoClient
""" import needed to establish a connection to the MongoDB server. """

def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    documents = mongo_collection.find()
    """
    calls the find() method on the mongo_collection object
    find() method retrieves all documents in a collection,
    it returns a cursor which is stored in documents.
    """

    if documents.count() == 0:
        """
        calls the count() method on document,
        it counts  all documents in a collection.
        """
        return []

    return documents
