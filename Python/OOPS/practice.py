

class Test:
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def m1(self):
        self.d=40
    
    def m2(self):
        self.e=50

t1=Test(10,20,21)
t1.m1()

t2=Test(11,12,13)
t2.m2()
t2.x=55
t2.y=99

print(t1.__dict__)
print(t2.__dict__)