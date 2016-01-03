

from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def createDatabse():

    con = psycopg2.connect(database='postgres', user='postgres', host='localhost', password='pass')
    dbname = "tcount"

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = con.cursor()
    curr.execute("SELECT * FROM pg_database WHERE datname=%s", (dbname,))
    check = curr.fetchall()
        
    if not check:
        curr.execute('CREATE DATABASE ' + dbname)
        print ("Database created")
    else:
        print ("Database already exists")

    con.commit()
    curr.close()
    con.close()



if __name__ == '__main__':

    createDatabse()