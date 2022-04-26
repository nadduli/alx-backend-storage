#!/usr/bin/env python3
'''python function to insert documents in a collection
'''


def insert_school(mongo_collection, **kwargs):
    ''' insert document in a collection
    '''
    result = mongo_collection.insert_one(**kwargs)
    return result.inserted_id
