# #A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print percentage of class attended
    # Is student is allowed to sit in exam or not?

classHeld= int(input("how many classes are held : "))
classesAttended=int(input("how many classes did you attend: "))
classesAttended/classHeld
percentAttend=(classesAttended/classHeld)*100
if percentAttend<75:
    print("You can not take part in the class")
else:
    print("You can take part in the class")
