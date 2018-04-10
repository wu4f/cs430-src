# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This file contains the main page for chapter 6 questions
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
from questions6 import generateQuestions
from collections import OrderedDict

class Chapter6(flask.views.MethodView):
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
        cursor=conn.execute("SELECT count(*) from QUESTIONBANK where CHAPTER=6")
        if ((cursor.fetchone())[0]>0):
            crsr=conn.execute("SELECT NUMBER,QUESTION,STATUS,ANSWER from QUESTIONBANK where CHAPTER=6")
            for row in crsr:
                questions[row[0]]=row[1]
                if (row[2]=='SOLVED'):
                    solved.insert(len(solved),row[0])
                    answers[row[0]]=row[3]
        else: 
            quest=generateQuestions()
            questions=quest.genChap6(flask.session['username'])
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Successfully generated chapter 6 questions.\n"
            logfile.write(logentry)
        logfile.close()
        conn.close()
        return flask.render_template('chapter6.html', questions=questions,solved=solved,answers=answers)

    @login_required
    def post(self):
        try:
            if 'logout' in flask.request.form:
                flask.session.pop('username', None)
                return flask.redirect(flask.url_for('login'))
            if 'reset' in flask.request.form:
                conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
                conn.execute("delete from QUESTIONBANK where CHAPTER=6")
                conn.commit()
                conn.close()

                logpath = "../logs/"
                logfilename = logpath +  flask.session['username'] + ".log"
                logfile = open(logfilename,"a")
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 6 : Resetting Questions...\n"
                logfile.write(logentry)
                logfile.close()

                return flask.redirect(flask.url_for('chapter6'))

            winput=set(flask.request.form.values()).pop()
            winputkey=set(flask.request.form.keys()).pop()  
            if (winput==""):
                flask.flash("Error: Input is required. Enter a valid answer and resubmit.")
                return flask.redirect(flask.url_for('chapter6'))
        #There's an answer entered by student and we need to verify if its right or wrong and provide message accordingly
            conn=sqlite3.connect('../db/{0}.db'.format(flask.session['username']))
            cursor=conn.execute("SELECT ANSWER from QUESTIONBANK where CHAPTER=6 AND NUMBER='{0}'".format(winputkey))
            for row in cursor:
                answer=row[0]
        
       
        #logging some info in log files
            logpath = "../logs/"
            logfilename = logpath +  flask.session['username'] + ".log"
            logfile = open(logfilename,"a")
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : Chapter 6 : " + winputkey + " : " + winput + "\n"
            logfile.write(logentry)
 
        #Some Question specific adjustments
            modifiedAnswer=""
            tweakList=['2b','2c','4b','4c','4e']
            if (winputkey in tweakList):
                winput = winput[:2]+winput[2:].upper()
            upperList=['2d','2e','4d']
            if (winputkey in upperList):winput = winput.upper()
            if (winputkey =='3a'):
                temp=winput.split()
                newtemp=[]
                for x in temp:
                    if(len(x)==5):
                        newtemp.insert(0,x[:2]+'0'+x[2:])
                    else:
                        newtemp.insert(0,x)
                newtemp.sort()
                winput=''
                for x in newtemp:
                    winput=winput+x+' '
                winput=winput[:-1]
            if (winputkey == '5c'):
                if (winput[-1:] != '%'):winput = winput+'%'

        #Answer verification against database answers
            if (answer==winput or answer==modifiedAnswer):
                flask.flash("Good Job!!!")
                conn.execute("UPDATE QUESTIONBANK SET STATUS='SOLVED' where CHAPTER=6 AND NUMBER='{0}'".format(winputkey))
                conn.commit()
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Correct" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter6'))
            else:
                flask.flash("The answer you provided ({0}) for question {1} is incorrect. Try again...".format(winput,winputkey))
                conn.close()
                logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Answered Wrong" + "\n"
                logfile.write(logentry)
                logfile.close()
                return flask.redirect(flask.url_for('chapter6'))
    
        except:
            flask.flash("Check and correct the format of the answer you provided and try again...")
            conn.close()
            logentry = time.asctime() + " : " + flask.request.remote_addr + " : " + "Incorrect format" + "\n" + traceback.format_exc() +"\n"
            logfile.write(logentry)
            logfile.close()
            return flask.redirect(flask.url_for('chapter6'))
