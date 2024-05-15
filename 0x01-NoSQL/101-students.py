#!/usr/bin/env python3
"""script that returns all students sorted by average score """


def top_students(mongo_collection):
    """ function that returns all students sorted by average score """
     # top_st = mongo_collection.aggregate([
    #     {"$unwind": "$topics"},
    #     {"$group":
    #         {
    #             "_id": "$_id",
    #             "name": {"$first": '$name'},
    #             "averageScore": {"$avg": "$topics.score"}
    #         }
    #      },
    #     {"$sort": {"averageScore": -1}}
    # ])

    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
