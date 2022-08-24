import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        self.no=no
        realNumbersAdded=self.real+no.real
        imaginaryNumbersAdded=self.imaginary + no.imaginary
        return Complex(realNumbersAdded,imaginaryNumbersAdded)
    def __sub__(self, no):
        self.no=no
        realNumbersSubtract=self.real-no.real
        imaginaryNumbersSubtract=self.imaginary-no.imaginary
        return Complex(realNumbersSubtract,imaginaryNumbersSubtract)
    def __mul__(self, no):
        self.no=no
        xVal=(self.real* no.real) - (self.imaginary * no.imaginary)
        yVal=(self.real * no.imaginary)+ (self.imaginary * no.real)
        return Complex(xVal,yVal)
    
    def __truediv__(self, no):
        selfVals = Complex(self.real, self.imaginary) * Complex(no.real, (-no.imaginary))
        noVals = Complex(no.real,no.imaginary) * Complex(no.real, (-no.imaginary))
        return Complex((selfVals.real/noVals.real), (selfVals.imaginary/noVals.real))
    def mod(self):
        self.self=self
        placeHolder=math.sqrt((pow(self.real,2))+(pow(self.imaginary, 2)))
        return Complex(placeHolder,0) #because the imaginary part is 0
    def __str__(self):
        if self.imaginary == 0:
               result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
