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
        self.questions=OrderedDict()
    
    #Function to generate the questions based on some random value/ encoding algorithm
    def genChap6(self,username):
        self.questions=OrderedDict()
        self.answers=OrderedDict()

        #Generating questions for chapter 6
        #Question 1a through d
        options=[4,8,32]
        random.shuffle(options)
        B=options[0]
        if(B==4):
            E=1
            S=256
        elif(B==8):
            E=4
            S=32
        else:
            E=32
            S=1
       
        b=int(str(math.log(B,2))[:1])
        s=int(str(math.log(S,2))[:1])
        t=32-(s+b)

        self.questions['1a']='1. (B&O Chapter 6.9) Consider a {0}-way set associative cache on a 32-bit machine (m=32) with {1} set(s) and a line/block size of {2}.<br/>a. How large is this cache in bytes?'.format(E,S,B)
        self.answers['1a']=1024
        self.questions['1b']='b. How many bits of the address are used to indicate the block offset?'
        self.answers['1b']=b
        self.questions['1c']='c. How many bits of the address are used to indicate the set index?'
        self.answers['1c']=s
        self.questions['1d']='d. How many bits of the address are used to indicate the tag?'
        self.answers['1d']=t
	
        #Questions 2a through e
        addOptions=['0x037A','0x0D53','0x0CB4','0x0A31']
        random.shuffle(addOptions)
        address=addOptions[0]
        if (address == '0x037A'):
            bo='0x2'
            si='0x6'
            ct='0x1B'
            horm='MISS'
            ret='NONE'
        elif (address == '0x0D53'):
            bo='0x3'
            si='0x4'
            ct='0x6A'
            horm='MISS'
            ret='NONE'
        elif (address == '0x0CB4'):
            bo='0x0'
            si='0x5'
            ct='0x65'
            horm='MISS'
            ret='NONE'
        elif (address == '0x0A31'):
            bo='0x1'
            si='0x4'
            ct='0x51'
            horm='MISS'
            ret='NONE'
        else:
            ret='NONE'
        
        self.questions['2a']='2. (B&O Chapter 6.12 - 6.15) Consider the 2-way set associative cache below with (S,E,B,m) = (8,2,4,13). Cache lines that are blank are invalid.<br/>Set&emsp;Tag&emsp;&emsp;Data0-3&emsp;&emsp;&emsp;&emsp;Tag&emsp;&emsp;Data0-3<br/>-------------------------------&emsp;&emsp;&emsp;&emsp;-------------------------<br/>&nbsp;0&nbsp;&nbsp;&emsp;09&nbsp;&nbsp;|&nbsp;&nbsp;86 30 3F 10&emsp;&emsp;&emsp;&emsp;00&nbsp;&nbsp;|<br/>&nbsp;1&nbsp;&nbsp;&emsp;45&nbsp;&nbsp;|&nbsp;&nbsp;60 4F E0 23&emsp;&emsp;&emsp;&emsp;38&nbsp;&nbsp;|&nbsp;&nbsp;00 BC 0B 37<br/>&nbsp;2&nbsp;&nbsp;&emsp;EB&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;0B&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;3&nbsp;&nbsp;&emsp;06&nbsp;&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;32&nbsp;&nbsp;|&nbsp;&nbsp;12 08 7B AD<br/>&nbsp;4&nbsp;&nbsp;&emsp;C7&nbsp;|&nbsp;&nbsp;06 78 07 C5&emsp;&emsp;&emsp;&emsp;05&nbsp;&nbsp;|&nbsp;&nbsp;40 67 C2 3B<br/>&nbsp;5&nbsp;&nbsp;&emsp;71&nbsp;&nbsp;|&nbsp;&nbsp;0B DE 18 4B&emsp;&emsp;&emsp;&nbsp;&nbsp;6E&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;6&nbsp;&nbsp;&emsp;91&nbsp;&nbsp;|&nbsp;&nbsp;A0 B7 26 2D&emsp;&emsp;&emsp;&nbsp;&nbsp;F0&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;7&nbsp;&nbsp;&emsp;46&nbsp;&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;DE&nbsp;&nbsp;|&nbsp;&nbsp;12 C0 88 37<br/>Consider an access to {0}<br/>[Provide answer to below in hex eg. 0xFF]<br/>a. What is the block offset of this address in hex?'.format(address)
        self.answers['2a']=bo
        self.questions['2b']='b. What is the set index of this address in hex?'
        self.answers['2b']=si
        self.questions['2c']='c. What is the cache tag of this address in hex?'
        self.answers['2c']=ct
        self.questions['2d']='d. Does this access hit or miss in the cache?<br/>[Provide answer as &#39;hit&#39; or &#39;miss&#39;]'
        self.answers['2d']=horm
        self.questions['2e']='e. What value is returned if it is a hit?<br/>[Provide answer as &#39;None&#39; if it is a miss]'
        self.answers['2e']=ret

        #Questions 3
        dict={'0':'0x0120 0x0121 0x0122 0x0123','3':'0x064C 0x064D 0x064E 0x064F','5':'0x0E34 0x0E35 0x0E36 0x0E37','6':'0x1238 0x1239 0x123A 0x123B','7':'0x1BDC 0x1BDD 0x1BDE 0x1BDF'}
        setnumOpt=['0','3','5','6','7']
        random.shuffle(setnumOpt)
        setnum=setnumOpt[0]
        ans=dict.get(setnum)
        self.questions['3a']='3. (B&O Chapter 6.16) Consider the 2-way set associative cache in the previous question (2) with (S,E,B,m) = (8,2,4,13).<br/>a. List all addresses that will hit in set {0}.[Provide each address in hex (in ascending order) with space delimited eg. 0x0111 0x0222 0x1AAA 0x1BBB]'.format(setnum)
        self.answers['3a']=ans
        
        #Questions 4a through e
        addOptions=['0x18F3','0x064E','0x0645','0x0634']
        random.shuffle(addOptions)
        address=addOptions[0]
        if (address == '0x18F3'):
            bo='0x3'
            si='0x4'
            ct='0xC7'
            horm='HIT'
            ret='0xC5'
        elif (address == '0x064E'):
            bo='0x2'
            si='0x3'
            ct='0x32'
            horm='HIT'
            ret='0xAD'
        elif (address == '0x0645'):
            bo='0x1'
            si='0x1'
            ct='0x32'
            horm='HIT'
            ret='0x4F'
        elif (address == '0x0634'):
            bo='0x0'
            si='0x5'
            ct='0x31'
            horm='HIT'
            ret='0xAB'
        else:
            ret='NONE'

        self.questions['4a']='4. (B&O Chapter 6.12 - 6.15) Consider the 2-way set associative cache below with (S,E,B,m) = (8,2,4,13). Cache lines that are blank are invalid.<br/>Set&emsp;Tag&emsp;&emsp;Data0-3&emsp;&emsp;&emsp;&emsp;Tag&emsp;&emsp;Data0-3<br/>-------------------------------&emsp;&emsp;&emsp;&emsp;-------------------------<br/>&nbsp;0&nbsp;&nbsp;&emsp;08&nbsp;&nbsp;|&nbsp;&nbsp;86 32 3F 12&emsp;&emsp;&emsp;&emsp;03&nbsp;&nbsp;|<br/>&nbsp;1&nbsp;&nbsp;&emsp;32&nbsp;&nbsp;|&nbsp;&nbsp;56 4F D3 19&emsp;&emsp;&emsp;&emsp;38&nbsp;&nbsp;|&nbsp;&nbsp;11 BC D7 37<br/>&nbsp;2&nbsp;&nbsp;&emsp;AD&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;B0&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;3&nbsp;&nbsp;&emsp;23&nbsp;&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;32&nbsp;&nbsp;|&nbsp;&nbsp;21 12 AD 82<br/>&nbsp;4&nbsp;&nbsp;&emsp;C7&nbsp;|&nbsp;&nbsp;06 78 07 C5&emsp;&emsp;&emsp;&emsp;05&nbsp;&nbsp;|&nbsp;&nbsp;40 67 C2 3B<br/>&nbsp;5&nbsp;&nbsp;&emsp;31&nbsp;&nbsp;|&nbsp;&nbsp;AB 91 76 F7&emsp;&emsp;&emsp;&nbsp;&nbsp;4A&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;6&nbsp;&nbsp;&emsp;41&nbsp;&nbsp;|&nbsp;&nbsp;B0 63 CE 8A&emsp;&emsp;&emsp;&nbsp;&nbsp;BF&nbsp;&nbsp;|&nbsp;&nbsp;<br/>&nbsp;7&nbsp;&nbsp;&emsp;5A&nbsp;&nbsp;|&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;12&nbsp;&nbsp;|&nbsp;&nbsp;DE C3 66 29<br/>Consider an access to {0}<br/>[Provide answer to below in hex eg. 0xFF]<br/>a. What is the block offset of this address in hex?'.format(address)
        self.answers['4a']=bo
        self.questions['4b']='b. What is the set index of this address in hex?'
        self.answers['4b']=si
        self.questions['4c']='c. What is the cache tag of this address in hex?'
        self.answers['4c']=ct
        self.questions['4d']='d. Does this access hit or miss in the cache?<br/>[Provide answer as &#39;hit&#39; or &#39;miss&#39;]'
        self.answers['4d']=horm
        self.questions['4e']='e. What value is returned if it is a hit?<br/>[Provide answer as &#39;None&#39; if it is a miss]'
        self.answers['4e']=ret

        #Question 5a through c
        varOpts=['int','short','long']
        random.shuffle(varOpts)
        vartype=varOpts[0]
        if (vartype == 'int'):
            ans=1024
            hitrate='75%'
        if (vartype == 'short'):
            ans=2048
            hitrate='87.5%'
        if (vartype == 'long'):
            ans=512
            hitrate='50%'

        self.questions['5a']='5. (B&O Chapter 6.18) Consider a direct mapped cache on a 64-bit machine (m=64) with 256 sets and a line/block size of 16.<br/>a. How large is this cache in bytes?'
        self.answers['5a']=4096
        self.questions['5b']='b. How many {0} data type values can fit into this cache?'.format(vartype)
        self.answers['5b']=ans
        self.questions['5c']='c. What would be the hit rate for sequential access of this data type through this cache?<br/>[Provide your answer as a decimal percentage between 0% and 100%]'
        self.answers['5c']=hitrate     

	#Store the Questions and answers in database
        conn=sqlite3.connect('../db/{0}.db'.format(username))
        id=1
        for qkey,question in self.questions.items():
            conn.execute("INSERT INTO QUESTIONBANK (NUMBER,CHAPTER,QUESTION,STATUS,SCOREID) VALUES('{0}',6,'{1}','UNSOLVED',{2})".format(qkey,question,id))
            id=id+1
        for akey,answer in self.answers.items():
            conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' WHERE CHAPTER=6 AND NUMBER='{1}'".format(answer,akey))
        conn.commit()
        conn.close()
        
        return self.questions

