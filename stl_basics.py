"""Brief tour of the standard library."""

import os
import shutil
import glob
import sys
import argparse
import re
import math
import random
import statistics
import urllib
import smtplib
import datetime
import zlib, gzip, tarfile, zipfile, bz2, lzma
import timeit, profile, pstats
import doctest
import unittest

dirc = os.getcwd()  # get current working directory
os.chdir('/')  # change current working directory
os.chdir(dirc)
os.system('mkdir today')  # run command mkdir today in system shell
dir(os)  # list of all module functions
help(os)  # manual page from os's docstrings

# shutil is a higher level interface for performing primitive OS fxns
print(dir(shutil))
help(shutil)

# glob makes file lists from directory wildcard searches
dir(glob)
help(glob)
py_files = glob.glob('*.py')
print(f"Python files in this directory: {name for name in py_files}")

# command line arguments are accessed using sys
dir(sys)
help(sys)
print(sys.argv)
sys.stderr.write('Warning')  # redirect error messages to stderr
# sys.exit() to terminate a script

# argparse module is a more sophisticated mechanism to process cmd args
help(argparse)
dir(argparse)

# string pattern matching using regular expressions
dir(re)
help(re)
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

'tea for too'.replace('too', 'two') # for simple expressions string methods do

# for floating point math
dir(math)
help(math)
math.cos(math.pi/4)
math.log(1024, 2)

# random module for random selections
dir(random)
help(random)
random.choice(['apple', 'banana', 'orange'])
random.sample(range(100), 10)
random.randrange(199)

# statistics module to do basic statistical operations
dir(statistics)
help(statistics)

# urllib and smtplib are used for internet and email access
dir(urllib)
help(urllib)
dir(smtplib)
help(smtplib)

# datetime module allows operations on dates and times
dir(datetime)
help(datetime)
now = datetime.date.today()
print(now)
print(now.strftime("%d-%m-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = datetime.date(2000, 8, 16)
age = now - birthday  # calendar arithmetic supported
print(age.days)

# data compression formats are supported by modules like zlib, gzip, bz2, lzma
# zipfile and tarfile
dir(zlib)
dir(gzip)
dir(bz2)
dir(lzma)
dir(zipfile)
dir(tarfile)
help(zlib)
help(gzip)
help(bz2)
help(lzma)
help(zipfile)
help(tarfile)
s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
print(len(t))
zlib.decompress(t)
zlib.crc32(s)

# performance measurement can be done using timeit module
dir(timeit)
help(timeit)
dir(profile)
help(profile)
dir(pstats)
help(pstats)
# comparing performance of tuple packing and unpacking vs swapping
timeit.Timer('t=a; a = b; b = t', 'a = 1; b = 2').timeit()
timeit.Timer('a,b = b,a', 'a = 1; b = 2').timeit()

# doctest enables quality control by validating tests embedded in a program's
# docstrings
dir(doctest)
help(doctest)

# unittest also does testing

dir(unittest)
help(unittest)

# check the Library Reference for more modules
