#!/usr/bin/env python3
"""
12-log_stats

This script connects to a MongoDB database
and retrieves statistics about the logs.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats = client.logs.nginx

    number_of_logs = log_stats.count_documents({})
    number_of_gets = log_stats.count_documents({"method": "GET"})
    number_of_posts = log_stats.count_documents({"method": "POST"})
    number_of_puts = log_stats.count_documents({"method": "PUT"})
    number_of_patchs = log_stats.count_documents({"method": "PATCH"})
    number_of_deletes = log_stats.count_documents({"method": "DELETE"})
    number_of_status_gets = log_stats.count_documents({"method": "GET",
                                                       "path": "/status"})

    print(f'{number_of_logs} logs')
    print(f'\tmethod GET: {number_of_gets}')
    print(f'\tmethod PUT: {number_of_puts}')
    print(f'\tmethod PATCH: {number_of_patchs}')
    print(f'\tmethod DELETE: {number_of_deletes}')
    print(f'{number_of_status_gets} status check')
    print(f'\tmethod POST: {number_of_posts}')
