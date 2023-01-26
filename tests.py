from tables import *
from symbols import *
from data_loader import *
from globals import the as the


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
    # print("End of first for loop in rand_test_2()")
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


n = 0

def fun(t):
    global n
    n = n + len(t)


def csv_5():
    global n
    # n=fun(t)
    n = 0
    csv(the['file'], fun)
    # src_pointer.seek(0, os.SEEK_END)
    # file_length=src_pointer.tell()
    # print("file length as returned by file.tell is:",file_length)
    return n==8*399

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