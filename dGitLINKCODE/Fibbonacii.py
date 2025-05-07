

def Fibonacii(num):
    first=0
    second=1
    print(f"Fibonacii Series of {num} is : {first} {second}",end=" ")
    for i in range(2,num+1):
        third=first+second
        first=second
        second=third
        print(third,end=" ")
    
num=int(input("Enter a number: "))

Fibonacii(num)