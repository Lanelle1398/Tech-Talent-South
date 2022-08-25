import statistics
class Person:
    fname = ""
    lname = ""
    def desc(self):
        desc_person = "%s %s is a person." % (self.fname, self.lname)
        return desc_person

class Student(Person):
      def desc(self):
          #desc_person = "%s %s is a student." % (self.fname, self.lname)
           desc_person = "First name: %s \nLast name: %s \nStudent ID: %d" % (self.fname, self.lname, self.studentID)
           return desc_person
        
class Grades(Student):
      def desc(self, myList):
           #self.avg=statistics.mean(myList)
           desc_person = self.fname2+ " " + self.lname2 + " " + "Student ID " + str(self.studentID2) + ", you got a " + str(statistics.mean(myList))
           #"%s %s Student ID %d , you got a " % (self.fname2, self.lname2, self.studentID2)
           return desc_person
            
person2 = Student()
person2.fname =input("Enter a first name: \n")
person2.lname = input("Enter a last name: \n")
person2.studentID=int(input("Enter a student ID number: \n"))

studentGrades=Grades()
studentGrades.fname2=person2.fname
studentGrades.lname2=person2.lname
studentGrades.studentID2=person2.studentID

#print(person2.desc())
# take multiple inputs in array
input_int_array= [int(x) for x in input("enter a list of numbers").split()]
#print(studentGrades.desc(input_int_array))
print(studentGrades.desc(input_int_array))

#studentGrades.myList=input_int_array 
#print("array:", input_int_array)

