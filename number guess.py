import random
target = random.randint(1,100)

while True:
    user_choice = input("Enter the number or Quit: ")
    if(user_choice == "quit"):
        break
    user_choice = int(user_choice)
    if(user_choice == target):
        print("Sucess: Correct Guess")
        print("----GAME OVER----")
    elif(user_choice > target):
        print("Number gussed is big, guess again")
    else:
        print("Number gussed is small , Guess again")

