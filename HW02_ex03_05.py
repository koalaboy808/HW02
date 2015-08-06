#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def plus_minus():
	print "+ - - - - + - - - - +"

def minus():   
	print "|         |         |"

def repeat_minus(f):
	f()
	f()
	f()
	f()

def long_plus_minus():
	print "+ - - - - + - - - - + - - - - + - - - - +"

def long_minus():   
	print "|         |         |         |         |"

def long_repeat_minus(f):
	f()
	f()
	f()
	f()





def two_by_two():
	plus_minus()
	repeat_minus(minus)
	plus_minus()
	repeat_minus(minus)
	plus_minus()

def four_by_four():
	long_plus_minus()
	long_repeat_minus(long_minus)
	long_plus_minus()
	long_repeat_minus(long_minus)
	long_plus_minus()
	long_repeat_minus(long_minus)
	long_plus_minus()
	long_repeat_minus(long_minus)
	long_plus_minus()	










# Write your functions above:
################################################################################
def main():

    two_by_two()
    four_by_four()
    
    print("Hello World!")
    



if __name__ == "__main__":
    main()