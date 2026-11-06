"""
Task 4: Rock-Paper-Scissors Game
CodSoft Python Programming Internship
Author: Thilochan P
"""

import random

CHOICES = ["rock", "paper", "scissors"]
ICONS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0
    ties = 0
    rounds = 0

    print("=========================================")
    print("    ROCK - PAPER - SCISSORS GAME         ")
    print("=========================================")
    print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock")

    while True:
        rounds += 1
        print(f"\n--- ROUND {rounds} ---")
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").strip().lower()

        if user_choice in ['q', 'quit', 'exit']:
            break

        if user_choice not in CHOICES:
            print("[!] Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            rounds -= 1
            continue

        computer_choice = random.choice(CHOICES)

        print(f"You chose     : {user_choice.capitalize()} {ICONS[user_choice]}")
        print(f"Computer chose: {computer_choice.capitalize()} {ICONS[computer_choice]}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result        : It's a TIE! 🤝")
            ties += 1
        elif winner == "user":
            print("Result        : YOU WIN! 🎉")
            user_score += 1
        else:
            print("Result        : COMPUTER WINS! 🤖")
            computer_score += 1

        print(f"Current Score | You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    print("\n=========================================")
    print("               GAME OVER                 ")
    print("=========================================")
    print(f"Total Rounds Played : {rounds}")
    print(f"Final Score Board   : You {user_score} - {computer_score} Computer (Ties: {ties})")
    if user_score > computer_score:
        print("Final Verdict       : Champion! 🏆 You won the series!")
    elif user_score < computer_score:
        print("Final Verdict       : Better luck next time! Computer won the series.")
    else:
        print("Final Verdict       : The series ended in a tie!")
    print("Thanks for playing! 👋\n")

if __name__ == "__main__":
    main()
