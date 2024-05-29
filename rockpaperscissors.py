import random

def Game(our_choice, computers_choice):
    if our_choice == computers_choice:
        return "It's a tie!"
    elif (our_choice == 'rock' and computers_choice == 'paper') or \
         (our_choice == 'paper' and computers_choice == 'scissors') or \
         (our_choice == 'scissors' and computers_choice == 'rock'):
        return "Computer wins!"
    else:
        return "You win!"

def main():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        our_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if our_choice not in choices:
            print("Invalid choice! Please choose again.")
            continue
        
        computers_choice = random.choice(choices)
        print(f"The computer chooses: {computers_choice}")
        
        result = Game(our_choice, computers_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
