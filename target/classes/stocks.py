import datetime
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from yfinance import *
from pymongo import *

# This is where Stock data can be retrieved
# ----------
# Used to provide several functions for making simple Data API calls


class Data:
    __gui = None

    def __init__(self, gui):
        self.__gui = gui

    def run(self):
        print('Hello world!')


class MongoDB:

    def __init__(self, c):
        self.client = MongoClient(c)
        self.database = 0

    def list_database_names(self):
        self.client.list_database_names()

    def set_database(self, db):
        self.database = db

    def get_collection(self, col):
        return self.client[self.database][col]


def __main__():
    mongo_toolbase = MongoDB(c="mongodb+srv://finn:sauber@cluster0.4gtm6.mongodb.net/test")
    mongo_toolbase.set_database("Algo")

    col = mongo_toolbase.get_collection("Waitlist")

    for entry in col.find():
        print(entry)


__main__()
