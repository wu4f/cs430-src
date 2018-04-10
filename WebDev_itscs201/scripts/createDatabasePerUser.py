#!/usr/bin/python3

# Liz Lawrens
# New Beginnings 2016
# Final Term Project
# This script file will be used to create databases for each user/student.
# This program will create database with name as <username.db> taking each
# username listed in the file 'userlist'. 

import sqlite3
import os
import stat
import json

try:
    usersfile=open("userlist","r")
    d = dict([line.split() for line in usersfile])
    usersfile.close()
except:
    print("Error opening users file")
    exit()

try:
    with open("../www/users.py","w") as pyusers:
        pyusers.write("users = {}\n".format(json.dumps(d)))
        pyusers.close()
except:
    print("Error opening www/users.py")
    exit()

userList=[]
for key in d:
    userList.insert(len(userList),key)

for user in userList:
    conn = sqlite3.connect('../db/{0}.db'.format(user))
    conn.execute('''CREATE TABLE QUESTIONBANK
       (NUMBER VARCHAR(10) NOT NULL,
        CHAPTER INT NOT NULL,
        QUESTION  TEXT  NOT NULL,
        ANSWER    TEXT,
        STATUS    VARCHAR(50),
        SCOREID INT NOT NULL,
        HINT TEXT,
        PRIMARY KEY(NUMBER,CHAPTER));''')
    conn.close()
    os.chmod('../db/{0}.db'.format(user), 0o664)
