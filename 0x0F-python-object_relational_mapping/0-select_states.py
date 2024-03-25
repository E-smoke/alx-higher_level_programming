#!/usr/bin/python3
import sys
import mysql.connector as connector

mydb = connector.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM states ORDER BY id")
states = mycursor.fetchall()
for i in states:
    print(i)
