import random

def play_round():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose from rock, paper, or scissors.")
        return

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        return 'user'
    else:
        print("You lose!")
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        print("Score - User:", user_score, "Computer:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
