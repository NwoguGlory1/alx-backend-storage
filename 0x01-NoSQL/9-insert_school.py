#!/usr/bin/env python3
""" script that inserts a new document in a collection based on kwargs"""

from pymongo import MongoClient
""" import needed to establish a connection to the MongoDB server. """

def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection, mongo_collection
    based on kwargs
    """
    result_of_insertion = mongo_collection.insertOne(kwargs)
    """
    inserted_id is an attribute of insertOne, contains the _id
    of the newly inserted document."""
    return result_of_insertion.inserted_id
