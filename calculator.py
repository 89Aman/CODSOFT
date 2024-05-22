operations = ["1.+ \n 2.-  \n3.*  \n4./"]
for operators in operations:
    print(operators)

 
num1= int(input("Enter The First Number - "))
num2 = int(input("Enter The Second Number - "))
oprtn = input("Enter Arithmatic Operator  serial number - ")
if oprtn =="1":
    result = num1 +num2
if oprtn =="2":
    result = num1 - num2
if oprtn =="3":
    result = num1 * num2
if oprtn =="4":
    result = num1  / num2
else:
    result = print("Invalid Entry")

print(result)