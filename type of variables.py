'''
Type of Variables:

    1. Instance Variables  ---> object level >>> It varries from object to object 
    2. Static Variables    ---> class level  >>> It is same throughout the class
    3. Local Variables     ---> Method level >>> It is declared inside the method

'''

class Student:
    college_name = "VIT PUNE"                                  # ----> class variables

    def __init__(self,name,rollno):
        self.name=name                                         # ----->instance variables
        self.rollno=rollno

    def display(self):
        print(f"My name is {self.name}")
        print(f"My roll no is {self.rollno}")
     
     
    @classmethod   
    def getclgname(cls):
        print(f"College name : {cls.college_name}")   
    
    @staticmethod                                                 # =====> Decorator
    def findAvg(a,b):
        print(f"Average of {a} & {b} : {a+b/2}")    


s1=Student('Jyoti',1035)
s1.display()
print(s1.__dict__)


s1.getclgname()
s1.findAvg(10,20)

Student.findAvg(10,88)

print(Student.college_name)
