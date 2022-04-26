#!/usr/bin/env python3
'''python function to list all documents in a collection
'''


def list_all(mongo_collection):
    '''List all documents in a collection
    '''
    return [item for item in mongo_collection.find()]
