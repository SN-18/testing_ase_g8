import sys
import math
# import tables
import data_loader

from functions import *
from settings import *
from tests import *
from tables import *
from symbols import *
from globals import the as the
from globals import help as help
# import symbols

import re
import os
# seed=[0]*1





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
    sys.exit(fails)












#Main
if __name__ == '__main__':

    eg('the', 'show settings', the_test_1, help)
    eg('rand', 'generate, reset, regenerate same', rand_test_2, help)
    eg('sym', 'check syms', sym_test_3, help)
    eg('num', 'check nums', num_test_4, help)
    eg('csv','read from csv',csv_5, help)
    eg('data','read data csv',data_6,help)
    eg("stats", "stats from data", stats_7,help)

    driver(the, help, egs)


