import re

from functions import *

import sys

import itertools

from symbols import NUM
from symbols import SYM

#row
class ROW:
    def __init__(self,t:dict):
        self.cells=t
        self.t=t
    def len_row(self):
        return len(self.t)

class COLS:
    index1=1
    index2=1
    index3 = 1

    def __init__(self,t:dict):
        self.names=t
        self.all=dict()
        # self.index=0
        self.x=dict()
        self.y=dict()
        self.klass=None

        # print("I am printing t inside of COLS", str(t))

        for n,s in t.items():
            # print("This is the value of n,s",n,s)
            # print("this is the type of n,s",type(n),type(s))

            regex="^[A-Z]+"
            mo=re.search(regex,s)
            push_obj=object

            if mo:
                new_num=NUM(n,s)
                push_obj=new_num
            else:
                new_sym=SYM(n,s)
                push_obj=new_sym



            self.all[COLS.index1]=push_obj
            COLS.index1= COLS.index1 + 1
            regex1="X$"
            mo1=re.search(regex1,s)
            col=push_obj
            if not mo1:
                regex2="!$"
                mo2=re.search(regex2,s)
                if mo2:
                    self.klass=col
                regex3="[!+-]$"
                mo3=re.search(regex3,s)
                if mo3:
                    self.y[COLS.index3]=col
                    COLS.index3 = COLS.index3 + 1

                else:
                    self.x[COLS.index2]=col
                    COLS.index2 = COLS.index2 + 1


    def add(self,row):
        li=list()
        for t in [self.x,self.y]:
            # print("This is t in for loop",t)

            for _,col in t.items():
                # print("this is col", col, "this is type of col", type(col))
                col.add(row.cells[col.at])
