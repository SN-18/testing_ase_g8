from functions import *
import sys
import itertools
#NUM class

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
        # print(var1, var2, var3)
        return (var1 and var2) or var3

    def rnd(self, x, n):
        if x == '?':
            return x
        else:
            return round_n(x, n)




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

