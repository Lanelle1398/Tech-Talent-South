# In mathematics, the quadratic equation ax2+bx+c=0 can be solved with the formula x=−b±b2−4ac√2a.

# Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:

import math

def equationroots( a, b, c): 
  
    #myTuple=("")
    # calculating discriminant 
    discriminantValue = ((b ** 2) - (4 * a * c)) # b^2-4ac)
     
    math.sqrt((discriminantValue)) #sqrt(b^2-4ac)
    root1 = ((-b-discriminantValue)/(2 * a)) #[-b-(sqrt(b^2-4ac))]/2a
    root2= ((-b + discriminantValue)/(2 * a) ) #[-b+(sqrt(b^2-4ac))]/2a
   
    myTuple=(root2, root1)
    print(myTuple)
  



equationroots(1,-3,2)
equationroots(1,2,1)
