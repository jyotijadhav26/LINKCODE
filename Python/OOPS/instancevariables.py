class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print(f"Hello my  name is {self.name} and my marks are {self.marks}")
    
    def grade(self):
        if self.marks>=60:
            print("My grade is First class")
        elif self.marks>=50 & self.marks<60:
            print("My grade is Second class")
        elif self.marks>=35 & self.marks<50:
            print("Pass")
        else:
            print("You are failed")
            
            
n=int(input("Enter no of students:"))
for i in range(n):
    name=input("Enter your name please: ")
    marks=int(input("Enter your marks: "))
    s=Student(name,marks)
    s.display()
    s.grade()

        
