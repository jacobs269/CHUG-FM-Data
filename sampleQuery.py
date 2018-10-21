import numpy as np
import cv2
import sqlite3
#__________________________________________
#PART 1: GRAB relevant user Ids from both databases

img_id=str(3) #3 is the ID of Houston
####Grab the user ids from database1
conn = sqlite3.connect('dbM1COPY.sqlite3')
c = conn.cursor()
v1=c.execute('SELECT id from getlabels_user where id>='+str(119)+' AND id<='+str(131)+' AND successRate='+str(1))
holder1 = []
for nonCheat in v1:
	nextID = nonCheat[0]
	holder1.append(nextID)
v2=c.execute('SELECT id from getlabels_user where id>='+str(240)+' AND id<='+str(250)+' AND successRate='+str(1))
holder2 = []
for nonCheat in v2:
	nextID = nonCheat[0]
	holder2.append(nextID)
db1IDs = tuple(holder1+holder2)

###Grab the user ids from database2
conn2 = sqlite3.connect('dbM2COPY.sqlite3')
c2 = conn2.cursor()
v3=c2.execute('SELECT id from getlabels_user where id>='+str(247)+' AND id<='+str(277)+' AND successRate='+str(1))
holder = []
for nonCheat in v3:
	nextID = nonCheat[0]
	holder.append(nextID)
db2IDs = tuple(holder)

#____________________________________________________
#PART 2: GRAB ANSWERS from both databases for relevant user ids
answersDB1 = c.execute('SELECT user_id,water,land,unknown,imgrow,imgcol from getlabels_answer where img_id='+img_id+' AND unknown=0 AND user_id IN '+str(db1IDs))
answersDB2 = c2.execute('SELECT user_id,water,land,unknown,imgrow,imgcol from getlabels_answer where img_id='+img_id+' AND unknown=0 AND user_id IN '+str(db2IDs))

#********************************
answersDB1 = answersDB1.fetchall()
answersDB2 = answersDB2.fetchall()
#********************************
#These above two objects contain all of the NOT UNKNOWN answers for Houston from users who had a perfect success rate on the test pixels.
#print(answersDB1)
#print(answersDB2)
#____________________________________________________
#PART 3: GRAB Houston results from both databases for relevant user ids
v1 = c.execute('SELECT resultfile from getlabels_result where user_id IN '+str(db1IDs)+' AND image_id='+img_id)
resultsDB1 = []
for link in v1.fetchall():
	s = str(link[0])
	img = cv2.imread(s)
	resultsDB1.append(img)
v2 = c2.execute('SELECT resultfile from getlabels_result where user_id IN '+str(db2IDs)+' AND image_id='+img_id)
resultsDB2 = []
for link in v2.fetchall():
	s = str(link[0])
	img = cv2.imread(s)
	resultsDB2.append(img)

#**************************
##resultsDB1 and resultsDB2 contain the houston results for users who had perfect success rate
#**************************



