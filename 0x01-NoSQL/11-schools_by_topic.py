#!/usr/bin/env python3
""" script that returns the list of school having a specific topic """

from pymongo import MongoClient
""" import needed to establish a connection to the MongoDB server. """


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    """
    document_topic = mongo_collection.find({topics: "topic"})
    """
    find() method is used to query on mongo_collection for where
    topics field contains specified topic
    """
    returned_list = [document for document in document_topic]
    """ Extract documents that match the specified topic """
    return returned_list
