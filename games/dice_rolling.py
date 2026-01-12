import random

def play():
    """
    Simulates rolling one or more dice with a user-specified number of sides.
    """
    print("\n--- 9. Enhanced Dice Rolling Simulator ---")
    
    # --- 1. Get Number of Dice ---
    while True:
        num_dice_input = input("How many dice do you want to roll (e.g., 2)? ").strip()
        
        if num_dice_input.isdigit() and int(num_dice_input) > 0:
            num_dice = int(num_dice_input)
            break
        else:
            print("Invalid input. Please enter a positive number.")
            continue

    # --- 2. Get Number of Sides ---
    while True:
        num_sides_input = input("How many sides should the dice have (e.g., 6, 10, 20)? ").strip()
        
        if num_sides_input.isdigit() and int(num_sides_input) >= 2: # Minimum 2 sides for a die
            num_sides = int(num_sides_input)
            break
        else:
            print("Invalid input. Please enter a number greater than or equal to 2.")
            continue

    results = []
    total_sum = 0
    
    print(f"\nRolling {num_dice} x D{num_sides} dice...")
    
    # Use a for loop to simulate each individual die roll
    for i in range(num_dice):
        # random.randint(1, num_sides) uses the user-specified sides
        roll = random.randint(1, num_sides)
        results.append(str(roll))
        total_sum += roll
    
    print("-" * 40)
    print(f"Roll Details: {num_dice} dice, {num_sides} sides each.")
    print(f"Individual Rolls: {', '.join(results)}")
    print(f"Total Sum: **{total_sum}**")
    print("-" * 40)

if __name__ == "__main__":
    play()

