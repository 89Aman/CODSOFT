operations = ["1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION"]
for operators in operations:
    print(operators)

 
num1= int(input("Enter The First Number - "))
num2 = int(input("Enter The Second Number - "))
oprtn = input("Enter Arithmatic Operator's serial number - ")
if oprtn =="1":
    result = num1 +num2
    print(f"The sum of {num1} and {num2}  are {result}")
elif oprtn =="2":
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2}  are {result}")
elif oprtn =="3":
    result = num1 * num2
    print(f"The multiflication of {num1} and {num2}  are {result}")
elif oprtn =="4":
    result = num1  / num2
    print(f"The division of {num1} and {num2}  are {result}")
