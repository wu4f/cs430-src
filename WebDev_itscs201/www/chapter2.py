# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This file contains the main page for chapter 2 questions
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
from questions2 import generateQuestions
from collections import OrderedDict

class Chapter2(flask.views.MethodView):
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
        cursor=conn.execute("SELECT count(*) from QUESTIONBANK where CHAPTER=2")
        if ((cursor.fetchone())[0]>0):
            crsr=conn.execute("SELECT NUMBER,QUESTION,STATUS,ANSWER from QUESTIONBANK where CHAPTER=2")
            for row in crsr:
                questions[row[0]]=row[1]
                if (row[2]=='SOLVED'):
                    solved.insert(len(solved),row[0])
                    answers[row[0]]=row[3]
        else: 
            quest=generateQuestions()
            questions=quest.genChap2(flask.session['username'])
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Successfully generated chapter 2 questions.\n"
            logfile.write(logentry)
        logfile.close()
        conn.close()
        return flask.render_template('chapter2.html', questions=questions,solved=solved,answers=answers)

    @login_required
    def post(self):
        try:
            if 'logout' in flask.request.form:
                flask.session.pop('username', None)
                return flask.redirect(flask.url_for('login'))
            if 'reset' in flask.request.form:
                conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
                conn.execute("delete from QUESTIONBANK where CHAPTER=2")
                conn.commit()
                conn.close()
                logpath = "../logs/"
                logfilename = logpath +  flask.session['username'] + ".log"
                logfile = open(logfilename,"a")
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 2 : Resetting Questions...\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter2'))
 
            winput=set(flask.request.form.values()).pop()
            winputkey=set(flask.request.form.keys()).pop()  
            if (winput==""):
                flask.flash("Error: Input is required. Enter a valid answer and resubmit.")
                return flask.redirect(flask.url_for('chapter2'))
        #There's an answer entered by student and we need to verify if its right or wrong and provide message accordingly
            conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
            cursor=conn.execute("SELECT ANSWER from QUESTIONBANK where CHAPTER=2 AND NUMBER='{0}'".format(winputkey))
            for row in cursor:
                answer=row[0]
        
       
        #logging some info in log files
            logpath = "../logs/"
            logfilename = logpath +  flask.session['username'] + ".log"
            logfile = open(logfilename,"a")
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 2 : " + winputkey + " : " + winput + "\n"
            logfile.write(logentry)
 
        #Some Question specific adjustments
            modifiedAnswer=""
            upperList=['1b','1f','3a','3b','5b','10a','10b','12a','12b']
            lowerList=['5d','6a','6b','8a','8b']
            if (winputkey in upperList): winput=winput.upper()
            if (winputkey in lowerList): winput=winput.lower()
            if (winputkey == "5b"):
                if(winput[2] == "0"):
                    winput=winput[:2]+winput[3]
            if (winputkey=="11a" or winputkey=="11b"):
                regex=re.compile('[0-9x<>()+-]+$')
                if(regex.match(winput)):
                    x=random.randint(1,100)
                    answer=str(int(answer)*x)
                    modifiedAnswer=str(eval(winput))
                else:
                    flask.flash("Input Error: Enter a valid answer and resubmit.")
                    return flask.redirect(flask.url_for('chapter2'))
 
            if (winputkey=="14a"):
                firstChar=winput[:1]
                if(firstChar=="."):winput='0'+winput
            if(winputkey=="15a" or winputkey=="15c"):winput=winput.replace(" ","")

        #Answer verification against database answers
            if (answer==winput or answer==modifiedAnswer):
                flask.flash("Good Job!!!")
                conn.execute("UPDATE QUESTIONBANK SET STATUS='SOLVED' where CHAPTER=2 AND NUMBER='{0}'".format(winputkey))
                if (winputkey=="11a" or winputkey=="11b"):
                    conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' where CHAPTER=2 AND NUMBER='{1}'".format(winput,winputkey))
                conn.commit()
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Correct" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter2'))
            else:
                cursor=conn.execute("SELECT HINT from QUESTIONBANK where CHAPTER=2 AND NUMBER='{0}'".format(winputkey))
                for row in cursor:
                    hint=row[0]
                flask.flash("The answer you provided ({0}) for question {1} is incorrect. Try again...\n\t\t{2}".format(winput,winputkey,hint))
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Wrong" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter2'))
    
        except:
            flask.flash("Check and correct the format of the answer you provided and try again...")
            conn.close()
            logpath = "../logs/"
            logfilename = logpath +  flask.session['username'] + ".log"
            logfile = open(logfilename,"a")

            logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Incorrect format" + "\n" + traceback.format_exc() +"\n"
            logfile.write(logentry)
            logfile.close()
            return flask.redirect(flask.url_for('chapter2'))
