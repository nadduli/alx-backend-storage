#!/usr/bin/env python3
'''python function to insert documents in a collection
'''


def insert_school(mongo_collection, **kwargs):
    ''' insert document in a collection
    '''
    items = mongo_collection.insert_one(**kwargs)
    return items.inserted_id
