### This is a Python program to sum three given integers. However, if two values are equal, the sum will be zero. 

print("Input three integer numbers: ")
number1 = input()
number2 = input()
number3 = input()

a1 = int(number1)
a2 = int(number2)
a3 = int(number3)

sum = 0
if not(a1 == a2 or a2 == a3 or a3 == a1):
    sum = a1 + a2 + a3
  
print("sum = ", sum)

