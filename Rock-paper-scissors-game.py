import random
score1 = 0
score2 = 0

def input2():
     choices = ["Rock" ,"Paper", "Scissor"]
     return random.choice(choices)

menu = input("To Start any key \nTo Exit press Q or ctrl+ c\n")
if menu.lower() == "q":
    quit()
else:
    while True :
        try:
            opp1 = input("1.Rock\n2.Paper\n3.Scissor")
            opp2 = input2()
            print(f"User - {opp1} , computer - {opp2}")
            if  opp1 =="Rock" and opp2 == "Scissor":
                print("User Wins")
                score1 +=1
            elif opp1 =="Paper" and opp2 == "Scissor":
                print("Computer Wins")
                score2 +=1
            elif opp2 =="Rock" and opp2 == "Paper":
                print("Computer wins")
                score2 +=1
            elif opp1 =="Rock" and opp2 == "paper":
                print("User Wins")
                score1 +=1
            elif opp1 == opp2 :
                print("Its a tie")
                print("No score !")
            else :
                 print("Wrong choice")
            ctnue =input("Want to play again? Y/N")
            if ctnue.lower() =="n":
                        quit()
            else:
                continue 
        finally:
            print(f"User - {score1} \nComputer - {score2}")


        