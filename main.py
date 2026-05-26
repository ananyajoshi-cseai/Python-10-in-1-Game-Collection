import sys
import os

# Import modules from the games folder
from games import (
    blackjack,
    dice_rolling,
    mad_libs,
    magic_8_ball,
    password_generator,
    pet,
    quiz,
    random_number,
    rock_paper_scissors,
    word_scramble
)

def clear_screen():
    # Clears the console screen for a cleaner look.
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("==========================================")
        print("   PYTHON 10-IN-1 GAME COLLECTION MENU    ")
        print("==========================================")
        print("1.  Blackjack")
        print("2.  Dice Rolling Simulator")
        print("3.  Mad Libs Generator")
        print("4.  Magic 8-Ball")
        print("5.  Password Generator")
        print("6.  Pet Simulator")
        print("7.  Quiz / FLAMES")
        print("8.  Random Number Guesser")
        print("9.  Rock Paper Scissors")
        print("10. Word Scramble")
        print("Q.  Quit")
        print("==========================================")
        
        choice = input("Enter your choice (1-10 or Q): ").strip().upper()

        if choice == 'Q':
            print("\nThanks for playing! Goodbye.")
            sys.exit()

        try:
            if choice == '1':
                blackjack.play()
            elif choice == '2':
                dice_rolling.play()
            elif choice == '3':
                mad_libs.play()
            elif choice == '4':
                magic_8_ball.play()
            elif choice == '5':
                password_generator.play()
            elif choice == '6':
                pet.play()
            elif choice == '7':
                quiz.play()
            elif choice == '8':
                random_number.play()
            elif choice == '9':
                rock_paper_scissors.play()
            elif choice == '10':
                word_scramble.play()
            else:
                input("\nInvalid selection. Press Enter to try again...")
                continue
            
            # Pause for a while after game finishes before showing menu again for clarity.
            input("\nPress Enter to return to the main menu...")

        except AttributeError:
            print(f"\n[Error] The file for choice {choice} is missing a 'play()' function.")
            print("Did you remember to edit the game file to include 'def play():'?")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"\n[Error] An unexpected error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
