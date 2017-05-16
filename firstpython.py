#!/usr/bin/python
# This is written by dilip
import sys

def Hello(name):
	if name == 'Dilip':
		print 'Alert: Dilip Mode'
		name = name + '???'
	else	
		print 'Else'
	name = name + '!!!!!'
	print 'Hello', name
	
def main():
	Hello(sys.argv[1])
	
