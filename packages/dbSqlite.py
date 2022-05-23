# -*- coding: utf-8 -*-
import sqlite3
import time


class dbSqlite:
    def __init__(self):
        self.sqliteConnection=sqlite3.connect('database/db.sql')

    def insertDB(self, query):
        print(query)
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return 'Insert success'
        except:
            return 'query not found'

    def selectDB(self, query):
        print(query)
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(query)
            return cur.fetchall()
        except:
            return 'error: query not found'

    def updateDB(self, query):
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return 'out: Update success'
        except:
            return 'error: query not found'

    def deleteDB(self, query):
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return 'out: Delete success'
        except:
            return 'error: query not found'

    def checkUsername(self, username):
        findUser="select * from Users"
        outcome=[]
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(findUser)
            for row in cur.fetchall():
                if username == row[2]:
                    outcome=list(row)
            return outcome
        except:
            return 'error: query not found'

    def checkPublicId(self, publicId):
        findUser="select * from Users"
        outcome=[]
        try:
            cur=self.sqliteConnection.cursor()
            cur.execute(findUser)
            for row in cur.fetchall():
                if publicId == row[1]:
                    outcome=list(row)
            return outcome
        except:
            return 'error: query not found'
