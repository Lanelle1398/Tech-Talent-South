import numpy

#polyval is a method that finds the value of p at point 'x'
#numpy.polyval(p, x)
#x is the number for evaluating the polynomials
#p is the polynomial coefficients

p= [float(x) for x in input().split()]
x=float(input())
print(numpy.polyval(p,int(x)));
