import random

spcl_char = list("!@$%^&*|#")
alphbts =list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


user_input = True
while user_input:
    length = int(input("Enter password Length - "))
    numbs = input("Want numbers Y/N ?")
    spcl_char=input("Want special characters  Y\N ?")
    user_input = False


for numbs in user_input.lower() == "Y" :
        for reps in range(1,length + 1):
            password = random.choice(alphbts)
        else:
            pass
for spcl_char in user_input.lower() == "Y":
        pass_part2 = random.choice(spcl_char)

print(password + pass_part2)
