a=int(input("Fibonacci no:"))
i=0
num1=0
num2=1
print(0,1)
for i in range(a-2):
    i=num1+num2
    print(i)
    num1=num2
    num2=i
