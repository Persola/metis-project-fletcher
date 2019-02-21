import json
from pymongo import MongoClient

with open('data/amazon_book_reviews.json', 'r') as reviews_file:
    reviews = (json.loads(line) for line in reviews_file)
    mongo = MongoClient()
    for review in reviews:
        mongo.reviews.books.insert(review)
