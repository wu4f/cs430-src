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
    
    #function to adjust the length of binary to 8 bits if its less than that (Used in Question 1a through f)
    def adjustBinaryLength(self,binform):
        length=len(binform)
        if(length<8):
            l=8-length
            for l in range(0,l):
                binform='0'+binform
                l=l-1
        return binform
      
    #Function to generate twos complement format (Used in Question 2a and b)
    def twos_complement(self,value,bits):
        if(value & (1 << (bits - 1))) != 0: #if sign bit is set
            value = value - (1 << bits)     #compute negative value
        return value			    #return positive value as is
 
    #Function to generate the questions based on some random value/ encoding algorithm
    def genChap2(self,username):
        self.questions=OrderedDict()
        self.answers=OrderedDict()
        self.hints=OrderedDict()

        #Generating questions for chapter 2
        #Question 1a through f

        #commenting this out as .from_bytes giving problems while executing in python3.4 version. Generating numbers using random
        #num=int.from_bytes(username.encode(), 'little') #generate a unique number with username as input
        #num1=num%256
        #num2=num%164
        #num3=num%199

        num1=random.randint(100,256)
        num2=random.randint(100,256)
        num3=random.randint(100,256)
        num4=random.randint(100,256)
        num5=random.randint(100,256)
        num6=random.randint(100,256)
        binform1='{0:b}'.format(num1)
        binform2='{0:b}'.format(num2)
        hexform2=('{0:x}'.format(num2)).upper()
        hexform3=('{0:x}'.format(num3)).upper()
        binform4='{0:b}'.format(num4)        
        binform5='{0:b}'.format(num5)
        hexform5=('{0:x}'.format(num5)).upper()
        hexform6=('{0:x}'.format(num6)).upper()

        binform1=self.adjustBinaryLength(binform1)
        binform2=self.adjustBinaryLength(binform2)
        binform4=self.adjustBinaryLength(binform4)
        binform5=self.adjustBinaryLength(binform5)
        
    
        self.questions['1a']='1.(B&O Ch.2.1) Assuming use of unsigned numbers, perform the following conversions. Use 8 bits for representing binary numbers (eg.00110011) and 2 digits for hexadecimal numbers(eg. FF). <br/>a. Convert the decimal {0} to binary.'.format(num1)
        self.answers['1a']='{0}'.format(binform1)
        self.hints['1a']='[Hint: How about dividing by 2 and keeping track of remainder!]'
        self.questions['1b']='b. Convert the binary {0} to hexadecimal.'.format(binform2)
        self.answers['1b']='{0}'.format(hexform2)
        self.hints['1b']='[Hint: How about splitting the number into groups of 4 and translating each group of bits into corresponding hex digits!]'
        self.questions['1c']='c. Convert the hexadecimal {0} to decimal.'.format(hexform3)
        self.answers['1c']='{0}'.format(num3)
        self.hints['1c']='[Hint: Multiply each place value by the corresponding power of sixteen!]'
        self.questions['1d']='d. Convert the binary {0} to decimal.'.format(binform4)
        self.answers['1d']='{0}'.format(num4)
        self.hints['1d']='[Hint: Multiply each place value by the corresponding power of two!]'
        self.questions['1e']='e. Convert the hexadecimal {0} to binary.'.format(hexform5)
        self.answers['1e']='{0}'.format(binform5)
        self.hints['1e']='[Hints: Expand each hex digit to corresponding binary]'
        self.questions['1f']='f. Convert the decimal {0} to hexadecimal.'.format(num6)
        self.answers['1f']='{0}'.format(hexform6)
        self.hints['1f']='[Hint: How about converting to binary and then to hex!]'
    
	#Questions 2a and b
        bitval=random.randint(4,8)
        max=(2 ** bitval) - 1
        b=0
        while(b==0):
            b=bin(random.randint(2 ** (bitval-1),max-1))
        binary_string = b[2:]
        value = self.twos_complement(int(binary_string,2),bitval)

        self.questions['2a']='2.(B&O Ch.2.2)<br/>a. Give the binary representation of the number {0} in a {1}-bit twos complement format.'.format(value,bitval)
        self.answers['2a']=binary_string
        self.hints['2a']='[Hint: For a number x, such that Tmin <= x <= Tmax, T2B(x) is the unique w-bit pattern that encodes x.]'
        self.questions['2b']='b. Give the binary representation of the number -1 in a {0}-bit twos complement format.'.format(bitval)
        self.answers['2b']=''.rjust(bitval,'1')
        self.hints['2b']='[Hint: For a number x, such that Tmin <= x <= Tmax, T2B(x) is the unique w-bit pattern that encodes x.]'

        #Questions 3a and b
        val=random.randint(1,4)*8
        self.questions['3a']='3.(B&O Ch.2.2) Give the hex representation of the following:<br/>(Give your answer as a hexadecimal value - eg. 0xFFFF)<br/>a. Give the hex representation of the most negative {0}-bit twos complement number.'.format(val)
        self.answers['3a']='0X80'.ljust(4+((val//8)-1)*2,'0')
        self.hints['3a']='[Hint: Tmin = -2 raised to the power of (w-1) where w = word size]'
        self.questions['3b']='b. Give the hex representation of the largest positive {0}-bit twos complement number.'.format(val)
        self.answers['3b']='0X7F'.ljust(4+((val//8)-1)*2,'F')
        self.hints['3b']='[Hint: Tmax = 2^(w-1) - 1 where ^ implies raised to power of and w = word size]'

        #Questions 4a and b
        bitval=random.randint(4,8)
        max=(2 ** bitval) - 1
        b=0
        while(b==0):
            b=bin(random.randint(2 ** (bitval-1),max-1))
        binary_string = b[2:]
        value = self.twos_complement(int(binary_string,2),bitval)
       
        self.questions['4a']='4.(B&O Ch.2.2)<br/>a. Consider the {0}-bit twos complement number {1}, what is its decimal value?'.format(bitval,binary_string) 
        self.answers['4a']=value
        self.questions['4b']='b. Consider the {0}-bit unsigned number {1}, what is its decimal value?'.format(bitval,binary_string)
        self.answers['4b']=int(binary_string,2)

        #Questions 5a,b,c and d
        val=hex(random.randint(100,256))
        xor1=random.randint(100,256)
        xor2=random.randint(100,256)
        xor=xor1^xor2
        self.questions['5a']='5.(B&O Ch.2.2)<br/>a. What is the value of !{0} ?'.format(val)
        self.answers['5a']=0
        self.questions['5b']='b. What is the value of ~{0} ? (Give your answer as a hexadecimal-eg.0xFF)'.format(val)
        self.answers['5b']=hex(~(int(val,16)) & 0xFF).upper()
        self.questions['5c']='c. What is the value of !!{0} ?'.format(val)
        self.answers['5c']=1
        self.questions['5d']='d. What is the value of {0} ^ {1} ? (Give your answer as a hexadecimal - eg.0xFF)'.format(hex(xor1),hex(xor2))
        self.answers['5d']=hex(xor)

        #Questions 6a and b
        val1="0x{:04x}".format(random.randint(4369,16384))
        val2="0x{:02x}".format(random.randint(8,127))
        ans1="0x{:04x}".format(int(val1,16) + int(val2,16))
        val3="0x{:04x}".format(random.randint(4369,16384))
        val4="0x{:02x}".format(random.randint(8,127))
        ans2="0x{:04x}".format(int(val3,16) - int(val4,16))
        self.questions['6a']='6.(B&O Ch.2.1) Assuming the use of unsigned values, perform the following hex arithmetic :<br/>(Give your answer as a hexadecimal-eg.0xFFFF)<br/> a. {0} + {1} = ?'.format(val1,val2)
        self.answers['6a']=ans1
        self.questions['6b']='b. {0} - {1} = ?'.format(val3,val4)
        self.answers['6b']=ans2
       
        #Questions 7a and b
        options={'c':8,'&c':64,'ui':32,'i':32,'f':32,'d':64,'dp':64}
        keyList=['c','&c','ui','i','f','d','dp']
        random.shuffle(keyList)
        q1=keyList[0]
        q2=keyList[1]
        a1=options.get(q1)
        a2=options.get(q2)
        self.questions['7a']='7. (B&O Ch.2.1) Consider the following declaration:<br/>int i;<br/>char c;<br/>unsigned int ui;<br/>float f;<br/>double d;<br/>double* dp;<br/>List the number of bits used to represent the following terms assuming C on x86.<br/>a. {0}'.format(q1)
        self.answers['7a']=a1
        self.questions['7b']='b. {0}'.format(q2)
        self.answers['7b']=a2

        #Questions 8a and b
        self.questions['8a']='8. (B&O Ch.2.1) Consider this program :<br />#include&lt;stdio.h&gt;<br />int main(){<br />int i=0x40302010;<br />unsigned char *cp;<br />cp = (unsigned char *) &i;<br />printf("%x",*cp);<br />}<br />(Give your answer as a hexadecimal-eg.0xFF)<br/>a. What is its output on a little endian machine?'
        self.answers['8a']='0x10'
        self.questions['8b']='b. What is its output on a big endian machine?'
        self.answers['8b']='0x40'

        #Questions 9a and b
        bitval=random.randint(4,5)
        max=(2 ** bitval) - 1
        b=0
        while(b==0):
            b=bin(random.randint(2 ** (bitval-1)+1,max-1))
        binary_string = b[2:]
        addans=bin(int(binary_string,2)+int(binary_string,2))
        mulans=bin(int(binary_string,2)*int(binary_string,2))
        self.questions['9a']='9. (B&O Ch.2.3) Assuming unsigned arithmetic using {0}-bit integers, what are the results (after truncation) of the following operations?<br />(Give your answer as a binary)<br/>a. {1} + {2} = ?'.format(bitval,binary_string,binary_string)
        if(bitval==4):self.answers['9a']=addans[-4:]
        else:self.answers['9a']=addans[-5:]
        self.questions['9b']='b. {0} * {1} = ?'.format(binary_string,binary_string)
        if(bitval==4):self.answers['9b']=mulans[-4:]
        else:self.answers['9b']=mulans[-5:]
     
        #Questions 10 a,b and c
        options={'-1 > 0U':'TRUE','0 == 0U':'TRUE','-1 < 0':'TRUE','-1 < 0U':'FALSE','2147483647 > -2147483647-1':'TRUE','2147483647U > -2147483647-1':'FALSE','2147483647 > (int)2147483648U':'TRUE','-1 > -2':'TRUE','(unsigned)-1 > -2':'TRUE','(unsigned)-2 > -9':'TRUE'}
        keylist=['-1 > 0U','0 == 0U','-1 < 0','-1 < 0U','2147483647 > -2147483647-1','2147483647U > -2147483647-1','2147483647 > (int)2147483648U','-1 > -2','(unsigned)-1 > -2','(unsigned)-2 > -9']
        random.shuffle(keylist)
        q1=keylist[0]
        q2=keylist[1]
        a1=options.get(q1)
        a2=options.get(q2)
        self.questions['10a']='10. (B&O Ch.2.2) For expressions that mix signed and unsigned numbers, C will cast the signed value to an unsigned one before evaluation. In C, list whether the following expressions are true or false.<br />a. {0}'.format(q1)
        self.answers['10a']=a1
        self.questions['10b']='b. {0}'.format(q2)
        self.answers['10b']=a2 

        #Questions 11a and b
        options=[7,18,28,30,23,55,63,48]
        random.shuffle(options)
        self.questions['11a']='11. (B&O Ch.2.3) Suppose we are given the task of generating code to multiply integer variable x by various different constant factor K. To be efficient we want to use only the operations +,- and <<. For the following values of K, write C expressions to perform the multiplication :<br />(Give your answer as an expression in brackets - eg. (x<<1)-(x>>1) - Do not use = )<br/>a. K = {0}'.format(options[0])
        self.answers['11a']=options[0]
        self.questions['11b']='b. K = {0}'.format(options[1])
        self.answers['11b']=options[1] 

        #Questions 12a and b
        options={'x == (int)(float) x;':'FALSE','x == (int)(double) x;':'TRUE','f == (float)(double) f;':'TRUE','d == (float) d;':'FALSE','f == -(-f);':'TRUE','2/3 == 2/3.0':'FALSE','d > f implies -f > -d':'TRUE','d * d >= 0.0':'TRUE','(d+f)-d == f;':'FALSE'}
        keylist=['x == (int)(float) x;','x == (int)(double) x;','f == (float)(double) f;','d == (float) d;','f == -(-f);','2/3 == 2/3.0','d > f implies -f > -d','d * d >= 0.0','(d+f)-d == f;']
        random.shuffle(keylist)
        q1=keylist[0]
        q2=keylist[1]
        a1=options.get(q1)
        a2=options.get(q2)
        self.questions['12a']='12. (B&O Ch.2.4) Assume variables x, f and d, are of type int, float and double, respectively. Their values are arbitrary, except that neither f nor d is infinite or NaN. For each of the following C expressions, state TRUE if it will always be true and FALSE if otherwise.<br/>a. {0}'.format(q1)
        self.answers['12a']=a1
        self.questions['12b']='b. {0}'.format(q2)
        self.answers['12b']=a2

        #Questions 13a,b,c and d
        totalbits=[7,8]
        random.shuffle(totalbits)
        tbits=totalbits[0]
        if (tbits==7):
            expFrac={'3':'3','4':'2','2':'4'}
            expList=['2','3','4']
            random.shuffle(expList)
            exp=int(expList[0])
            frac=int(expFrac.get(expList[0]))
           
        if (tbits==8):
            expFrac={'2':'5','3':'4','4':'3','5':'2'}
            expList=['2','3','4','5']
            random.shuffle(expList)
            exp=int(expList[0])
            frac=int(expFrac.get(expList[0]))
        e=exp
        f=frac
        expStr=''
        fracStr=''
        ans1=ans2=ans3=ans4='0'
        while(exp>0):
            expStr=expStr+'e'+'{0}'.format(exp-1)+' '
            ans1=ans1+'0'
            ans2=ans2+'0'
            ans3=ans3+'0'
            ans4=ans4+'1'
            exp=exp-1
        ans3=ans3[:-1]+'1'
        ans4=ans4[:-1]+'0'
        while(frac>0):
            fracStr=fracStr+'f'+'{0}'.format(frac-1)+' '
            ans1=ans1+'0'
            ans2=ans2+'1'
            ans3=ans3+'0'
            ans4=ans4+'1'
            frac=frac-1 
        ans1=ans1[:-1]+'1'

        self.questions['13a']='13. (B&O Ch.2.4) Consider an IEEE-based floating point format below with 1 sign bit, {0} exponent bits, and {1} fraction bits.<br/>+---+--------------+-----------+<br/>| s | {2}| {3}|<br/>+---+--------------+-----------+<br/>a. Give the bit-representation of the smallest, non-zero positive denormalized number.'.format(e,f,expStr,fracStr)
        self.answers['13a']=ans1
        self.questions['13b']='b. Give the bit representation of the largest, positive denormalized number.'
        self.answers['13b']=ans2
        self.questions['13c']='c. Give the bit representation of the smallest, positive normalized number.'
        self.answers['13c']=ans3
        self.questions['13d']='d. Give the bit representation of the largest, non-infinite, positive normalized number.'
        self.answers['13d']=ans4

        #Questions 14a and b
        denom=[8,16]
        random.shuffle(denom)
        numerList=[3,5,7,9,11,13,15,17,19,21,23]
        random.shuffle(numerList)
        numer=numerList[0] 
        w='{0:b}'.format(numer//denom[0])
        m='{0:b}'.format(numer%denom[0])
        if(denom[0]==8):
            if(len(m)!=3):
                l=len(m)
                while(l<3):
                    m='0'+m
                    l=l+1
        if(denom[0]==16):
            if(len(m)!=4):
                l=len(m)
                while(l<4):
                    m='0'+m
                    l=l+1
        ans=w+'.'+m

        first=[2,3]
        random.shuffle(first)
        if(first[0]==2):num='10'
        else:num='11'
        decimalDict={'3':'0011','5':'0101','7':'0111','9':'1001','11':'1011','13':'1101','15':'1111'}
        second=random.randint(3,15)
        if(second%2==0):second=second+1
        num=num+'.'+decimalDict.get(str(second))
        self.questions['14a']='14. (B&O Ch.2.4) <br/>a. Write the following fraction as a binary number using a binary point {0}/{1}.'.format(numer,denom[0])
        self.answers['14a']=ans
        self.questions['14b']='b. Write the fractional value of the following binary number : {0}<br/>[Give your answer as a whole number followed by space and then fraction (eg. 1 2/3)].'.format(num)
        self.answers['14b']=str(first[0])+' '+str(second)+'/16'
       
        #Questions 15a through f
        self.questions['15a']='15. (B&O Ch.2.4) Consider an IEEE-based floating point format below with one sign bit, four exponent bits, and two fraction bits. The exponent has a Bias of 7. Recall, an exponent of all 0s denotes a denormalized number while an exponent of all 1s denotes infinite/NaN values.<br/>+---+-----------------+-------+<br/>| s | e3 e2 e1 e0 | f1 f0 |<br/>+---+-----------------+-------+<br/>a. What is the value of the smallest, non-zero, positive number in this format, given as a fraction?'
        self.answers['15a']='1/256'
        self.questions['15b']='b. What is the value of the largest, non-infinite, positive number in this format, given as a decimal?'
        self.answers['15b']='224'
        self.questions['15c']='c. In this format, calculate the value of the following bit representation:  0 0000 10'
        self.answers['15c']='1/128'
        self.questions['15d']='d. In this format, calculate the value of the following bit representation:  0 1010 11'
        self.answers['15d']='14'
 

	#Store the Questions and answers in database
        conn=sqlite3.connect('../db/{0}.db'.format(username))
        id=1
        for qkey,question in self.questions.items():
            conn.execute("INSERT INTO QUESTIONBANK (NUMBER,CHAPTER,QUESTION,STATUS,SCOREID) VALUES('{0}',2,'{1}','UNSOLVED',{2})".format(qkey,question,id))
            id=id+1
        for akey,answer in self.answers.items():
            conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' WHERE CHAPTER=2 AND NUMBER='{1}'".format(answer,akey))
        for akey,hint in self.hints.items():
            conn.execute("UPDATE QUESTIONBANK SET HINT='{0}' WHERE CHAPTER=2 AND NUMBER='{1}'".format(hint,akey))
        conn.commit()
        conn.close()
        
        return self.questions

