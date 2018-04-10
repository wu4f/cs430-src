# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This file contains the code for scores calculation and display
# For normal users it will query the database to get the scores
# for each chapter and displays results when user clicks on the
# display tab. Solved questions will be displayed as green and 
# unsolved ones will be displayed as red.
# Admin user will be able to view scores of every other user. The
# result will be displayed in a tabular form with each user listed
# and number of solved questions from each chapter for each user 
# will also be listed.

import flask, flask.views
from utils import login_required
from login import users
import os
import time
import sqlite3
from collections import OrderedDict

class Score(flask.views.MethodView):
    @login_required
    def get(self):
        scores = {}					#scores stored in a dictionary
        solved = {}					#solved question info stored in dictionary
        questions = OrderedDict()			#all the questions present in database is stored as an ordered dictionary
        account = flask.session['username']
        if account == 'admin':				#if user is admin, display results for every other user
            for user in users.keys():			#for each user in userlist, query info from database	
                conn=sqlite3.connect('../db/{0}.db'.format(user))
                cursor=conn.execute("SELECT COUNT(*) from QUESTIONBANK where CHAPTER=2 AND STATUS='SOLVED'")
                for row in cursor:
                    userStatus='Chapter2 : '+str(row[0])
                cursor=conn.execute("SELECT COUNT(*) from QUESTIONBANK where CHAPTER=3 AND STATUS='SOLVED'")
                for row in cursor:
                    userStatus=userStatus +' | Chapter3 : '+str(row[0])
                cursor=conn.execute("SELECT COUNT(*) from QUESTIONBANK where CHAPTER=5 AND STATUS='SOLVED'")
                for row in cursor:
                    userStatus=userStatus +' | Chapter5 : '+str(row[0])
                cursor=conn.execute("SELECT COUNT(*) from QUESTIONBANK where CHAPTER=6 AND STATUS='SOLVED'")
                for row in cursor:
                    userStatus=userStatus +' | Chapter6 : '+str(row[0])
                cursor=conn.execute("SELECT COUNT(*) from QUESTIONBANK where CHAPTER=8 AND STATUS='SOLVED'")
                for row in cursor:
                    userStatus=userStatus +' | Chapter8 : '+str(row[0])
                scores[user]=userStatus

                cursor=conn.execute("SELECT NUMBER,CHAPTER from QUESTIONBANK ORDER BY SCOREID")
                for row in cursor:
                    questions[user+row[0]+str(row[1])]=row[0]

                cursor=conn.execute("SELECT NUMBER,CHAPTER from QUESTIONBANK where STATUS='SOLVED'")
                for row in cursor:
                    solved[user+row[0]+str(row[1])]=row[0]

                conn.close()
            return flask.render_template('adminscore.html', scores=scores, users=sorted(scores.keys()), questions=questions, solved=solved, chapters=sorted(set(['2','3','5','6','8'])))	#render adminscore.html with all the details
        else:
            conn=sqlite3.connect('../db/{0}.db'.format(account))	#this part gets executed for normal users
            cursor=conn.execute("SELECT NUMBER,CHAPTER from QUESTIONBANK ORDER BY SCOREID")
            for row in cursor:
                questions[row[0]+str(row[1])]=row[0]

            cursor=conn.execute("SELECT NUMBER,CHAPTER from QUESTIONBANK where STATUS='SOLVED'")
            for row in cursor:
                solved[row[0]+str(row[1])]=row[0]
            conn.close()  
            return flask.render_template('score.html', questions=questions, solved=solved, chapters=sorted(set(['2','3','5','6','8'])))	#renders score.html
