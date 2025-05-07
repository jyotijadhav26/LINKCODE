class Test:
    
    def m1(self):
        a=10
        print(a)

    def m2(self):
        b=20
        print(b)
        c= self.m1()
        
    
t1=Test()
t1.m1()
t1.m2()


class Test:
    
    def Avg(self,list):
        # sum=0
        # cnt=0
        # res=0
        # for i in list:
        #     sum=sum+i
        #     cnt+=1
        # res=sum/cnt
        # return res
        result=sum(list)/len(list)
        return f"Avg is : {result}"

t=Test()
Avg=t.Avg([1,2,3,4])
print(Avg)

        
        
        
        
        
        
        
