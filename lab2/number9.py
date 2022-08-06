#Get input of the age of 3 people by user and determine oldest and youngest among them

number1 = int(input("Enter First Person's Age : "))
number2 = int(input("Enter Second Person's Age : "))
number3 = int(input("Enter Third Person's Age : "))
maxNumber=max(number1,number2, number3)
minNumber=min(number1,number2, number3)
print("the oldest person is : "+ str(maxNumber))
print("the youngest person is : "+ str(minNumber))
