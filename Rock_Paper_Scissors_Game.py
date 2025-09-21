import random
options=["rock", "paper", "scissors"]

play_again="yes"
    

print("Hellooo and Welcome!!!")
print("\n Do you want to play 'Rock-Paper-Scissors' with me? If 'Yes' then help me to know your choice-")
print("What do you want to choose--Rock, Paper or Scissors?")
while play_again=="yes":
    computer_choice=random.choice(options)
    
    player_choice=(input("Please enter your choice:"))
    
    if player_choice not in options:
        print("Invalid choice! try again.\n")

    else:
        print("\n You chose:",{player_choice})
        print(" And")
        print(" Computer chose:",{computer_choice})
        print("So,")

        if (player_choice==computer_choice):
            print("It's a tie")

        elif(player_choice=="rock" and computer_choice=="scissorss"):
            print("Congratulations..You win!!")

        elif(player_choice=="scissors" and computer_choice=="paper"):
            print("Congratulations..You win!!")

        elif(player_choice=="paper" and computer_choice=="rock"):
           print("Congratulations..You win!!")
            
        else:
           print("Computer win!!!!")

        play_again=input("\nDo you wanna play again? (yes/no): \n").lower()
print("Thanks for playing!!!")






