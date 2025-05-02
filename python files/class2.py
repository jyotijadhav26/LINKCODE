

class Employee:
    def __init__(self,Ename,EId,Esal,Edes):
        self.Ename=Ename
        self.EId=EId
        self.Esal=Esal
        self.Edes=Edes
        
    def info(self):
        print(f"""Myself {self.Ename} and \nmy employee code is {self.EId} \nworking as a {self.Edes} \nhaving salary {self.Esal}""")

e1=Employee('Jyoti',1045,60000,'Software Developer')
e2=Employee('Harshal',1125,50000,'DevOps Engineer')

e1.info()
print(e1.Ename)



        