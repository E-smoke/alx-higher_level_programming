#!/usr/bin/python3
'''mysql 4'''

import sys
from MySQLdb import connect
if __name__ == '__main__':
    db = connect(host="localhost", port=3306, user=sys.argv[1],
                 passwd=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    query1 = "SELECT cities.id, cities.name, states.name FROM cities JOIN"
    query2 = " states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query1 + query2)
    li = cursor.fetchall()
    for i in li:
        print(i)
    cursor.close()
    db.close()
