import sqlite3

class StockManager:
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()
