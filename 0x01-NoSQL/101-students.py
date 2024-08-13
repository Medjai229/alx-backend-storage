#!/usr/bin/env python3
""" 101-main """


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    avg_score = mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])

    return avg_score
