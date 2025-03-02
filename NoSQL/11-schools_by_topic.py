#!/usr/bin/env python3
"""
 Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Prototype: def schools_by_topic(mongo_collection, topic):
    Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})