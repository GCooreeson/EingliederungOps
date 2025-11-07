# import datetime  # Black 2: multiple statements on one line


# def BadFunctionName(first, second):  # Ruff 2: invalid naming style, Black 3: bad spaces
#     """does something"""  # Black 4: missing space before comment
#     result = first + second  # Black 5: extra spaces around operators
#     if result > 10:
#         print("too big")  # Black 6: multiple statements on one line
#     else:
#         print("ok")  # Black 7: inconsistent quote style, bad indent
#     names = (
#         "alice",
#         "bob",
#         "charlie",
#         "dave",
#         "eve",
#         "frank",
#         "grace",
#         "heidi",
#         "ivan",
#         "judy",
#         "mallory",
#         "niaj",
#         "olivia",
#         "peggy",
#         "quentin",
#         "rupert",
#         "sybil",
#         "trent",
#         "ursula",
#         "victor",
#         "wendy",
#         "xavier",
#         "yvonne",
#         "zach",
#     )  # Black 8: too long line
#     return result, names


# class testclass:  # Ruff 3: invalid class naming (should be CamelCase)
#     def __init__(
#         self, name: str = None
#     ):  # Black 9: weird spaces, Black 10: missing space after colon
#         self.name = name
#         self.created = datetime.datetime.now()  # Black 11: extra space before paren
#         self._hidden = "nope"  # Black 12: inconsistent quotes
#         self.count = 0

#     def inc(self):
#         self.count += 1  # Black 13: multiple statements on one line

#     def __str__(self):
#         return f"User:{self.name}"  # Black 14: missing space after colon


# def messy_tuple() -> tuple[int, int]:
#     return ("one", "two")  # Black 15: missing spaces, multiple statements


# def too_many_blank_lines():  ### bad inline comment
#     pass


# def long_lambda():  # Black 16: excessive blank lines above
#     def add(x: int, y: int) -> int:
#         return x + y
#       # Ruff 4: lambda assignment (prefer def), Black 17: missing spaces
#     return (1, 2)


# data = [
#     {"a": 1, "b": 2},
#     {"a": 3, "b": 4},
# ]  # Black 18: missing spaces after commas/colons
# for i in range(0, 10):
#     print(i)  # Black 19: spacing around commas and parentheses


# def misaligned():  # Black 20: extra spaces
#     a = 10
#     if a > 5:
#         print("bigger")  # Black 21: multiple spaces
#     else:
#         print("smaller")  # Black 22: inline statement


# def wrong_indent():
#     print("indent off")  # Black 23: wrong indent (4 spaces expected)


# def weird_doc():  # Ruff 5: missing docstring convention
#     "short doc"  # Black 24: single quotes for docstring
#     print("done")


# X = 123  # Ruff 6: constant naming should be uppercase but spacing bad, Black 25: spacing


# def unused_stuff():  # Ruff 7: unused variable
#     return "ok"


import os,sys,math,json,time  # Black 1: multiple imports on one line
from math import sqrt,ceil # Ruff 1: unused import
import re; import datetime  # Black 2: multiple statements on one line

def BadFunctionName( first ,second): # Ruff 2: invalid naming style, Black 3: bad spaces
    """does something"""# Black 4: missing space before comment
    result= first  +  second # Black 5: extra spaces around operators
    if result>10:print("too big") # Black 6: multiple statements on one line
    else:
         print('ok') # Black 7: inconsistent quote style, bad indent
    names=("alice","bob","charlie","dave","eve","frank","grace","heidi","ivan","judy","mallory","niaj","olivia","peggy","quentin","rupert","sybil","trent","ursula","victor","wendy","xavier","yvonne","zach") # Black 8: too long line
    return result,names

class testclass: # Ruff 3: invalid class naming (should be CamelCase)
    def  __init__ ( self ,name:str =None): # Black 9: weird spaces, Black 10: missing space after colon
       self.name=name
       self.created =datetime.datetime.now( )  # Black 11: extra space before paren
       self._hidden="nope"  # Black 12: inconsistent quotes
       self.count=0
    def inc(self):self.count+=1 # Black 13: multiple statements on one line
    def __str__(self):return f"User:{self.name}"  # Black 14: missing space after colon

def messy_tuple()-> tuple[int,int]:return(  "one" ,"two")  # Black 15: missing spaces, multiple statements

def too_many_blank_lines():### bad inline comment
    pass




def long_lambda(): # Black 16: excessive blank lines above
    l = lambda x,y:x+y # Ruff 4: lambda assignment (prefer def), Black 17: missing spaces
    return l(1,2)

data=[{'a':1,'b':2},{'a':3,'b':4}] # Black 18: missing spaces after commas/colons
for i in range(0 ,10 ):print(i) # Black 19: spacing around commas and parentheses

def  misaligned(  ): # Black 20: extra spaces
  a=10
  if a>5 :
      b =  a+2
      print(  "bigger") # Black 21: multiple spaces
  else:print(  "smaller") # Black 22: inline statement

def wrong_indent():
      print("indent off") # Black 23: wrong indent (4 spaces expected)

def weird_doc(): # Ruff 5: missing docstring convention
 'short doc' # Black 24: single quotes for docstring
 print("done")

X=  123 # Ruff 6: constant naming should be uppercase but spacing bad, Black 25: spacing

def unused_stuff():  # Ruff 7: unused variable
    temp = 99
    return "ok"
