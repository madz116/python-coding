import random
def display_rules():
    print("\n-----Game Rules-----")
    print("Rock beats scissors")
    print("Scissors beat paper")
    print("Paper beats rock\n")

def determine_winner(user, computer):
    if user==computer:
        return "tie"
    elif (user=="rock" and computer=="scissors") or \
         (user=="paper" and computer=="rock") or \
         (user=="scissors" and computer=="paper"):
        return "user"
    else:
        return "computer"
    
def rock_paper_scissors():
    total_choices=["Rock", "paper", "scissors"]

    while True:
        user_score=0
        computer_score=0
        round_num=1

        print("\nWelcome to Rock Paper Scissors!")
        print("type 'rules' to see the rules and 'quit' to exit the game.")

        while True:
            print(f"-----Round Number {round_num}-----")
            print("Choices: rock, paper, scissors")
            user_choice=input("Enter your choice: ").lower()

            if user_choice=="quit":
                print("\nThanks for playing!")
                print(f"Final score- You: {user_score}; Computer: {computer_score}\n")
            elif user_choice=="rules":
                display_rules()
                continue
            elif user_choice not in total_choices:
                print("Invalid Input. Please try again.")
                continue

            computer_choice=random.choice(total_choices)
            print(f"Computer choice: {computer_choice}")

            result=determine_winner(user_choice, computer_choice)

            if result=="tie":
                print("It is a tie.")
            elif result=="user":
                print("User has won this round.")
                user_score+=1
            else:
                print("Computer has won this round.")
                computer_score+=1

            print(f"Current score- You: {user_score} Computer: {computer_score}")
            round_num+=1

        play_again=input("Do you want to play again? (yes/no): ").lower()

        if play_again!="yes":
            print("Goodbye.")
            break

rock_paper_scissors()