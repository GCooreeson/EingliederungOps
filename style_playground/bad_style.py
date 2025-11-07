import os, sys  # multiple imports on one line
import re  # unused
from math import *  # wildcard import

CONSTANT=  42  # extra spaces around operator

def foo(x,y): print("bad spacing");   return x+y  # many statements on one line

def bad_name():
    l = 1  # ambiguous variable name
    x = None
    if x==None:  # comparison to None
        pass

def mixed_quotes():
    a = "double"; b='single'  # multiple statements on one line
    long = "x"*  3  # extra spaces
    try:
        eval("1+1")  # risky call (ruff will flag if S rules enabled)
    except:  # bare except
        print("oops")

def import_not_at_top():
    print(sys.version)
    import json  # import not at top

def long_line():
    s = "This is a very very very very very very very very very very very very very very long line that should trigger Black formatting to wrap it properly or at least make Ruff complain depending on your config"
