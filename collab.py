#24th Jan Tue
#8.45 pm complete monolithic

import sys
import math
import re
import os
# seed=[0]*1


the, help = {},\
'''   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = ./auto93.csv
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''

# class obj:
#     id = 0
#     t_the = {}
#
'''@classmethod'''
#     def update(cls):
#         cls.id = cls.id + 1
#
#     def __init__(self, s: str):
#         self.t_metatable = {}
#         self.t = {}
#         obj.update()
#         obj.add_child(self, s)
#
#     def add_child(self, s: str):
#         self.t[s] = obj.id


# Meta table class
# class table:
#     def __init__(self):
#         self.key = ""
#         self.value = -1
#         self.metatable = table()


# Symbol class inherited from global object class
# and it's related methods implemented inside of symbol
# sym = SYM("SYM")
class SYM():
    # has = {}
    def __init__(self,at,txt):
        # super.__init__(s)
        self.n = 0
        self.has={}
        self.most = 0
        self.mode = None
        self.at = at or 0
        self.txt = txt or ""

    # def obj_table():
    #     print(obj.t)

    def add(self, x: str):
        if x != "?":
            self.n = self.n + 1
            value = self.has.get(x, 0)
            self.has[x] = value + 1

            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        def fun(p):
            return p * (math.log(p, 2))

        # e_n is the negative entropy
        # n_cur is the current n, not the instance value self.n
        # n, here, represents frequency

        e_n = 0
        # print("I am printing self.has",self.has)

        for _,val in self.has.items():
            # print("I am printing tuples in self.has",element)
            # curr_val=self.has[element[1]]

            n_cur=val
            # print("I am printing n_cur, it should be an integer",n_cur)
            # print("I am printing has, it should contain")
            e_n = e_n + fun(n_cur / self.n)

        return (-1) * e_n

    def rnd(self, x, n=0):
        return x


# Num class inherited from global object class
# and it's related methods implemented inside of NUM class
class NUM():
    def __init__(self, at, txt):
        # super.__init__(s)
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = sys.maxsize
        self.hi = (-1) * sys.maxsize
        self.at = at if at else 0
        self.txt = txt if txt else ""
        self.w = -1 if txt.find('-') != -1 else 1

    # n_cur is the current n
    def add(self, n_cur):
        if n_cur != "?":
            try:
                n_cur=float(n_cur)
            except:
                n_cur=0

            self.n = self.n + 1
            d = n_cur - self.mu
            self.mu = self.mu + d / self.n
            self.m2 = self.m2 + d * (n_cur - self.mu)
            self.lo = min(n_cur, self.lo)
            self.hi = max(n_cur, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        var1 = self.m2 < 0 or self.n < 2
        var2 = 0
        var3 = ((self.m2) / (self.n - 1)) ** (0.5)
        return (var1 and var2) or var3

    def rnd(self, x, n):
        if x == '?':
            return x
        else:
            return round_n(x, n)

# seed = 937162211
#data


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

def csv(sFilename,fun,count=0):

    filename=open(sFilename)

    src=filename
    s=t=None
    t = dict()
    while True:
        s=src.readline()
        count=count+1


        # print(s)
        if s:

            # regex="([^,]+)"
            # mo=re.search(regex,s)
            # print("current mo is printed here",mo)

            # t=dict()
            for s1 in s.split(','):
                index=len(t)+1
                t[index]=coerce(s1)
            fun(t)
            # print(t)

        else:
            break


    # print(t)
    return t,count


            # src.close()





class DATA:
    index=0
    def __init__(self,src):
        self.rows=dict()
        self.cols=None
        #for the function called fun
        def fun(x):
            self.add(x)


        if type(src) is str:
            csv(src, fun)

        else:
            d=dict()
            map_co(src or d,fun)

    def add(self,t:dict):
        if self.cols:
            if isinstance(t,ROW):
                t=t.cells
            else:
                t=ROW(t)

            self.rows[DATA.index]=t
            DATA.index=DATA.index + 1
            # if COLS.index==t.len_row():
            #     COLS.index=0
            self.cols.add(t)
        else:
            self.cols=COLS(t)

    def clone(self, init_para=0):
        data=DATA({self.cols.names})
        d={}
        map_co(init_para or d,lambda x:data.add(x))
        return data

    def stats(self,what, cols, nPlaces):
        def fun(k,col):
            if what=="div":
                val=col.rnd(col.div(), nPlaces)

            elif what=="mid":
                val=col.rnd(col.mid(), nPlaces)

            return val,col.txt



        return kap_co(cols or self.cols.y,fun)






















#miscelleneous functions
def rand_intpy(lo, hi):
    return math.floor(0.5 + rand_fltpy(lo, hi))


def rand_fltpy(lo, hi, seed):
    # print("I am printing seed inside rand_flty",seed)
    lo, hi = lo or 0, hi or 1
    # print("I am printing seed and type of seed, should be a list",seed,type(seed))
    seed = (16807 * seed) % 2147483647
    return seed, lo + (hi - lo) * seed / 2147483647


def round_n(n, nPlaces=3):
    multiplier = 10 ** (nPlaces)
    return math.floor(n*multiplier+ 0.5)/multiplier
# List functions
# map collection
def map_co(t, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(v)
        u[k or (1 + len(u))] = v
    return u


def kap_co(t, fun):
    u = {}
    for k, v in t.items():
        v, k = fun(k, v)
        u[k or 1 + (1 + len(u))] = v
    return u


def sort_co(t, fun):
    dict(sorted(t.items(), fun))
    return t


def keys_co(t):
    return sorted(t.keys())


###Strings functions

# def oo(t:table):
#   print(o(t))


# def o(t:table, isKeys):
#   if type(t) != dict:
#     return str(t)
#   def fun(k, v):
#     temp = str(k)
#     if temp.find("^_") != -1:
#       return fmt()
#   return "{" +  "}"

def coerce(s):
    # inner function

    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        try:
            s_ret = int(s)
            return s_ret
        except ValueError:
            try:
                s_ret = float(s)
                return s_ret
            except ValueError:
                try:
                    regex = re.compile('(^\s*)(.+?)(\s*$)')
                    mo = regex.search(s)
                    return mo.group(2)
                except:
                    return s


import re


def settings(s):
    regex = "\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    mo = re.findall(regex, s)
    d = dict(mo)
    return d


def cli(options):
    args = sys.argv[1:]
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(args):
            if x == '-' + k[0] or x == '--' + k:
                if v == 'false':
                    v = 'true'
                elif v == 'true':
                    v = 'false'
                else:
                    v = args[n + 1]
            options[k] = coerce(v)
    return options








def driver(options, help, funs):
    # print("We have entered the driver code")
    saved, fails = {}, 0
    d=cli(settings(help))
    for key in d:
        val=d[key]
        options[key]=val

    # print("is options empty?\n")
    # print(options)
    saved = options
    # print("I am now printing options",options)
    if options['help'] is not False:
        # print("I am inside the if statement")
        print(help)
    else:
        # print("I am printing funs\n")
        # print(funs)
        # print("I am now printing fun.items",funs.items())

        for what, fun in funs.items():
            if options['go'] == 'all' or what == options['go']:
                for k, v in saved.items():
                    options[k] = v
                Seed = options['seed']
                if funs[what]() == False:
                    fails = fails + 1
                    print(str(u'\u274C') + " fail: " + str(what))

                else:
                    print(str(u'\u2705') + " pass: " + str(what))
    print("System didn't pass, raise generic exception")
    sys.exit(fails)










# Test cases
egs = {}


def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"


def the_test_1():
    print(the)
    # print(the.__repr__())


def rand_test_2():
    num1, num2 = NUM(0,""), NUM(8,"")

    # print("I'm printing 'the' dict now:\n")

    seed = the['seed']

    for i in range(1, 10 ** 3):
        seed, r = rand_fltpy(0, 1, seed)
        num1.add(r)
        # num1.add(rand_fltpy(0, 1,seed))
    print("End of first for loop in rand_test_2()")
    seed = the['seed']

    for i in range(1, 10 ** 3):
        seed, r = rand_fltpy(0,1,seed)
        num2.add(r)

    m1, m2 = round_n(num1.mid(), 10), round_n(num2.mid(), 10)

    print("m1 is :",m1)
    print("m2 is :",m2)


    return m1 == m2 and .5 == round_n(m1, 1)


def sym_test_3():
    sym = SYM(at=0,txt="")
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == round_n(sym.div())


def num_test_4():
    num = NUM(at=0,txt="")
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    return 11 / 7 == num.mid() and 0.787 == round_n(num.div())


# global n


def fun(t,n=0):
    # global n
    n = n + len(t)


def csv_5():
    # n=fun(t)
    loaded_table,count=csv(the['file'], fun)
    print("count wjo;e csv is,",count)
    # src_pointer.seek(0, os.SEEK_END)
    # file_length=src_pointer.tell()
    # print("file length as returned by file.tell is:",file_length)

    return len(loaded_table)==8*399

#
def data_6():
    data=DATA(the['file'])


    #print("this is the value of data.cols.x",data.cols.x)
    #for k,v in data.cols.x.items():
        #print("x.txt x.at ",v.txt,v.at)

    #print("Re?dundant: This is the value of w", data.cols.x[1].at)

    return len(data.rows)==398 and \
    data.cols.y[1].w == -1 and \
    data.cols.x[1].at==1 and \
    len(data.cols.x)==4

def stats_7():
    data = DATA(the['file'])
    d = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in d.items():
        print(k + "mid"+ str(data.stats("mid", cols, 2)))
        print(""+ "div" +str(data.stats("div", cols, 2)))
    # for k,cols in (data.cols.y,data.cols.x)




#Main
if __name__ == '__main__':

    eg('the', 'show settings', the_test_1, help)
    eg('rand', 'generate, reset, regenerate same', rand_test_2, help)
    eg('sym', 'check syms', sym_test_3, help)
    eg('num', 'check nums', num_test_4, help)
    eg('csv','read from csv',csv_5, help)
    eg('data','read data csv',data_6,help)
    eg("stats", "stats from data", stats_7,help)

    # eg()
#
    driver(the, help, egs)

    # def settings(s:str):
    #   t={}
    #   regex="\n[\s]+[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
    #   mo=re.findall(regex,s)
    #   d=dict(mo)

# scontrol="%s %s"
# actual string->unpack

# print("%s %s","a","b")
# sControl_modified="{" + sControl + "}"
# print("{sControl}"$).format
# print()


# NUM,SYM = obj("NUM"), obj("SYM")


