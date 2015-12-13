from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def selectHistogramPostGres(k1, k2):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()

        cur.execute("SELECT word, count from tweetwordcount WHERE count >= %s AND count <= %s", (k1,k2))
        records = cur.fetchall()

        if not records:
        	print ("Empty Data")

        for rec in records:
            print ("(word = %s , count = %s)" % (rec[0], rec[1]))

        print("Row Count : %s" % cur.rowcount)

        conn.commit()
        conn.close()


if __name__ == '__main__':

    if len(sys.argv) > 1:
        arg = sys.argv[1].split(',')

        k1 = 0
        k2 = 0

        if len(arg) > 0 :
            k1 = arg[0]
        if len(arg) > 1:
            k2 = arg[1]

        selectHistogramPostGres(k1, k2)
    
