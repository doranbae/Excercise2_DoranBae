from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import sys



def selectAllPostGres():

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    cur = conn.cursor()

         #Select
    cur.execute("SELECT word, count from tweetwordcount")
    records = cur.fetchall()

    for rec in records:
        print ("word = %s , count = %s" % (rec[0], rec[1])

    conn.commit()
    conn.close()


if __name__ == '__main__':
	selectAllPostGres()