"""
a finction that print all the numbers from 1-100
if the number modolu 3 print fizz
if the number modolu 5 print buzz
if the number modolu 3 and 5 print fizzBuzz
with while loop
"""

def fizzBuzz ():
    i = 1
    while (i < 101 ):
        if (i % 3) == 0: 
            print ("fizz")
        elif (i %5) == 0:
            print ("buzz")
        elif (i%3)== 0 and (i %5)== 0 :
            print ("fizzBuzz")
        else :
            print (i)
        i += 1
    

fizzBuzz ()

