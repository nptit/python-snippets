from functools import wraps
import os
import pprint

def printdir(obj):
    dir_out = dir(obj)
    pprint.pprint(dir_out)


print dir(os)
print os.listdir('.')
cwd = os.getcwd()
print cwd
print dir(os.path)
