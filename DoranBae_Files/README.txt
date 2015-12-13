This is step by step instruction to replicate my exercise 2 submission.


##########################################################
STEP 1 SET UP A NEW INSTANCE
##########################################################
1. 	From AWS's AMI, search for AMI with ID : ami-596f1733
	This is AMI I created for Lab 9. I will re-use it for Exercise 2. 

2. Configure instance and launch it. In the security setting, make sure port 5432 is open. 

3. Connect to the instance and do the neccessary settings including mounting volume, and starting hadoop and postres.
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
	