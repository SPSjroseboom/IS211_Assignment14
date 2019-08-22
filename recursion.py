#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assingment14 - recursion.py
Created on Thu Aug 22 10:09:51 2019
@author: SPSjroseboom
"""


def fibonnaci(n):
    """The fibonnaci sequence. Returns the nth element"""
    if n == 0 or n == 1:
        return -1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print '----------fibonnaci----------' 
print 'fibonnaci(10) is:'
print fibonnaci(10)

def gcd(a, b):
    """Returns the greatest common divisor."""
    return gcd(b, a % b) if b else abs(a)

print '-------------gcd-------------' 
print 'gcd(44, 4) is:'
print gcd(44, 4)

def compareTo(s1, s2):
    """Compares two strings and returns an output.
    Args:
        s1 (string): A string to compare.
        s2 (string): A string to compare.
    Returns:
        int: 0 if strings are of equal length.
        int: 1 if the first string is longer.
        int: -1 if the second string is longer.
    """
    if not s1 and not s2:
        print '\nstring1 and string2 are of equal length:'
        return 0
    elif not s1:
        print '\nstring2 is longer:'
        return -1
    elif not s2:
        print '\nstring1 is longer:'
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

print '----------compareTo----------' 
print 'Compares the length of two strings and returns what is longer.'
print 'Please input your two strings:'
s1 = str(raw_input('string1: ').strip())
s2 = str(raw_input('string2: ').strip())
print compareTo(s1, s2)