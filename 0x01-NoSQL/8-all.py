#!/usr/bin/env python3
""" list_all """

import pymongo


def list_all(mongo_collection):
    """ This function returns a list of all docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    doc_list = []
    for doc in docs:
        doc_list.append(doc)

    return doc_list
