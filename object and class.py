

# class Student:
#     def __init__(self,name):
#         self.name=name
#         print(f"My name is {self.name}")
      
    
    
# s1=Student('Jyoti')   #====> Instance of class/object

# # print(s1.name)




class Calculator:
    

    def addition(self,a,b):
        return a+b

    def substraction(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def division(self,a,b):
        try:
                return a/b
        except:
            print("Zero Division Error ....!!!")
                

c1=Calculator()

sum=c1.addition(10,12)
print(f"Addition : ",sum)

sub=c1.substraction(13,1)
print(f"SUBSTRACTION : ",sub)

mul=c1.mul(12,25)
print(f"MULTIPICATION : ",mul)

div=c1.division(10,2)
print(f"DIVISION : ",div)


div1=c1.division(10,0)
# print(f"DIVISION : ",div1)