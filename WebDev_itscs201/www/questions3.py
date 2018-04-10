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
    def genChap3(self,username):
        self.questions=OrderedDict()
        self.answers=OrderedDict()

        #Generating questions for chapter 3
        #Question 1a through d
        options=['0x100','0x104','0x108','0x110','0x118','0x10C']
        random.shuffle(options)
        ques1=ans1=ques2=options[0]
        optDict={'0x100':'0x89','0x104':'0x78','0x108':'0xAB','0x110':'0xCD','0x118':'0xEF','0x10C':'0x11'}
        ans2=optDict.get(ques2)
        ques3Opt={'(%rax)':'0xAB','(%rbx)':'0x78'}
        q3opt=['(%rax)','(%rbx)']
        random.shuffle(q3opt)
        ques3=q3opt[0]
        ans3=ques3Opt.get(ques3)
        ques4Opt={'4(%rax)':'0x11','-8(%rax)':'0x89','4(%rbx)':'0xAB','-4(%rbx)':'0x89'}
        q4opt=['4(%rax)','-8(%rax)','4(%rbx)','-4(%rbx)']
        random.shuffle(q4opt)
        ques4=q4opt[0]
        ans4=ques4Opt.get(ques4)
        ques5Opt={'(%rax,%rdx,2)':'0x11','(%rbx,%rdx,4)':'0x11','(%rbx,%rdx,2)':'0xAB','(%rax,%rdx,8)':'0xEF'}
        q5opt=['(%rax,%rdx,2)','(%rbx,%rdx,4)','(%rbx,%rdx,2)','(%rax,%rdx,8)']
        random.shuffle(q5opt)
        ques5=q5opt[0]
        ans5=ques5Opt.get(ques5)
        ques6Opt={'0x110':'What value is in %rcx after this instruction: leaq 4(%rax,%rdx,2),%rcx','0x24':'If the value in the %rcx register is 8, then what is the hexadecimal value in %rax after this instruction: leaq 4(,%rcx,4),%rax'}
        q6opt=['0x110','0x24']
        random.shuffle(q6opt)
        ans6=q6opt[0]
        ques6=ques6Opt.get(ans6)

        self.questions['1a']='1. (B&O Chapter 3.4) Assuming an x86-64 CPU, Consider the following values stored at the indicated memory addresses and registers:<br/>&emsp;Address&emsp;|&emsp;Value&emsp;&emsp;&emsp;&emsp;Register&emsp;|&emsp;Value<br/>-------------------------------&emsp;&emsp;&emsp;&nbsp;&nbsp;-----------------------------<br/>&emsp;0x100&nbsp;&emsp;&nbsp;&nbsp;|&emsp;0x89&emsp;&emsp;&emsp;&emsp;&emsp;%rax&emsp;&emsp;|&emsp;0x108<br/>&emsp;0x104&nbsp;&emsp;&nbsp;&nbsp;|&emsp;0x78&emsp;&emsp;&emsp;&emsp;&emsp;%rbx&emsp;&emsp;|&emsp;0x104<br/>&emsp;0x108&nbsp;&emsp;&nbsp;&nbsp;|&emsp;0xAB&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;%rdx&emsp;&emsp;|&emsp;0x2<br/>&emsp;0x10C&emsp;&nbsp;&nbsp;|&emsp;0x11<br/>&emsp;0x110&nbsp;&emsp;&nbsp;&nbsp;|&emsp;0xCD<br/>&emsp;0x118&nbsp;&emsp;&nbsp;&nbsp;|&emsp;0xEF<br/>What are the values for the following source operands when used with a movq instruction? (i.e. What does %rcx contain after executing movq S, %rcx when S is each of the operands below?<br/>[Provide your answers as a hexadecimal eg. 0xFF]<br/>a. ${0}'.format(ques1)
        self.answers['1a']=ans1
        self.questions['1b']='b. {0}'.format(ques2)
        self.answers['1b']=ans2
        self.questions['1c']='c. {0}'.format(ques3)
        self.answers['1c']=ans3
        self.questions['1d']='d. {0}'.format(ques4)
        self.answers['1d']=ans4
        self.questions['1e']='e. {0}'.format(ques5)
        self.answers['1e']=ans5
        self.questions['1f']='f. {0}'.format(ques6)
        self.answers['1f']=ans6

        #Question 2
        optionsDict={'mov__&emsp;%eax,(%rsp)':'l','mov__&emsp;(%rax),%dx':'w','mov__&emsp;$0xFF,%bl':'b','mov__&emsp;(%rsp,%rdx,4),%dl':'b','mov__&emsp;(%rdx),%rax':'q','mov__&emsp;%dx,(%rax)':'w'}
        options=['mov__&emsp;%eax,(%rsp)','mov__&emsp;(%rax),%dx','mov__&emsp;$0xFF,%bl','mov__&emsp;(%rsp,%rdx,4),%dl','mov__&emsp;(%rdx),%rax','mov__&emsp;%dx,(%rax)']
        random.shuffle(options)
        ques1=options[0]
        ans1=optionsDict.get(ques1)
        ques2=options[1]
        ans2=optionsDict.get(ques2)

        self.questions['2a']='2. (B&O Chapter 3.4) Assuming an x86-64 CPU, for each of the following lines of assembly language, determine the appropriate instruction suffix based on the operands. (For example, mov can be written as movb, movw, movl, or movq)<br/>a. {0}'.format(ques1)
        self.answers['2a']=ans1
        self.questions['2b']='b. {0}'.format(ques2)
        self.answers['2b']=ans2

        #Question 3
        self.questions['3a']='3. (B&O Chapter 3.4) Assuming an x86-64 CPU, Consider the following assembly routine :<br/>&emsp;&emsp;dx:<br/>&emsp;&emsp;&emsp;&emsp;movq %rdx, %rax<br/>&emsp;&emsp;&emsp;&emsp;subq %rsi, %rax<br/>&emsp;&emsp;&emsp;&emsp;movq %rax, (%rdi)<br/>&emsp;&emsp;&emsp;&emsp;retq<br/>Fill in the missing lines of the following C function.<br/>&emsp;&emsp;long dx(long *xp,long y,long z){<br/>&emsp;&emsp;&emsp;&emsp;long result = _______;<br/>&emsp;&emsp;&emsp;&emsp;_______= result;<br/>&emsp;&emsp;&emsp;&emsp;return _______;<br/>&emsp;&emsp;}<br/><br/>a.  long result = _______;'
        self.answers['3a']='z-y'
        self.questions['3b']='b.  _______= result;'
        self.answers['3b']='*xp'
        self.questions['3c']='c.  return _______;'
        self.answers['3c']='result'

        #Question 4
        self.questions['4a']='4.a. (B&O Chapter 3.4) Assuming an x86-64 CPU, Consider the following assembly routine:<br/>&emsp;&emsp;fx:<br/>&emsp;&emsp;&emsp;&emsp;movq %rdi, %rax<br/>&emsp;&emsp;&emsp;&emsp;imulq %rsi, %rax<br/>&emsp;&emsp;&emsp;&emsp;addq $5, %rax<br/>&emsp;&emsp;&emsp;&emsp;retq<br/>Fill in the corresponding C function. Only one statement is required.<br/>&emsp;&emsp;long fx(long x, long y){<br/>&emsp;&emsp;&emsp;&emsp;__________<br/>&emsp;&emsp;}<br/>'
        self.answers['4a']='return x*y+5;'
       
        #Question 5
        optDict={'leaq -8(%rax), %rdx':'x-8','leaq (%rax, %rcx, 4), %rdx':'x+4y','leaq 4(%rax, %rcx, 2), %rdx':'x+2y+4','leaq 0xA(, %rcx,2),%rdx':'2y+10','leaq 0xC(,%rcx,4), %rdx':'4y+12','leaq 8(%rax),%rdx':'x+8','leaq 8(%rax, %rcx,4), %rdx':'x+4y+8'}
        options=['leaq -8(%rax), %rdx','leaq (%rax, %rcx, 4), %rdx','leaq 4(%rax, %rcx, 2), %rdx','leaq 0xA(, %rcx,2),%rdx','leaq 0xC(,%rcx,4), %rdx','leaq 8(%rax),%rdx','leaq 8(%rax, %rcx,4), %rdx']
        random.shuffle(options)
        ques1=options[0]
        ans1=optDict.get(ques1)
        ques2=options[1]
        ans2=optDict.get(ques2)

        self.questions['5a']='5. (B&O Chapter 3.5) Assuming an x86-64 CPU, Suppose %rax contains x and %rcx contains y at the beginning of each instruction below. What would %rdx contain after each instruction is executed?<br/>a. {0}'.format(ques1)
        self.answers['5a']=ans1
        self.questions['5b']='b. {0}'.format(ques2)
        self.answers['5b']=ans2

        #Question 6
        optDict={'short S[15]':'movw','int S[15]':'movl','double *W[4]':'movq','short *W[4]':'movq','int *W[4]':'movq'}
        optS=['short S[15]','int S[15]']
        optW=['double *W[4]','short *W[4]','int *W[4]']
        random.shuffle(optS)
        random.shuffle(optW)
        opt1=optS[0]
        opt2=optW[0]
        optValue1=optDict.get(opt1)
        optValue2=optDict.get(opt2)
        if (opt1 == 'short S[15]'):
            ans1='30'
            temp='2'
            reg='%ax'
        else: 
            ans1='60'
            temp='4'
            reg='%eax'
            
  
        self.questions['6a']='6. (B&O Chapter 3.8) Assuming an x86-64 CPU, Consider the following declaration :<br/>&emsp;&emsp;{0};<br/>&emsp;&emsp;{1};<br/>a. What is the total size of the array S in bytes?'.format(opt1,opt2)
        self.answers['6a']=ans1
        self.questions['6b']='b. Assuming the address of S is stored in %rbx and i is stored in %rdx, write a single {0} instruction using the scaled index memory mode that loads S[i] into the low word of %rax.'.format(optValue1)
        self.answers['6b']=optValue1+' (%rbx,%rdx,'+temp+'),'+reg
        self.questions['6c']='c. What is the total size of the array W in bytes?'
        self.answers['6c']='32'
        self.questions['6d']='d. Assuming the address of W is stored in %rbx and i is stored in %rdx, write a single {0} instruction using the scaled index memory mode that loads W[i] into %rax.'.format(optValue2)
        self.answers['6d']=optValue2+' (%rbx,%rdx,8),%rax'

        #Question 7
        optDict={'5,7':'&emsp;&emsp;leaq 0(,%rdi,8), %rdx<br/>&emsp;&emsp;subq %rdi, %rdx<br/>&emsp;&emsp;addq %rsi, %rdx<br/>&emsp;&emsp;leaq (%rsi,%rsi,4), %rax<br/>&emsp;&emsp;addq %rax, %rdi<br/>&emsp;&emsp;movq Q(,%rdi,8), %rax<br/>&emsp;&emsp;addq P(,%rdx,8), %rax<br/>&emsp;&emsp;ret','3,9':'&emsp;&emsp;leaq (%rdi, %rdi,8), %rdx<br/>&emsp;&emsp;addq %rsi, %rdx<br/>&emsp;&emsp;leaq (%rsi,%rsi,2), %rax<br/>&emsp;&emsp;addq %rax, %rdi<br/>&emsp;&emsp;movq Q(,%rdi,8), %rax<br/>&emsp;&emsp;addq P(,%rdx,8), %rax<br/>&emsp;&emsp;ret','3,7':'&emsp;&emsp;leaq 0(,%rdi,8), %rdx<br/>&emsp;&emsp;subq %rdi, %rdx<br/>&emsp;&emsp;addq %rsi, %rdx<br/>&emsp;&emsp;leaq (%rsi,%rsi,2), %rax<br/>&emsp;&emsp;addq %rax, %rdi<br/>&emsp;&emsp;movq Q(,%rdi,8), %rax<br/>&emsp;&emsp;addq P(,%rdx,8), %rax<br/>&emsp;&emsp;ret','5,9':'&emsp;&emsp;leaq (%rdi, %rdi,8), %rdx<br/>&emsp;&emsp;addq %rsi, %rdx<br/>&emsp;&emsp;leaq (%rsi,%rsi,4), %rax<br/>&emsp;&emsp;addq %rax, %rdi<br/>&emsp;&emsp;movq Q(,%rdi,8), %rax<br/>&emsp;&emsp;addq P(,%rdx,8), %rax<br/>&emsp;&emsp;ret'}
        ansOpt=['5,7','3,9','3,7','5,9']
        random.shuffle(ansOpt)
        ans=ansOpt[0]
        ques1=optDict.get(ans)
        ans1=ans[:1]
        ans2=ans[-1:]
        self.questions['7a']='7. (B&O Chapter 3.8) Assuming an x86-64 CPU, Consider the following source code, where M and N are constants declared with #define:<br/>long P[M][N];<br/>long Q[N][M];<br/><br/>long sum_element(long i, long j)&#123;<br/>&emsp;&emsp;return P[i][j] + Q[j][i];<br/>&#125;<br/>In compiling this program, GCC generates the following assembly code:<br/>sum_element:<br/>{0}<br/>Use your reverse engineering skills to determine the values of M and N.<br/>a. M = ?'.format(ques1)
        self.answers['7a']=ans1
        self.questions['7b']='b. N = ?'
        self.answers['7b']=ans2

        #Questions 8a through h
        questeOpts={'s.c':'1','s.d':'8','s.i':'4'}
        questOpts=['s.c','s.d','s.i']
        random.shuffle(questOpts)
        queste=questOpts[0]
        questg=str(random.randint(1,4))
        ansgOpts={'1':'0x128','2':'0x140','3':'0x158','4':'0x170'}
        ansg=ansgOpts.get(questg)
        anshOpts={'1':'0x208','2':'0x210','3':'0x218','4':'0x220'}
        ansh=anshOpts.get(questg)
        
        self.questions['8a']='8. (B&O Chapter 3.9) Assuming an x86-64 CPU, Consider the following declarations:<br/>&emsp;&emsp;typedef struct&nbsp;&nbsp;&#123;<br/>&emsp;&emsp;&emsp;int i;<br/>&emsp;&emsp;&emsp;double d;<br/>&emsp;&emsp;&emsp;char c;<br/>&emsp;&emsp;&#125;&nbsp;&nbsp;s_t;<br/><br/>&emsp;&emsp;typedef union&nbsp;&nbsp;&#123;<br/>&emsp;&emsp;&emsp;int i;<br/>&emsp;&emsp;&emsp;double d;<br/>&emsp;&emsp;&emsp;char c;<br/>&emsp;&emsp;&#125;&nbsp;&nbsp;u_t;<br/><br/>&emsp;&emsp;s_t&emsp;s,&emsp;*sp,&emsp;sa[5];<br/>&emsp;&emsp;u_t&emsp;u,&emsp;*up,&emsp;ua[5];<br/>What are the size (in bytes) of the following variables?<br/>a. s'
        self.answers['8a']='24'
        self.questions['8b']='b. sp'
        self.answers['8b']='8'
        self.questions['8c']='c. u'
        self.answers['8c']='8'
        self.questions['8d']='d. up'
        self.answers['8d']='8'
        self.questions['8e']='e. {0}'.format(queste)
        self.answers['8e']=questeOpts.get(queste)
        self.questions['8f']='f. &{0}'.format(queste)
        self.answers['8f']='8'
        self.questions['8g']='g. Suppose the address of sa is 0x100. What is the address in hex of &sa[{0}].c'.format(questg)
        self.answers['8g']=ansg
        self.questions['8h']='h. Suppose the address of ua is 0x200. What is the address in hex of &ua[{0}].c'.format(questg)
        self.answers['8h']=ansh

        #Question 9
        Opts={'struct P1 &#123; short i; int c; int *j; short *d; &#125;;':'24','struct P2 &#123; int i[2]; char c[8]; short s[4]; long *j; &#125;;':'32','struct P3 &#123; long w[2]; int *c[2]; &#125;;':'32','struct P4 &#123; char w[16]; char *c[2]; &#125;;':'32','struct P5 &#123; long l; char c; int i; char d; &#125;;':'24','struct P6 &#123; float f; char c; char d; long l; &#125;;':'16','struct P7 &#123; short w[3]; int *c[3]; &#125;;':'32'}
        quesOpt=['struct P1 &#123; short i; int c; int *j; short *d; &#125;;','struct P2 &#123; int i[2]; char c[8]; short s[4]; long *j; &#125;;','struct P3 &#123; long w[2]; int *c[2]; &#125;;','struct P4 &#123; char w[16]; char *c[2]; &#125;;','struct P5 &#123; long l; char c; int i; char d; &#125;;','struct P6 &#123; float f; char c; char d; long l; &#125;;','struct P7 &#123; short w[3]; int *c[3]; &#125;;']
        random.shuffle(quesOpt)
        ques1=quesOpt[0]
        ques2=quesOpt[1]
        ans1=Opts.get(ques1)
        ans2=Opts.get(ques2)
      
        self.questions['9a']='9. (B&O Chapter 3.9) Assuming an x86-64 CPU, Consider the following structure definitions on an x86-64 machine. Determine the total size(in bytes) of each structure.<br/>a. {0}'.format(ques1)
        self.answers['9a']=ans1
        self.questions['9b']='b. {0}'.format(ques2)
        self.answers['9b']=ans2

        #Question 10
        opt1='&emsp;&emsp;struct rec&#123;<br/>&emsp;&emsp;&emsp;short a;<br/>&emsp;&emsp;&emsp;char *b;<br/>&emsp;&emsp;&emsp;double c;<br/>&emsp;&emsp;&emsp;char d;<br/>&emsp;&emsp;&emsp;int e;<br/>&emsp;&emsp;&#125;;<br/>---------------------------------------------------------------------------<br/>A. char *b; double c; int e; short a; char d;<br/>B. char d; short a;double c; char *b; int e;<br/>C. int e; short a; char d; char *b; double c;<br/>D. double d; int e; char *b; short a; char d;'
        opt2='&emsp;&emsp;struct rec&#123;<br/>&emsp;&emsp;&emsp;int *a;<br/>&emsp;&emsp;&emsp;float b;<br/>&emsp;&emsp;&emsp;char c;<br/>&emsp;&emsp;&emsp;short d;<br/>&emsp;&emsp;&emsp;long e;<br/>&emsp;&emsp;&emsp;double f;<br/>&emsp;&emsp;&emsp;int g;<br/>&emsp;&emsp;&emsp;char *h;<br/>&emsp;&emsp;&#125;;<br/>-------------------------------------------------------------------------------------<br/>A. char *h; int g; double f; long e; short d; char c; float b; int *a;<br/>B. int g; short d; long e; float b; int *a; double f; char *h; char c;<br/>C. int *a; char *h; double f; long e; float b; int g; short d; char c;<br/>D. char c; short d; int g; float b; long e; double f; char *h; int *a;'
        optDict={opt1:'A',opt2:'C'}
        opts=[opt1,opt2]
        random.shuffle(opts)
        ques1=opts[0]
        self.questions['10a']='10. (B&O Chapter 3.8,3.9) Assuming an x86-64 CPU, Reorganize the structure given below in order to minimize its size.<br/>[Choose your answer from options given - A/B/C/D]<br/>{0}'.format(ques1)
        self.answers['10a']=optDict.get(ques1)

        #Question 11
        asm1='int myasm(int x, int y){<br/>&emsp;&emsp;int result;<br/>&emsp;&emsp;asm("sall $2,%1; addl %1,%2; movl %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;int k;<br/>&emsp;&emsp;k = myasm(5,4);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asm2='int myasm(int x, int y){<br/>&emsp;&emsp;int result;<br/>&emsp;&emsp;asm("sall $2,%1; addl %1,%2; movl %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;int k;<br/>&emsp;&emsp;k = myasm(6,6);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asm3='int myasm(int x, int y){<br/>&emsp;&emsp;int result;<br/>&emsp;&emsp;asm("sall $2,%1; addl %1,%2; movl %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;int k;<br/>&emsp;&emsp;k = myasm(7,5);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asmDict1={asm1:'24',asm2:'30',asm3:'33'}
        asmopts1=[asm1,asm2,asm3]
        random.shuffle(asmopts1)
        q1=asmopts1[0]
        ans1=asmDict1.get(q1)

        asm4='long myasm(long x, long y){<br/>&emsp;&emsp;long result;<br/>&emsp;&emsp;asm("imulq %1,%2; xorq $15,%2; movq %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;long k;<br/>&emsp;&emsp;k = myasm(8,3);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asm5='long myasm(long x, long y){<br/>&emsp;&emsp;long result;<br/>&emsp;&emsp;asm("imulq %1,%2; xorq $15,%2; movq %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;long k;<br/>&emsp;&emsp;k = myasm(7,4);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asm6='long myasm(long x, long y){<br/>&emsp;&emsp;long result;<br/>&emsp;&emsp;asm("imulq %1,%2; xorq $15,%2; movq %2,%0"<br/>&emsp;&emsp;&emsp;: "=r" (result)<br/>&emsp;&emsp;&emsp;: "r" (x), "r" (y)<br/>&emsp;&emsp;);<br/>&emsp;&emsp;return result;<br/>}<br/>main(){<br/>&emsp;&emsp;long k;<br/>&emsp;&emsp;k = myasm(6,4);<br/>&emsp;&emsp;printf("%d",k);<br/>}'
        asmDict2={asm4:'23',asm5:'19',asm6:'23'}
        asmopts2=[asm4,asm5,asm6]
        random.shuffle(asmopts2)
        q2=asmopts2[0]
        ans2=asmDict2.get(q2)

        self.questions['11a']='11.a. (B&O Chapter 3.10) Assuming an x86-64 CPU, Consider the following code using embedded assembly :<br/>{0}<br/>What is the output of the printf statement?'.format(q1)
        self.answers['11a']=ans1
        self.questions['11b']='b. Consider the following code using embedded assembly :<br/>{0}<br/>What is the output of the printf statement?'.format(q2)
        self.answers['11b']=ans2

        #Question 12
        self.questions['12']='12. (B&O Chapter 3.6) Assuming an x86-64 CPU, Consider the following assembly routine that takes two input parameters x and y. Recall that the cmpq instruction (cmpq S1,S2) sets the condition flags by performing S2-S1.<br/>&emsp;&emsp;forloop:<br/>&emsp;&emsp;&emsp;&emsp;xorq&emsp;%rax, %rax<br/>&emsp;&emsp;&emsp;&emsp;xorq&emsp;%rdx, %rdx<br/>&emsp;&emsp;&emsp;&emsp;addq&emsp;%rsi, %rdi<br/>&emsp;&emsp;&emsp;&emsp;jmp&emsp;.L2<br/>&emsp;&emsp;.L3:<br/>&emsp;&emsp;&emsp;&emsp;addq&emsp;%rdi, %rax<br/>&emsp;&emsp;&emsp;&emsp;addq&emsp;$1, %rdx<br/>&emsp;&emsp;.L2:<br/>&emsp;&emsp;&emsp;&emsp;cmpq&emsp;$31, %rdx<br/>&emsp;&emsp;&emsp;&emsp;jl&emsp;.L3<br/>&emsp;&emsp;&emsp;&emsp;ret<br/>Fill in the missing statement in the C code below that was used to generate this assembly code. Do not use local variables.<br/>long forloop(long a, long b)<br/>&emsp;long i;<br/>&emsp;long result = 0;<br/>&emsp;for(i=0;i<31;i++)&#123;<br/>&emsp;&emsp;_______________________________;<br/>&emsp;return result;<br/>&#125;'
        self.answers['12']='result=result+a+b'

        #Question 13
        self.questions['13a']='13. (B&O Chapter 3.5) Assuming an x86-64 CPU, consider the assembly code implementation of a C function:<br/>&emsp;arith:<br/>&emsp;&emsp;subq&emsp;%rdx, %rdi&emsp;&emsp;&emsp;&emsp;;t1<br/>&emsp;&emsp;addq&emsp;%rdx, %rsi&emsp;&emsp;&emsp;&emsp;;t2<br/>&emsp;&emsp;leaq&emsp;(%rsi,%rsi,4), %rax<br/>&emsp;&emsp;addq&emsp;%rax, %rax&emsp;&emsp;&emsp;&emsp;;t3<br/>&emsp;&emsp;addq&emsp;%rdi, %rax&emsp;&emsp;&emsp;&emsp;;t4<br/>&emsp;&emsp;retq<br/>The C it was generated from is listed below with the expressions that are calculated replaced by blanks. Based on the assembly code, fill in these blanks:<br/>&emsp;long arith(long x, long y, long z)&#123;<br/>&emsp;&emsp;long t1 = ________________;<br/>&emsp;&emsp;long t2 = ________________;<br/>&emsp;&emsp;long t3 = ________________;<br/>&emsp;&emsp;long t4 = ________________;<br/>&emsp;&emsp;return ________________;<br/>&emsp;&#125;<br/>a. long t1 = ________________;'
        self.answers['13a']='x-z'
        self.questions['13b']='long t2 = ________________;'
        self.answers['13b']='y+z'
        self.questions['13c']='long t3 = ________________;'
        self.answers['13c']='10*t2'
        self.questions['13d']='long t4 = ________________;'
        self.answers['13d']='t1+t3'
        self.questions['13e']='return ________________;'
        self.answers['13e']='t4'        

	
	#Store the Questions and answers in database
        conn=sqlite3.connect('../db/{0}.db'.format(username))
        id=1
        for qkey,question in self.questions.items():
            conn.execute("INSERT INTO QUESTIONBANK (NUMBER,CHAPTER,QUESTION,STATUS,SCOREID) VALUES('{0}',3,'{1}','UNSOLVED',{2})".format(qkey,question,id))
            id=id+1
        for akey,answer in self.answers.items():
            conn.execute("UPDATE QUESTIONBANK SET ANSWER='{0}' WHERE CHAPTER=3 AND NUMBER='{1}'".format(answer,akey))
        conn.commit()
        conn.close()
        
        return self.questions

