#!/usr/bin/python3
'''sqldb 2'''


import sys
from MySQLdb import connect

if __name__ == '__main__':
    mydb = connect(host="localhost", port=3306, user=sys.argv[1],
                   passwd=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    mycursor.execute(query)
    li = mycursor.fetchall()
    for i in li:
        print(i)
    mycursor.close()
    mydb.close()
