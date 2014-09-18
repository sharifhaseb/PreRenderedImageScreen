#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script launches all process one minute later after it is iniateted.

__author__ = ('Kaan Akşit')

import sys,datetime


def main():
    # Get the current time.       
    now = datetime.datetime.now()
    # Print the current time.
    print 'Current time is ', now.strftime("%Y-%m-%d %H:%M")
    # If the next minute is too close than jump to the other one.
    if 60 -  now.second < 10:
       a = 2
    else:
       a = 1
    # Desired minute.    
    td  = (now.minute + a ) % 60
    # Loop to check if desired time is reached.
    while td != now.minute :
        # Get the current time to check in the cycle
        now = datetime.datetime.now()
    # Print when the desired time reached.
    print 'Time reached at ', now.strftime("%Y-%m-%d %H:%M")
    return True

if __name__ == '__main__':
    sys.exit(main())

