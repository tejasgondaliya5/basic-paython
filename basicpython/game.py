import random
if __name__ == "__main__":
    print("Welcome to the Snake Water Gun game!\n\n")

    attempts = 1
    your_point = 0
    computer_point = 0


    while (attempts<=3):

        lst=["snake","water","gun"]
        ran=random.choice(lst)
        
        inp = input("Enter your choice (snake/water/gun): ")
        inp = inp.lower()

        if inp==ran:
            print("Tie")
            print(f"You chose {inp} and computer guess is {ran}")
            print("No body gets point\n")


        elif inp=="snake" and ran=="water":
            your_point=your_point+1
            print(f"You choosed {inp} and computer guess is {ran}")
            print("The snake drank water\n")
            print("You won this round")
            print("You got 1 point\n")          


        elif inp=="water" and ran=="snake":
            computer_point = computer_point + 1
            print(f"You choosed {inp} and computer guess is {ran}")
            print("The snake drank water\n")
            print("You lost this round")
            print("Computer gets 1 point\n")
  


        elif inp=="water" and ran=="gun":
            print(f"You chose {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print("The gun sank in water\n")
            print("You won this round")
            print("You got 1 point\n")
            


        elif inp == "gun" and ran == "water":
            print(f"you choosed {inp} and computer guess is {ran}")
            computer_point = computer_point + 1
            print("The gun sank in water\n")
            print("You Lost this round")
            print("computer gets 1 point\n")
           


        elif inp == "gun" and ran == "snake":
            print(f"You choosed {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print("The snake was shot and it died\n")
            print("You won this round")
            print("You get 1 point\n")
            

        elif inp == "snake" and ran == "gun":
            print(f"you choosed {inp} and computer guess is {ran}")
            computer_point=computer_point+1
            print("The snake was shoot and he died\n")
            print("You lost this round")
            print("computer gets 1 point\n")

        else:
            print("Invalid input!\n")
            continue


        print("No. of guesses left: {}".format(3 - attempts))
        attempts = attempts + 1

        if attempts>3:
            print("Game over!")


    print(f"Your score: {your_point} \nComputer's score: {computer_point}")

    if computer_point > your_point:
        print("Computer won and you lost!")

    elif computer_point < your_point:
        print("You won and computer lost!")

    else:

        print("It was a tie!")
        print("invalid")

    if attempts>3:
        print("game over")

if computer_point > your_point:
    print("Computer wins and you loose")

if computer_point < your_point:
    print("you win and the computer looses")

print(f"your point is {your_point} and computer point is {computer_point}")