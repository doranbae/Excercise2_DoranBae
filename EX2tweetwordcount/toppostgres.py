from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def selectTopPostGres(topK):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()

        cur.execute("SELECT word, count from tweetwordcount ORDER BY count DESC LIMIT %s",(topK,))
        records = cur.fetchall()

        if not records:
        	print ("Empty Data")

        for rec in records:
            print ("(word = %s , count = %s)" % (rec[0], rec[1]))

        print("Row Count : %s" % cur.rowcount)

        conn.commit()
        conn.close()


if __name__ == '__main__':

    arg = 20

    if len(sys.argv) > 1:
        arg = sys.argv[1]


    selectTopPostGres(arg)
    
