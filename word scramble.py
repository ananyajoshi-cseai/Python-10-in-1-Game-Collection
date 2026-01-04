import random
import time

def word_scramble():
    """
    The main function for the Word Scramble game.
    The player must unscramble a jumbled word.
    """
    
    print("📜 Welcome to Word Scramble!")
    print("Unscramble the letters to form the correct word.")

    # A list of words the game can choose from
    word_list = [
        "python",
        "college",
        "project",
        "submit",
        "coding",
        "semester",
        "random"
    ]

    # 1. Choose a random word
    correct_word = random.choice(word_list)
    
    # 2. Convert the word to a list of characters for shuffling
    word_chars = list(correct_word)
    
    # 3. Shuffle the list of characters (This is the "scramble" part)
    random.shuffle(word_chars)
    
    # 4. Convert the shuffled list back into a single string (the jumbled word)
    jumbled_word = "".join(word_chars)
    
    # Ensure the jumbled word is not the same as the correct word (for a better experience)
    while jumbled_word == correct_word:
        random.shuffle(word_chars)
        jumbled_word = "".join(word_chars)


    # --- Game Play Loop ---
    
    attempts = 0
    max_attempts = 3
    
    print("-" * 30)
    print(f"Your jumbled word is: **{jumbled_word.upper()}**")
    print("-" * 30)
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1} of {max_attempts}. Your guess: ").lower().strip()
        attempts += 1
        
        if guess == correct_word:
            print("\n🎉 **CONGRATULATIONS!** You unscrambled the word!")
            print(f"The correct word was: {correct_word.upper()}")
            return  # End the game function
        
        elif attempts < max_attempts:
            print("❌ Incorrect. Keep trying!")
            
    # If the loop finishes without a correct guess
    print("\n💔 GAME OVER.")
    print(f"You ran out of attempts. The correct word was: **{correct_word.upper()}**")

# To test the game directly (you would call this function from your main menu)
if __name__ == "__main__":
    word_scramble()
