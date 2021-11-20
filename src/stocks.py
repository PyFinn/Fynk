import datetime
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from pymongo import *
from datetime import datetime as dt
from pymongo.errors import DuplicateKeyError

# This is where Stock data can be retrieved
# ----------
# Used to provide several functions for making simple Data API calls


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


class ProcessQueries(MongoDB):

    def __init__(self, c):
        super().__init__(c)

    def fetch_and_process_most_recent_query(self):
        queries = self.get_collection("Queries")
        stack = self.get_collection("Workstack")

        for entry in queries.find():
            try:
                entry["processingTimestamp"] = dt.now().strftime('%Y-%m-%d--%H:%M:%S.%f')[:-3]
                stack.insert_one(entry)
            except DuplicateKeyError:
                continue

            queries.delete_one({"_id": entry["_id"]})
            return entry

        return 0


def open_ticker_from_short(short):
    ticker = yf.Ticker(short)
    return ticker


def __main__():
    processor = ProcessQueries(c="mongodb+srv://finn:sauber@cluster0.4gtm6.mongodb.net/test")
    processor.set_database("Algo")

    current_entry = {}
    while current_entry != 0:
        current_entry = processor.fetch_and_process_most_recent_query()
        if type(current_entry) != int:
            short = current_entry["tickerSymbol"]
            time_frame = current_entry["timeFrame"]


__main__()
