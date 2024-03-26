#!/usr/bin/python3
'''mysqldb 5'''


import sys
from MySQLdb import connect

if __name__ == "__main__":
    mydb = connect(host="localhost", port=3306, user=sys.argv[1],
                   passwd=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    query1 = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities WHERE state"
    query2 = "_id = (SELECT id FROM states WHERE name = %s LIMIT 1) "
    query3 = "ORDER BY id ASC"
    mycursor.execute(query1 + query2 + query3, (sys.argv[4],))
    result = mycursor.fetchone()[0]
    if result:
        print(result)
    else:
        print()
    mycursor.close()
    mydb.close()
