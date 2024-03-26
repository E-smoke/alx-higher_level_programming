#!/usr/bin/python3
'''mysqldb 3'''


import sys
from MySQLdb import connect

if __name__ == '__main__':
    mydb = connect(host="localhost", port=3306, user=sys.argv[1],
                   passwd=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    mycursor.execute(query, ('{}%'.format(sys.argv[4]),))
    li = mycursor.fetchall()
    for i in li:
        print(i)
    mycursor.close()
    mydb.close()
