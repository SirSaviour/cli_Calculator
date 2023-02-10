#Saviour Prosper with Student ID - I4G0185511EH

# Python program to perform Addition Subtraction Multiplication Division
# and Modulus of two numbers

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("You can use this program for Simple Arithmethic Operations like Addition, Subtraction, Multiplication, Division and Modulus.")
print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == '%':
    result = num1 % num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)



#Saviour Prosper with Student ID - I4G0185511EH