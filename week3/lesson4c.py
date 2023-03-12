"""  Write a Python program that returns true
     if the two given integer values are equal 
     or their sum or difference is 5.
"""
print("Input 2 integer numbers: ")
number1 = input()
number2 = input()

a1 = int(number1)
a2 = int(number2)

if ((a1 == a2) or (a1 - a2 == 5) or (a1 + a2 ==5)):
    result = True
else:
    result = False

print(result)

