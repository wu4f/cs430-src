# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This file contains the main page for chapter 3 questions
# When user clicks on the link for first time, it will generate the questions
# randomly, store it in database and displays it to the user. Each user will
# get unique questions based on some inputs like username, and some algorithms
# implemented to generate random values. Every subsequent access will query 
# the database and display the results retrieved from database.
# There is also some logging mechanism implemented. Logs are saved in /logs
# directory and has file name as <username>.log

import flask, flask.views
from utils import login_required
import os
import time
import sqlite3
import re
import traceback
import random
from questions3 import generateQuestions
from collections import OrderedDict

class Chapter3(flask.views.MethodView):
    @login_required
    def get(self):
        questions=OrderedDict()
        answers={}
        solved=[]
        #logging some info in log files
        logpath = "../logs/"
        logfilename = logpath +  flask.session['username'] + ".log"
        logfile = open(logfilename,"a")

        conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
        cursor=conn.execute("SELECT count(*) from QUESTIONBANK where CHAPTER=3")
        if ((cursor.fetchone())[0]>0):
            crsr=conn.execute("SELECT NUMBER,QUESTION,STATUS,ANSWER from QUESTIONBANK where CHAPTER=3")
            for row in crsr:
                questions[row[0]]=row[1]
                if (row[2]=='SOLVED'):
                    solved.insert(len(solved),row[0])
                    answers[row[0]]=row[3]
        else: 
            quest=generateQuestions()
            questions=quest.genChap3(flask.session['username'])
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Successfully generated chapter 3 questions.\n"
            logfile.write(logentry)
        logfile.close()
        conn.close()
        return flask.render_template('chapter3.html', questions=questions,solved=solved,answers=answers)

    @login_required
    def post(self):
        try:
            if 'logout' in flask.request.form:
                flask.session.pop('username', None)
                return flask.redirect(flask.url_for('login'))
            if 'reset' in flask.request.form:
                conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
                conn.execute("delete from QUESTIONBANK where CHAPTER=3")
                conn.commit()
                conn.close()

                logpath = "../logs/"
                logfilename = logpath +  flask.session['username'] + ".log"
                logfile = open(logfilename,"a")
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 3 : Resetting Questions...\n"
                logfile.write(logentry)
                logfile.close()

                return flask.redirect(flask.url_for('chapter3'))

            winput=set(flask.request.form.values()).pop()
            winputkey=set(flask.request.form.keys()).pop()  
            if (winput==""):
                flask.flash("Error: Input is required. Enter a valid answer and resubmit.")
                return flask.redirect(flask.url_for('chapter3'))
        #There's an answer entered by student and we need to verify if its right or wrong and provide message accordingly
            conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
            cursor=conn.execute("SELECT ANSWER from QUESTIONBANK where CHAPTER=3 AND NUMBER='{0}'".format(winputkey))
            for row in cursor:
                answer=row[0]
        
       
        #logging some info in log files
            logpath = "../logs/"
            logfilename = logpath +  flask.session['username'] + ".log"
            logfile = open(logfilename,"a")
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 3 : " + winputkey + " : " + winput + "\n"
            logfile.write(logentry)
 
        #Some Question specific adjustments
            modifiedAnswer=""
            tweakList=['1b','1c','1d','1e','1f']
            if (winputkey in tweakList):
                winput = winput[:2]+winput[2:].upper()
            upperList=['2d','10a']
            if (winputkey in upperList):winput = winput.upper()
            stripList=['3a','3b','3c','5a','5b','12','13a','13b','13c','13d']
            if (winputkey in stripList):
                winput=winput.replace(" ","")
                winput=winput.replace("(","")
                winput=winput.replace(")","")
            if (winputkey=="4a"):
                winput=winput.replace(" ","")
                winput=winput.replace("(","")
                winput=winput.replace(")","")
                winput=winput[:6]+" "+winput[6:]
            if (winputkey=="6b" or winputkey=="6d"):
                winput=winput[:5]+winput[5:].replace(" ","")
            if (winputkey =="5a" or winputkey == "5b" or winputkey == "4a" or winputkey == "13b" or winputkey == "13c" or winputkey == "13d"):
                if all(char in winput for char in answer):
                    answer=winput
            if (winputkey =="12"):
                if (all(char in winput for char in answer) | all(char in winput for char in "result+=a+b")):
                    answer=winput
        #Answer verification against database answers
            if (answer==winput or answer==modifiedAnswer):
                flask.flash("Good Job!!!")
                conn.execute("UPDATE QUESTIONBANK SET STATUS='SOLVED' where CHAPTER=3 AND NUMBER='{0}'".format(winputkey))
                conn.commit()
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Correct" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter3'))
            else:
                flask.flash("The answer you provided ({0}) for question {1} is incorrect. Try again...".format(winput,winputkey))
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Wrong" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter3'))
    
        except:
            flask.flash("Check and correct the format of the answer you provided and try again...")
            conn.close()
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Incorrect format" + "\n" + traceback.format_exc() +"\n"
            logfile.write(logentry)
            logfile.close()
            return flask.redirect(flask.url_for('chapter3'))
