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

    def genChap5(self, username):
        self.questions = OrderedDict()
        self.answers = OrderedDict()    
        #Generating questions for chapter 5
        
        #opt1 is sharing common subexpressions
        opt1 = '<br/>int a = b * c + d;<br/>int f = b * c + e;<br/>---------------------<br/> int bc = b * c;<br/> int a = bc + d;<br/> int f = bc + e;'

        #opt2 is code motion
        opt2 = '<br/>void lower1(char *s){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;for (i = 0; i < strlen(s); ++i){<br/>&emsp;&emsp;&emsp;if (s[i] >= "A" && s[i] <= "Z")<br/>&emsp;&emsp;&emsp;&emsp;s[i] -= ("A" = "a");<br/>&emsp;&emsp;}<br/>}<br/>-----------------------------<br/>void lower1(char *s){<br/>&emsp;&emsp;long i; <br/>&emsp;&emsp;long len = strlen(s);<br/>&emsp;&emsp;for (i = 0; i < len; ++i)<br/>&emsp;&emsp;&emsp;if (s[i] >= "A" && s[i] <= "Z")<br/>&emsp;&emsp;&emsp;&emsp;s[i] -= ("A" = "a");<br/>&emsp;&emsp;}<br/>}<br/>'

        #opt3 is code motion
        opt3 = '<br/>void combine(vec_ptr v, data_t *dest){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;*dest = IDENT;<br/>&emsp;&emsp;for (i = 0; i < vec_length(v); ++i){<br/>&emsp;&emsp;&emsp;data_t val;<br/>&emsp;&emsp;&emsp;get_vec_element(v,i,&val);<br/>&emsp;&emsp;&emsp;*dest = *dest OP val;<br/>&emsp;&emsp;}<br/>}<br/>---------------------------<br/>void combine(vec_ptr v, data_t *dest){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;*dest = IDENT;<br/>&emsp;&emsp;long len = vec_length(v);<br/>&emsp;&emsp;for (i = 0; i < len; ++i){<br/>&emsp;&emsp;&emsp;data_t val;<br/>&emsp;&emsp;&emsp;get_vec_element(v,i,&val);<br/>&emsp;&emsp;&emsp;*dest = *dest OP val;<br/>&emsp;&emsp;}<br/>}<br/>'
       
        #opt4 is code motion and reduction in strength 
        opt4 = '<br/>void combine(vec_ptr v, int *dest){<br/>&emsp;&emsp;int i;<br/>&emsp;&emsp;*dest = 0;<br/>&emsp;&emsp;long len = vec_length(v);<br/>&emsp;&emsp;for (i = 0; i < len; ++i){<br/>&emsp;&emsp;&emsp;int val;<br/>&emsp;&emsp;&emsp;get_vec_element(v,i,&val);<br/>&emsp;&emsp;&emsp;*dest += val;<br/>&emsp;&emsp;}<br/>}<br/>---------------------------<br/>void combine(vec_ptr v, int *dest){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;*dest = 0;<br/>&emsp;&emsp;int len =vec_length(v);<br/>&emsp;&emsp;int *data = get_vec_start(v);<br/>&emsp;&emsp;for (i = 0; i < len; ++i){<br/>&emsp;&emsp;&emsp;*dest += data[i];<br/>&emsp;&emsp;}<br/>}<br/>'

        #opt5 is using registers 
        opt5 = '<br/>void combine(vec_ptr v, int *dest){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;long len = vec_length(v);<br/>&emsp;&emsp;data_t *data = get_vec_start(v);<br/>&emsp;&emsp; *dest = 0;<br/>&emsp;&emsp;for (i = 0; i < len; ++i){<br/>&emsp;&emsp;&emsp;*dest += data[i];<br/>&emsp;&emsp;}<br/>}<br/>----------------------------<br/>void combine(vec_ptr v, data_t *dest){<br/>&emsp;&emsp;long i;<br/>&emsp;&emsp;long len = vec_length(v);<br/>&emsp;&emsp;data_t *data = get_vec_start(v);<br/>&emsp;&emsp;sum = 0;<br/>&emsp;&emsp;for (i = 0; i < len; ++i){<br/>&emsp;&emsp;&emsp;sum += data[i];<br/>&emsp;&emsp;}<br/>&emsp;&emsp;*dest = sum; <br/>}<br/>'
        
       #code motion 
        opt6 = '<br/> int a[MAX]; int b[MAX];<br/>for (i = 0; i < N; ++i){<br/>&emsp;for (j = 0; j < N; ++j){<br/>&emsp;&emsp; a[n*i + j] = b[j];<br/>&emsp;}<br/>}<br/>-------------------------------<br/> int a[MAX]; int b[MAX];<br/>for (i = 0; i < N; ++i){<br/>&emsp; int ni = n*i;<br/>&emsp; for (j = 0; j < N; ++j){<br/>&emsp;&emsp; a[ni + j] = b[j];<br/>&emsp;{<br/>}<br/>'

        
        #kind1 = 'Is elimination of loop inefficiency an example of:<br/>A) code motion<br/>B) reduction in strength<br/>C) code motion and reduction in strength<br/>D) use of registers<br/>'
        #kind2 = 'Is reduction in procedure calls an example of:<br/>A) code motion<br/>B) reduction in strength<br/>C) code motion and reduction in strength<br/>D)use of registers<br/>'
        #kind3 ='Is elimination of memory references an example of:<br/>A) code motion<br/>B) reduction in strength<br/>C) code motion and reduction in strength<br/>D)use of registers'

        block1 = '<br/>Can the compiler safely make this optimization? Y or N <br/>for (i = 0; i < n; i++){<br/> &emsp;&emsp;a[0] += b[i];<br/> }<br/> ---------------------------<br/> int tmp = a[0];<br/> for (i = 0; i < n; i++){<br/> &emsp;&emsp;tmp += b[i];<br/> }<br/> a[0] = tmp;<br/>'

        block2 = '<br/>Can the compiler safely make this optimization? Y or N <br/>return sum() + sum()<br/> ---------------------------------<br/> return 2*sum()'

        block3 = '<br/>Can the programmer safely make this optimization? Y or N <br/> for(i = 0; i < strlen(num): i++)<br/>&emsp;&emsp;digits += num[i];<br/>----------------------------------<br/>length = strlen(num);<br/>for(i = 0; i < length; i++)<br/>&emsp;&emsp;digits += num[i];<br/>'
            
        unroll1 = '<br/> int sum = 0;<br/>for (i = 0; i < 100; i++)<br/>&emsp;&emsp;sum += a[i];<br/>--------------------------<br/>int sum = 0; <br/>for (i = 0; i < 100; i += 2){<br/>&emsp;&emsp;sum += a[i] + a[i+1];<br/>}' 
        unroll2 = '<br/>int sum1 = 0;<br/>int sum2 = 0;<br/>for (i = 0; i < length; i+=2){<br/>&emsp;&emsp; sum1 = sum1 + a[i];<br/>&emsp;&emsp; sum2 = sum2 + a[i+1];<br/>}<br/>&emsp;return sum1 + sum2;<br/>}'
        unroll3 = '<br/>int sum = 0;<br/>int sum1 = 0;<br/>int sum2 = 0;<br/>for (i = 0; i < length; i+=3){<br/>&emsp;&emsp; sum += a[i];<br/>&emsp;&emsp;sum1+= a[i+1];<br/>&emsp;&emsp;sum2+=a[i+2];<br/>}<br/>return sum + sum1 + sum2;<br/>}'
                    

        #branch1 = ' '
        #branch2 = ' '
        #branch3 = ' '

        opt_q = [opt1, opt2, opt3, opt4, opt5, opt6]
        opt_dict = {opt1:'D', opt2:'A', opt3:'A', opt4:'E', opt5:'C', opt6: 'A'}
        #kind_q = [kind1, kind2, kind3]
        #kind_dict = {kind1:'A', kind2:'C', kind3:'D'}
        block_q = [block1, block2, block3]
        block_dict = {block1:'N', block2:'N', block3:'Y'}
        unroll_q = [unroll1, unroll2, unroll3]
        unroll_dict = {unroll1:'2x1', unroll2:'2x2', unroll3:'3x3'}
        #branch_q = [branch1, branch2, branch3]
        #branch_dict = {branch1:"A", branch2:"B", branch3:"C"}

        random.shuffle(opt_q)
        #random.shuffle(kind_q)
        random.shuffle(block_q)
        random.shuffle(unroll_q)
        #random.shuffle(branch_q)
        
        self.questions['1a'] = '1a. (B&O 5.4-5.6)For the following questions (1a through 1c), compare both sets of code and identify the type of optimization used:<br/>A) Code motion <br/> B) Reduction in strength<br/> C) Using registers<br/> D) Sharing common subexpressions<br/> E) A and B<br/> F) None<br/>{0}'.format(opt_q[0]) 
        self.answers['1a'] ='{0}'.format(opt_dict.get(opt_q[0]))
        self.questions['1b'] = 'b.<br/>  {0}'.format(opt_q[1]) 
        self.answers['1b'] = '{0}'.format(opt_dict.get(opt_q[1]))
        self.questions['1c'] = 'c.<br/> {0}'.format(opt_q[2]) 
        self.answers['1c'] = '{0}'.format(opt_dict.get(opt_q[2]))
        #self.questions['2'] = '2.(B&O 5.4-5.6) {0}'.format(kind_q[0])
        #self.answers['2'] = '{0}'.format(kind_dict.get(kind_q[0]))
        #self.questions['3'] = '3. (B&O 5.4-5.6){0}'.format(kind_q[1])
        #self.answers['3'] = '{0}'.format(kind_dict.get(kind_q[1]))
        #self.questions['4'] = '4.(B&O 5.4-5.6) {0}'.format(kind_q[2])
        #self.answers['4'] = '{0}'.format(kind_dict.get(kind_q[2]))
        self.questions['2a'] = '2a.(B&O 5.1) {0}<br/>'.format(block_q[0])
        self.answers['2a'] = '{0}'.format(block_dict.get(block_q[0]))
        self.questions['2b'] = '2b. (B&O 5.1) {0}<br/>' .format(block_q[1])
        self.answers['2b'] = '{0}'.format(block_dict.get(block_q[1]))
        self.questions['3a'] = '3a.(B&O 5.8) What type of loop unrolling is this? Answer in AxB format. {0}<br/>'.format(unroll_q[0])
        self.answers['3a'] = '{0}'.format(unroll_dict.get(unroll_q[0]))
        self.questions['3b'] = '3b. (B&O 5.8) What type of loop unrolling is this? Answer in AxB format. {0}<br/>'.format(unroll_q[1])
        self.answers['3b'] = '{0}'.format(unroll_dict.get(unroll_q[1]))
        #self.questions['7a'] = '7a. something about branch prediction'.format(branch_q[0])
        #self.answers['7a'] = '{0}'.format(branch_dict.get(branch_q[0]))
        #self.questions['7b'] = '7b. something about branch prediction'.format(branch_q[1])
        #self.answers['7b'] = '{0}'.format(branch_dict.get(branch_q[1]))
        
	#Store the Questions and answers in database
        conn=sqlite3.connect('../db/{0}.db'.format(username))
        id=1
        for qkey,question in self.questions.items():
           conn.execute("INSERT INTO QUESTIONBANK (NUMBER,CHAPTER,QUESTION,STATUS,SCOREID) VALUES('{0}',5,'{1}','UNSOLVED',{2})".format(qkey,question,id))
           id=id+1
        for akey,answer in self.answers.items():
           conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' WHERE CHAPTER=5 AND NUMBER='{1}'".format(answer,akey))
        conn.commit()
        conn.close()
        
        return self.questions
