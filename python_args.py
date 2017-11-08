#!/usr/bin/python

import argparse
import os
import sys
import re
from itertools import islice
from os.path import isfile, join, split, isdir

PERSONFILE = '/home/mspencer/data/autism/genotype/people/person.csv'

PROGRESS = True
DEBUG = False
DEBUGLONG = False

def main(mystring, myfile, mydir, mynewfile, myint, mypat, mydefault):
    if PROGRESS: print("mystring: {}\nmyfile: {}\nmydir: {}\nmynewfile: {}\nmyint: {}\nmypat: {}\nnmydefault: {}".format(mystring, myfile, mydir, mynewfile, myint, mypat, mydefault))
    if DEBUG: print("Showing debug statements")
    if PROGRESS: print("Tada!")

#########################################################
# Argument checking functions below
#########################################################
# These functions require the following packages:
import argparse
import sys
import re
from os.path import isfile, join, split, isdir

def arg_error(message, req=True, default=''):
    if req:
        print("ERROR - " + message)
        sys.exit(-1)
    else:
        if default: message += " Using default value {}".format(default)
        else: message += " No default set."
        print("WARNING - " + message)

# TODO: Add option for checking the type and converting string arg
#       to the appropriate type (e.g. int, float, etc)
def check_arg(arg, name, file=False, dir=False, newfile=False, pattern=r".*", req=True, default=''):
    value = arg
    if not arg: 
        arg_error("Argument *{}* not found.".format(name), req, default)
        value = default
    if file: 
        if not isfile(value): arg_error("*{}* not found at {}.".format(name, value))
    if dir: 
        if not isdir(value): arg_error("*{}* not found at {}.".format(name, value))
        if value[-1] != '/': value += '/'
    if newfile: 
        if not isdir(split(value)[0]): arg_error("Path to *{}* invalid: {}".format(name, value))
        if isfile(value): arg_error("*{}* already exists: {}".format(name, value))
    pattern = re.compile(pattern)
    if not re.match(pattern, value): arg_error("Invalid form for *{}*: {}".format(name, value)) 
    return value

if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--string',
                        help=('String argument'))
    parser.add_argument('-f','--file',
                        help=('File argument'))
    parser.add_argument('-d','--dir',
                        help=('Directory argument'))
    parser.add_argument('-n','--newfile',
                        help=('New file to be made'))
    parser.add_argument('-i','--int',
                        help=('Integer argument'))
    parser.add_argument('-p','--pattern',
                        help=('Argument following a pattern'))
    parser.add_argument('-u','--unrequired',
                        help=('Not required argument, with default'))
    args = parser.parse_args()
    
    mystring = check_arg(args.string, 'string')
    myfile = check_arg(args.file, 'file', file=True)
    mydir = check_arg(args.dir, 'dir', dir=True)
    mynewfile = check_arg(args.newfile, 'newfile', newfile=True)
    myint = check_arg(args.int, 'int', pattern=r"^\d+$")
    mypat = check_arg(args.pattern, 'pattern', pattern=r"^\d{3}-\d{3}-\d{4}$")
    mydefault = check_arg(args.unrequired, 'unrequired', req=False, default='default')
    
    main(mystring, myfile, mydir, mynewfile, myint, mypat, mydefault)
#########################################################
