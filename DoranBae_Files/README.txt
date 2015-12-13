This is step by step instruction to replicate my exercise 2 submission.

****** WARNING regarding finalresults.py ******
Even though I made sure all the codes work properly, when copying the finalresults.py file, the indentation may change, resulting in an error message. It can be easily fixed. It is the IF & PRINT clause on line 37, 38. 

 I strongly encourage you to just use the final AMI fully loaded with all the scripts. The info on pre-loaded AMI is at the bottom of this document. If you decide to start from a new one, be aware of this issue. If an error occurs when running finalresults.py, open the python script, and please make sure indentations are correct. It may not occur for you. I cannot figure out why it is altering its indentation by itself. 


##########################################################
STEP 1 SET UP A NEW INSTANCE
##########################################################
1. 	From AWS's AMI, search for AMI with ID : ami-596f1733 (Lab9_Final_AMI)
	This is AMI I created for Lab 9. I will re-use it for Exercise 2. 

2. Configure instance and launch it. In the security setting, make sure port 5432 is open. 

3. Connect to the instance and do the neccessary settings including mounting volume, and starting hadoop and postgres.
- I ran every command under root to avoid any permission issues. So please be sure to do everything under root user.

	# fdisk -l
	# mount -t ext4 /dev/xvdf /data
	# sh start-hadoop.sh
	# cd .. 
	# cd data/
	# sh start_postgres.sh
	# cd .. 

4. Clone github repository
- I cloned my github repository at /

	# mkdir ex2
	# cd ex2/
	# git clone https://github.com/doranbae/Excercise2_DoranBae

- cd to DoranBae_Files. This is where you will find all the codes I have worked on.

5. Install psycopg

	# pip install psycopg2

6. Install tweepy
	
	# pip install tweepy

7. Make sure python version is 2.7.3

	# python --version

##########################################################
STEP 2 CREATE EX2Tweetwordcount project
##########################################################

1. At / create a project called EX2Tweetwordcount in Streamparse

	# sparse quickstart EX2Tweetwordcount

2. Copy the files from DoranBae_Files in your cloned repository and copy them in the corresponding folders in the new EX2Tweetwordcount project. 

	* You need below files to run streamparse.
	
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/topology/EX2Tweetwordcount.clj --> topology
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/src/tweets.py --> spouts folder
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/src/parse.py --> bolts folder
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/src/wordcount.py --> bolts folder

	* You need below files for querying the resutls
	
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/createdatabase.py
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/finalresults.py
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/histogram.py
	Exercise2_DoranBae/DoranBae_Files/EX2tweetwordcount/toppostgres.py


##########################################################
STEP 3 CREATE POSTGRES database
##########################################################

1. Create postgres database by running the following sh command 
	
	# python createdatabase.py 

##########################################################
STEP 4 RUN STREAMPARSE PROJECT
##########################################################

1. Under /src/spouts open tweets.py and put our twitter credentials. Without this, the streamparse won't run.

2. Run streamparse project
	
	# sparse run

	(press enter when warning sign comes up)

3. Let it run for as long as you like. I stopped it after 1 min. 

##########################################################
STEP 5 RUN FINALRESULTS.PY
##########################################################

1. Run finalresults.py WITH argument (any word of your choice). It gives you the number of counts for that particular word. If there is no count, python gives u "Empty Data"

	# python finalresults.py awesome

	Total number of occurences of "awesome" : 1

	# python finalresults.py christmas

	Empty Data

2. Run finalresults.py WITHOUT argument. It gives you the entire list of words & counts from postgres DB, sorted alphabetically in an ascending order, one word per line.

	# python finalresults.py 

##########################################################
STEP 6 RUN HISTOGRAM.PY
##########################################################

1. Run histogram.py WITH argument (any two numbers of your choice for range variables). It gives you all the words that their total number of occurrences between those two numbers line by line.

	# python histogram.py 4,6

##########################################################
STEP 7 RUN TOPPOSTGRES.PY
##########################################################

1. Run toppostgres.py WITH argument (any two numbers of your choice for range variables). It gives you all the words that their total number of occurrences between those two numbers line by line.

	# python toppostgres.py 


##########################################################
PRELOADED AMI
##########################################################

1. Search for: ami-a5551ecf (w205_Exercise2_DoranBae_FinalAMI)

##########################################################
SCREENSHOTS
##########################################################

1. For my screenshots please refer to:

Exercise2_DoranBae/DoranBae_Files/screenshots

##########################################################
PLOT.PNG
##########################################################

1. For my plot.png please refer to:

Exercise2_DoranBae/DoranBae_Files/plot


END OF DOCUMENT











