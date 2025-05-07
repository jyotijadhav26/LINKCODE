
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return f"Factorial of given {num} is {fact}"

num=int(input("Enter a  number:"))
fact = factorial(num)
print(fact)