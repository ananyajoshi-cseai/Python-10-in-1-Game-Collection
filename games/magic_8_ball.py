import random
import time
def play():
    def magic_8_ball():
        """
        Simulates a Magic 8-Ball.
        """
        # List of possible Magic 8-Ball responses
        responses = [
            # Positive responses
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
    
            # Non-committal responses
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
    
            # Negative responses
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
    
        print(" Welcome to the Python Magic 8-Ball! ")
        print("Ask any YES or NO question you have in your mind.")
        
        # Use a loop to allow the user to keep asking questions
        while True:
            question = input("\nYour Question (Type 'exit' to quit): ")
    
            if question.lower() == 'exit':
                print("Thank you for consulting the Magic 8-Ball. Goodbye!")
                break
            
            if not question.strip():
                print("Please enter a question.")
                continue
                
            print("Shaking the ball...")
            # Add a short delay for dramatic effect (optional)
            time.sleep(2) 
            
            # Select a random response from the list
            answer = random.choice(responses)
            
            print(f"\n The Magic 8-Ball says: **{answer}** ")
            
# To test the game directly (you would call this function from your main menu)
if __name__ == "__main__":
    play()

