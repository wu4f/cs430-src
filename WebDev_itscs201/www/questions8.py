# Liz Lawrens
# New Beginnings 2016
# Final Term Project - ITS CS201
# This file contains the code to generate random questions for each user.
# Each question has different algorithm/random number reneration.
# Questions and answers generated are stored in an ordered dictionary and 
# inserted into database.

import os
import datetime
import math
import random
import sqlite3
from collections import OrderedDict

class generateQuestions():
    def __init__(self):
        self.questions = OrderedDict()

    def genChap8(self, username):
        self.questions = OrderedDict()
        self.answers = OrderedDict()    
        #Generating questions for chapter 8 
        
        num = random.randint(1,5) 
        numans = 2 ** num
        forkans = ['a', 'b', 'c']
        random.shuffle(forkans)
        forkanswer = '{0}{1}{2}'.format(forkans[0],forkans[1],forkans[1])

        exceptions1 = 'Which of the following occur asynchronously?<br/>A. interrupts <br/>B. traps <br/>C. faults<br/>D. aborts<br/>'
        exceptions2 = 'Which of the following never returns to the process?<br/>A. interrupts<br/>B. traps<br/>C. faults<br/>D.aborts<br/>'
        exceptions3 = 'Which of the following exceptions are intentional?<br/>A. traps<br/>B. faults<br/>C. aborts<br/>'
        syscalls1 = 'Which Linux system call creates a new process almost identical to its parent?<br/>'
        syscalls2 = 'Which Linux system call retrieves the pid of the current process?<br/>'
        syscalls3 = 'Which Linux system call retrieves the pid of the current process parent pid?<br/>'
        syscalls4 = 'Which Linux system call suspends a process for a specified period of time?<br/>'
        syscalls5 = 'Which Linux system call executes a program, by loading and running into the current process?<br/>'
        syscalls6 = 'Which Linux system call suspends a running process until a signal is received?<br/>'
        fork1 = '<br/>pid = fork();<br/>if (pid != 0){{ <br/>&emsp;waitpid(-1,NULL,0);<br/> }} <br/>else {{ <br/>&emsp;printf("{0}");<br/> }} <br/>printf("{1}");'.format(forkans[0],forkans[1]) 
        fork2 = '<br/>for (i = 0; i < {0}; ++i) {{ <br/> &emsp;&emsp;fork();<br/> }} <br/>printf("hello ");<br/>exit(0);'.format(num)
        
        exceptions_q = [exceptions1, exceptions2, exceptions3]
        exceptions_dict = {exceptions1:'A', exceptions2:'D', exceptions3: 'A'}
        syscalls_q = [syscalls1, syscalls2, syscalls3, syscalls4, syscalls5, syscalls6]
        syscalls_dict = {syscalls1:'fork', syscalls2:'getpid', syscalls3:'getppid',syscalls4:'sleep', syscalls5:'execve', syscalls6:'pause'}

        random.shuffle(exceptions_q)
        random.shuffle(syscalls_q)
        
        self.questions['1'] = '1. (B&O Chapter 8.1) Choose the correct letter answer for the following three questions:<br/>{0}'.format(exceptions_q[0]) 
        self.answers['1'] ='{0}'.format(exceptions_dict.get(exceptions_q[0]))
        self.questions['2'] = '2. {0}'.format(exceptions_q[1]) 
        self.answers['2'] = '{0}'.format(exceptions_dict.get(exceptions_q[1]))
        self.questions['3'] = '3. {0}'.format(exceptions_q[2]) 
        self.answers['3'] = '{0}'.format(exceptions_dict.get(exceptions_q[2]))
        self.questions['4'] = '4. (B&O Chapter 8.1) Write the name of the system call below without the argument list. <br/> For example, if the solution is "exit(int status)", answer "exit".<br/>{0}'.format(syscalls_q[0])  
        self.answers['4'] = '{0}'.format(syscalls_dict.get(syscalls_q[0]))
        self.questions['5'] = '5. {0}'.format(syscalls_q[1])
        self.answers['5'] = '{0}'.format(syscalls_dict.get(syscalls_q[1]))
        self.questions['6'] = '6. {0}'.format(syscalls_q[2])
        self.answers['6'] = '{0}'.format(syscalls_dict.get(syscalls_q[2]))
        self.questions['7'] = '7. (B&O Chapter 8.4) What is the output of this program?<br/>{0}'.format(fork1)
        self.answers['7'] = '{0}'.format(forkanswer)
        self.questions['8'] = '8. (B&O Chapter 8.4)How many "hello" output lines does this program print?{0}'.format(fork2)
        self.answers['8'] = '{0}'.format(numans)

	#Store the Questions and answers in database
        conn=sqlite3.connect('../db/{0}.db'.format(username))
        id=1
        for qkey,question in self.questions.items():
           conn.execute("INSERT INTO QUESTIONBANK (NUMBER,CHAPTER,QUESTION,STATUS,SCOREID) VALUES('{0}',8,'{1}','UNSOLVED',{2})".format(qkey,question,id))
           id=id+1
        for akey,answer in self.answers.items():
           conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' WHERE CHAPTER=8 AND NUMBER='{1}'".format(answer,akey))
        conn.commit()
        conn.close()
        
        return self.questions
