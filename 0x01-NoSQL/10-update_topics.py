#!/usr/bin/env python3
""" script that changes all topics of a school document based on the name"""

from pymongo import MongoClient
""" import needed to establish a connection to the MongoDB server. """


def update_topics(mongo_collection, name, topics):
    """
    function that updates the topics field of a school document
    identified by its name in mongo_collection
    """
    mongo_collection.update_one({"name": name}, {$set: {"topics": topics}})
