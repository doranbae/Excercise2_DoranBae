from __future__ import absolute_import, print_function, unicode_literals
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def selectAllPostGres():

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()

        cur.execute("SELECT word, count from tweetwordcount ORDER BY word ASC")
        records = cur.fetchall()

        if not records:
        	print ("Empty Data")

        for rec in records:
            print ("(word = %s , count = %s)" % (rec[0], rec[1]))

        print("Row Count : %s" % cur.rowcount)

        conn.commit()
        conn.close()


def selectArgPostGres(word):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        cur = conn.cursor()

        #Update

        cur.execute("SELECT word, count from tweetwordcount WHERE word=%s", (word,))
        records = cur.fetchall()

		if not records:
			print ("Empty Data")

        for rec in records:
            print ("Total number of occurences of \"%s\" : %s" % (rec[0], rec[1]))

        print("Row Count : %s" % cur.rowcount)

        conn.commit()
        conn.close()


if __name__ == '__main__':

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        lowerArg = arg.lower()
        selectArgPostGres(lowerArg)
    else:
        selectAllPostGres()

