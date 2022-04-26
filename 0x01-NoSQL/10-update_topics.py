#!/usr/bin/env/python3
''' task 10 module
'''

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """function to update topics
    """

    mongo_collection.update_many({'name': name}, {$set: {'topics': topics}})
    
