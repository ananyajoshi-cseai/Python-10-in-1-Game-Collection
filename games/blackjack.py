# ------------ Importing required modules ---------------#
import random as rn
def play():
    # ------------ Welcome Message and rules for the game --------------#
    def intro():
        print("WELCOME TO THE GAME OF BLACKJACK\n")
        print("Below are the mentioned rules. New players are advised to go through the rules before proceding.\n")
        print("The rules are as follows:\n\
                1. The game is played with a deck of 52 cards.\n\
                2. Each player is dealt two cards.\n\
                3. The dealer, which in this case is the computer, is dealt one card face up and one card face down.\n\
                4. The goal is to get as close to 21 as possible without going over.\n\
                5. If you go over 21, you bust and lose.\n\
                6. If the dealer goes over 21, they bust and you win.\n\
                7. If you get 21 on your first two cards, you have a blackjack.\n\
                8. If the dealer gets 21 on their first two cards, they have a blackjack.\n\
                9. If both you and the dealer have a blackjack, it's a push.\n\
                10. You can hit to get another card or stand to keep your current hand.\n\
                11. The dealer must hit until they have at least 17.\n\
                12. The dealer must stand on all 17s.\n\
                13. All aces are counted as 11 and will be changed to 1 if the total sum exceeds 21.\n\
                14. All face cards are counted as 10.\n\
                15. All number cards are counted as their face value.\n\
                16. Please note that some rules have been modified so as to make the game simple for players.\n\
                17. Enjoy the game and good luck!\n")
    
    # ------------- Defining the deck ----------------#
    deck = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
    def gameplay():
        # Create a copy of the deck for the current game
        current_deck = list(deck.keys()) * 4 # A full deck has 4 of each card type
        rn.shuffle(current_deck)
    
        go = input("Do you wish to continue to the game [y/n]: ")
        if go.lower() == "y":
            name = input("Please enter your name to proceed: ")
            print(f'Let the game begin {name}!!\n')
    
            player_hand = []
            dealer_hand = []
            player_sum = 0
            deal_sum = 0
    
            def deal_card(hand):
                nonlocal current_deck
                card = current_deck.pop()
                hand.append(card)
                return deck[card]
    
            def calculate_sum(hand, current_sum):
                # Recalculate sum to handle Aces correctly
                current_sum = sum(deck[card] for card in hand)
                num_aces = hand.count('Ace')
                while current_sum > 21 and num_aces > 0:
                    current_sum -= 10
                    num_aces -= 1
                return current_sum
    
            # Initial deal
            player_sum += deal_card(player_hand)
            deal_sum += deal_card(dealer_hand)
            player_sum += deal_card(player_hand)
            deal_sum += deal_card(dealer_hand)
    
            player_sum = calculate_sum(player_hand, player_sum)
            deal_sum = calculate_sum(dealer_hand, deal_sum)
    
            print(f"Dealer's face-up card is: {dealer_hand[0]}")
            print(f"Your hand is: {', '.join(player_hand)} (Sum: {player_sum})\n")
    
            # Player's turn
            while player_sum < 21:
                hit_stand = input("Do you want to hit or stand? (h/s): ")
                if hit_stand.lower() == 'h':
                    player_sum += deal_card(player_hand)
                    player_sum = calculate_sum(player_hand, player_sum)
                    print(f"You drew a {player_hand[-1]}.")
                    print(f"Your hand is now: {', '.join(player_hand)} (Sum: {player_sum})\n")
                elif hit_stand.lower() == 's':
                    break
                else:
                    print("Invalid input. Please enter 'h' to hit or 's' to stand.")
    
            # Outcome after player's turn
            if player_sum == 21:
                print(f"Blackjack! You have {player_sum}.\n")
            elif player_sum > 21:
                print(f"Busted! Your sum is {player_sum}. You lose.")
                return
    
            # Dealer's turn
            print(f"Dealer reveals their second card. Hand: {', '.join(dealer_hand)} (Sum: {deal_sum})")
            while deal_sum < 17:
                print("Dealer hits.")
                deal_sum += deal_card(dealer_hand)
                deal_sum = calculate_sum(dealer_hand, deal_sum)
                print(f"Dealer drew a {dealer_hand[-1]}.")
                print(f"Dealer's hand is now: {', '.join(dealer_hand)} (Sum: {deal_sum})\n")
    
            # Final outcome
            print("--- Final Results ---")
            print(f"Your final hand: {', '.join(player_hand)} (Sum: {player_sum})")
            print(f"Dealer's final hand: {', '.join(dealer_hand)} (Sum: {deal_sum})")
    
            if deal_sum > 21:
                print("Dealer busted! You win!")
            elif deal_sum > player_sum:
                print("Dealer wins!")
            elif player_sum > deal_sum:
                print("You win!")
            else: # player_sum == deal_sum
                print("It's a push (tie)!")
        else:
            print("Maybe next time. Goodbye!")
        
    intro()
    while True:
        gameplay()
        play_again = input("Do you want to play another round? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break # Exit the while loop
if __name__ == "__main__":
    play()
