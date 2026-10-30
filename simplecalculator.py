
try:
 num1 = int(input("Enter first number: "))
 num2 = int(input("Enter second number: "))
except ValueError:
    print("Error:Please enter whole numbers only")
    exit()

print("/nSelect an operator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
try:
 choice = int(input("Enter your choice(1-4): "))
except ValueError:
    print("Error:Choice must be a number")
    exit()


if choice == 1:
    result = num1 + num2
    print("Result:",result)
elif choice == 2:
    result = num1 - num2
    print("Result:",result)


elif choice == 3:
    result = num1 * num2
    print("Result:",result)

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("Result:",result)
    else:
        print("Syntax Error")

else:
    print("Invalid Choice")



