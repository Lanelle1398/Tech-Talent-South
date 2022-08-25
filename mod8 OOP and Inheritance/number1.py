import statistics
class Person:
    fname = ""
    lname = ""
    def desc(self):
        desc_person = "%s %s is a person." % (self.fname, self.lname)
        return desc_person

class Student(Person):
      def desc(self):
           desc_person = "First name: %s \nLast name: %s \nStudent ID: %d" % (self.fname, self.lname, self.studentID)
           return desc_person
        
class Grades(Student):
      def desc(self, myList):
            averageVal=statistics.mean(myList)
            if  90 <= averageVal <= 100:
                x="A"
            if  80 <= averageVal < 90:
                x="B"
            if  70 <=  averageVal < 80:
                x="C"
            if  60 <=  averageVal < 70:
                x="D"
            if   averageVal  < 50:
                x="F"
            desc_person = self.fname2+ " " + self.lname2 + " " + "Student ID " + str(self.studentID2) + ", you got a " + x
      
            return desc_person
            
person2 = Student()
person2.fname =input("Enter a first name: \n")
person2.lname = input("Enter a last name: \n")
person2.studentID=int(input("Enter a student ID number: \n"))

studentGrades=Grades()
studentGrades.fname2=person2.fname
studentGrades.lname2=person2.lname
studentGrades.studentID2=person2.studentID


input_int_array= [int(x) for x in input("enter a list of space separated numbers ").split()]
print(studentGrades.desc(input_int_array))

