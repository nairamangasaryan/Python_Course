print("""
    This is a Python program that determines whether a given number 
    (accepted from the user) is even or odd, 
    and prints an appropriate message to the user.
""")  
print()
number = input("Input the number: ", )
num = int(number)
if num % 2 == 0:
    print("Your entered number is even")
else:
    print("Your entered number is odd")
print()

