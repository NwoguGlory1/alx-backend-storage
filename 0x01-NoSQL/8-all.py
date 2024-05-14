#!/usr/bin/env python3
""" script that lists all documents in a collection"""

from pymongo import MongoClient
""" import needed to establish a connection to the MongoDB server. """

def list_all(mongo_collection):
    """ List all documents in Python """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
