
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
      def desc(self):
           desc_person = "First name: %s \n Last name %s" % (self.fname, self.lname)
           return desc_person
person2 = Student()

person2.fname =input("Enter a first name: \n")
person2.lname = input("Enter a last name: \n")
person2.studentID=int(input("Enter a student ID number: \n"))
print(person2.desc())

# take multiple inputs in array
input_int_array = [int(x) for x in input("enter a list of numbers").split()]
print("array:", input_int_array)
