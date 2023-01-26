the, help = {}, '''   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''
from tables import *
from symbols import *
from data_loader import *
from globals import the as the


egs = {}


# Test cases
def eg(key, string, fun, help):
    egs[key] = fun
    help = help + " -g " + str(key) + "\t" + str(string) + "\n"


def the_test_1():
    print(the)






def sym_test_3():
    sym = SYM(at=0,txt="")
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    return "a" == sym.mid() and 1.379 == round_n(sym.div())


def num_test_4():
    print("This is test for nums, test 4")
    num = NUM(at=0,txt="")
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
        print("num.d, num.mu, and num are", num.d, num.mu,num.n)
        # print("value of mid on adding a new number is",num.mid())
    return 11 / 7 == num.mid() and 0.787 == round_n(num.div())


# global n


def fun(t,n=0):
    # global n
    n = n + len(t)


def csv_5():
    loaded_table=csv(the['file'], fun)
    return len(loaded_table)==8*399

#
def data_6():
    data=DATA(the['file'])




    return len(data.rows)==398 and \
    data.cols.y[1].w == -1 and \
    data.cols.x[1].at==1 and \
    len(data.cols.x)==4

def stats_7():
    data = DATA(the['file'])
    print(data)
    # print("This is printing data.cols.x",data.cols.x)
    print(data.cols.x[5].count)
    print(data.cols.x)
    print("I'm inside the stats test and value of data.cols.y and data.cols.x is\n")
    print(data.cols.y)
    print(data.cols.x)
    d = {'y': data.cols.y, 'x': data.cols.x}
    for k, cols in d.items():
        print(k + 'mid'+ str(data.stats('mid', cols, 2)))
        print(''+ 'div' +str(data.stats('div', cols, 2)))
