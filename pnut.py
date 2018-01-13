# coding: utf-8

import random
import datetime
import argparse


def read_para():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-offline", help=u' 离线形式的，非交互式的，一次出N个题目，自己慢慢做去吧',action="store_true")
    #parser.add_argument('-max', help=u'多少以内的加减法，默认20', type=int, default=20)
    #parser.add_argument('-num', type=int, default=10, help=u' 每次出多少道题目，默认10')
    parser.add_argument("-offline", help=u' offlin',action="store_true")
    parser.add_argument('-max', help=u'default=20', type=int, default=20)
    parser.add_argument('-num', type=int, default=10, help=u' dft=10')
    args = parser.parse_args()
    return args


def cal_add_2(max):
    num1=random.randint(0,max)
    num2=random.randint(0,max-num1)
    qstr="%s+%s" %(num1, num2)
    return qstr

def cal_sub_2(max):
    num1=random.randint(0,max)
    num2=random.randint(0,num1)
    qstr="%s-%s" %(num1, num2)
    return qstr

def cal_add_3(max):
    num1=random.randint(0,max)
    num2=random.randint(0,max-num1)
    num3=random.randint(0,max-num1-num2)
    qstr="%s+%s+%s" %(num1, num2, num3)
    return qstr
    
def cal_sub_3(max):
    num1=random.randint(0,max)
    num2=random.randint(0,num1)
    num3=random.randint(0,num1-num2)
    qstr="%s-%s-%s" %(num1, num2, num3)
    return qstr

def cal_addsub_3(max):
    num1=random.randint(0,max)
    qstr_tmp='num1'

    for i in range(2):
        r1=random.randint(0,10000)
        if(r1%2==0):
            opr1='+'
            rst_tm=eval(qstr_tmp)
            num_n=random.randint(0,max-rst_tm)
            qstr_tmp=qstr_tmp+opr1+'%s' %(num_n)
        else:
            opr1='-'
            rst_tm=eval(qstr_tmp)
            num_n=random.randint(0,rst_tm)
            qstr_tmp=qstr_tmp+opr1+'%s' %(num_n)

    qstr=qstr_tmp.replace('num1', '%s' %num1)
    return qstr  

def cal_online(num, max):
    f=[cal_add_2,cal_add_3,cal_sub_2,cal_sub_3,cal_addsub_3,cal_addsub_3]
    suc=0
    fail=0
    totaltime=0
    for i in range(num):
        r1=random.randint(0,10000)
        h=r1%6
        begine=datetime.datetime.now()
        qstr=f[h](max)
        strkey=raw_input(qstr+' = ')
        key=int(strkey)
        end=datetime.datetime.now()
        delta=end-begine
        totaltime+=delta.total_seconds()
        if(key==eval(qstr)):
            print (u'pnut回答正确，用了%s秒' %(delta.total_seconds()))
            suc+=1
        else:
            print(u'pnut你用了%s秒还搞错了，答案应该是%s，认真点啊！！' %(delta.total_seconds(), eval(qstr)))
    print(u'正确%s个，错误%s个，共用了%s秒' %(suc,fail,totaltime))

def cal_offline(num, max):
    f=[cal_add_2,cal_sub_2,cal_add_3,cal_sub_3,cal_addsub_3,cal_addsub_3]

    for i in range(num):
        r1=random.randint(0,10000)
        h=r1%2
        idx='%4d    ' %(i)
        qstr1=f[h](max)
        qstr2=f[h](max)
        qstr3=f[h](max)
        #print(idx+qstr+' = ')  
        print('%s%12s=    %12s= %12s=' %(idx,qstr1,qstr2,qstr3)) 
        if(i%10==9):
            print ' ' 

def jls():
    m=n=0
    for i in range(10):
        m=n+6000
        n=m*1.05
        print(u'第%3s年: 本+息=%s' %(i+1, n))
    for i in range(10):
        n=n*1.05
        print(u'第%3s年: 本+息=%s' %(i+11, n))

         

if __name__=='__main__':
    args=read_para()
    if args.offline:
        cal_offline(args.num, args.max)
    else:
        cal_online(args.num, args.max)
    #jls()
    
        