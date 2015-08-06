#!/usr/bin/env python
# HW02_ex03_04

# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object 
# as an argument and calls it twice:

# def do_twice(f):
#     f()
#     f()

# Here's an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#     print 'spam'

# do_twice(print_spam)

# 1. Type this example into this script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
#  and calls the function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes a 
# string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
#  as an argument.
# 5. Define a new function called do_four that takes a function object and a value 
# and calls the function four times, passing the value as a parameter. There 
# should be only two statements in the body of this function, not four.
################################################################################
# Write your functions below:
# Body

def print_twice(b):
     print b
     print b

def do_twice(f, b):
     f(b)
     f(b)


def do_four(f, b):
	do_twice(f,b)
	do_twice(f,b)

#do_four(print_twice, 'spam')
  





# Write your functions above:
################################################################################
def main():
    #"""Call your functions within this function.
    #When complete have one function call in this function:
    do_four(print_twice, "spam")
    #"""
    print("Hello World!")
    


if __name__ == "__main__":
    main()