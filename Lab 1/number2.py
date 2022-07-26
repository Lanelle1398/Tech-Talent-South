
UserInput= int(input("enter a number"))
x = int( "%s" % UserInput)
x2 = int( "%s%s" % (UserInput,UserInput) )
x3 = int( "%s%s%s" % (UserInput,UserInput,UserInput) )
y=x+x2+x3
print(str(x)+ "+"+ str(x2)+ "+" + str(x3)+"="+str(y))
