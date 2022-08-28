"""
a finction that print all the numbers from 1-100
if the number modolu 3 print fizz
if the number modolu 5 print buzz
if the number modolu 3 and 5 print fizzBuzz
with for loop
"""

def fizzBuzz ():
    for x in range (1, 101):
        if (x%3) == 0 :
            print ("fizz")
        elif (x%5) == 0 :
            print ("buzz")
        elif (x%3) == 0 and (x%5) == 0:
            print ("fizzBuzz")
        else:
            print (x)

fizzBuzz()
