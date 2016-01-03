

from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        cur = conn.cursor()

        tableName = 'tweetwordcount'
        cur.execute("select * from information_schema.tables where table_name=%s", (tableName,))

        if not cur.rowcount:
            cur.execute('''CREATE TABLE tweetwordcount
                (word TEXT PRIMARY KEY     NOT NULL,
                count INT     NOT NULL);''')

        conn.commit()
        conn.close()

    def process(self, tup):

        word = tup.values[0]
        lowerWord = word.lower()

        # Increment the local count

        self.counts[lowerWord] += 1

        isExists = self.checkRowPostGres(lowerWord)

        if not isExists:
            self.insertPostGres(lowerWord)
        else:
            self.updatePostGres(lowerWord)

        self.emit([lowerWord, self.counts[lowerWord]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (lowerWord, self.counts[lowerWord]))



    def insertPostGres(self, word):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        cur = conn.cursor()

        initCount = 1

        #Insert
        cur.execute("INSERT INTO tweetwordcount (word,count) \
            VALUES (%s, %s)", (word, initCount));
        conn.commit()
        conn.close()


    def updatePostGres(self, word):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        cur = conn.cursor()

        #Update

        cur.execute("UPDATE tweetwordcount SET count = count + 1 WHERE word=%s", (word,))
        conn.commit()
        conn.close()

    def checkRowPostGres(self, word):

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        cur = conn.cursor()
        cur.execute("SELECT * FROM tweetwordcount WHERE word=%s", (word,))
        check = cur.fetchall()

        isExists = False
        if check:
            isExists = True
            
        conn.commit()
        conn.close()

        return isExists









                                                               

