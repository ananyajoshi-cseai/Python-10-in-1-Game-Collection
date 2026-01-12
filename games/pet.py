import time
import random

def main():
    # --- 1. Initialize Pet Stats ---
    # Set the starting values for the pet's needs.
    hunger = 5
    happiness = 5
    energy = 5

    # Set the boundaries
    MAX_STAT = 20
    MIN_STAT = 0
    
    # How much time passes per loop
    TIME_TICK = 1

    print("--- Welcome to Pet Simulator! ---")
    print("Take care of your new digital pet.")
    print("Try to keep its stats from hitting 0!")
    print("-" * 30)

    # --- 2. Main Game Loop ---
    # The game continues as long as this loop runs.
    while True:
        
        # --- 3. Check Game Over Condition ---
        # If any stat hits 0, the game ends.
        if hunger <= MIN_STAT or happiness <= MIN_STAT or energy <= MIN_STAT:
            print("\nOh no! One of your pet's stats hit 0.")
            if hunger <= MIN_STAT:
                print("Your pet was too hungry. :(")
            elif happiness <= MIN_STAT:
                print("Your pet got too sad. :(")
            else:
                print("Your pet ran out of energy. :(")
            print("--- Game Over ---")
            break # Exit the while loop

        # --- 4. Display Current Stats ---
        # This provides a simple visual bar for each stat.
        print(f"\n--- Current Stats ---")
        print(f"Hunger:    [{'*' * hunger}{' ' * (MAX_STAT - hunger)}] {hunger}/{MAX_STAT}")
        print(f"Happiness: [{'*' * happiness}{' ' * (MAX_STAT - happiness)}] {happiness}/{MAX_STAT}")
        print(f"Energy:    [{'*' * energy}{' ' * (MAX_STAT - energy)}] {energy}/{MAX_STAT}")
        print("-" * 30)

        # --- 5. Get Player Input ---
        print("What would you like to do?")
        print("  1. Feed")
        print("  2. Play")
        print("  3. Sleep")
        print("  4. Quit")
        choice = input("Enter your choice (1-4): ")

        # --- 6. Process Player's Choice ---
        if choice == '1': # Feed
            print("\nYou feed your pet. Yum!")
            hunger = min(MAX_STAT, hunger + 4) # Increase stat, but don't go over MAX
        
        elif choice == '2': # Play
            print("\nYou play with your pet. Fun!")
            happiness = min(MAX_STAT, happiness + 4)
        
        elif choice == '3': # Sleep
            print("\nYou let your pet sleep. Zzzz...")
            energy = min(MAX_STAT, energy + 4)
        
        elif choice == '4': # Quit
            print("\nThanks for playing! Goodbye.")
            break # Exit the while loop
        
        else:
            print("\nThat's not a valid choice. Try again.")
            # We don't make time pass if the choice was invalid
            continue 

        # --- 7. Time Passes (Stats Decay) ---
        # After every valid action, time passes and stats decrease.
        # We add a small random element to make it interesting.
        print("...time passes...")
        hunger -= random.randint(1, 2)
        happiness -= random.randint(1, 2)
        energy -= random.randint(1, 2)
        
        # Ensure stats don't go below the minimum
        hunger = max(MIN_STAT, hunger)
        happiness = max(MIN_STAT, happiness)
        energy = max(MIN_STAT, energy)

        # --- 8. Pause the Game ---
        # This makes the loop wait for 1 second so it doesn't run too fast.
        time.sleep(1)


# This standard Python line ensures the main() function runs when the script is executed
if __name__ == "__main__":
    main()
