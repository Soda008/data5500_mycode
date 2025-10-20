from DeckOfCards import DeckOfCards

def card_value(card):
    """Return the blackjack value of a card."""
    if card.rank in ['J', 'Q', 'K']:
        return 10
    elif card.rank == 'A':
        return 11  # initially treat Ace as 11
    else:
        return int(card.rank)

def adjust_for_aces(score, aces):
    """Adjust score if there are Aces and the score is over 21."""
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score, aces

def start_game(deck):
    print("Welcome to Blackjack!")
    
    print("\nDeck before shuffle:")
    deck.print_deck()
    
    deck.shuffle()
    
    print("\nDeck after shuffle:")
    deck.print_deck()
    
    user_hand = []
    dealer_hand = []
    user_score = 0
    dealer_score = 0
    user_aces = 0
    dealer_aces = 0

    # Deal initial cards to user
    for _ in range(2):
        card = deck.deal()
        user_hand.append(card)
        val = card_value(card)
        user_score += val
        if card.rank == 'A':
            user_aces += 1
    user_score, user_aces = adjust_for_aces(user_score, user_aces)

    print("\nYour cards:", ", ".join(str(c) for c in user_hand))
    print("Your total score:", user_score)

    # User turn
    while user_score < 21:
        choice = input("Would you like a hit? (y/n): ").lower()
        if choice == 'y':
            card = deck.deal()
            print("You got:", card)
            user_hand.append(card)
            val = card_value(card)
            user_score += val
            if card.rank == 'A':
                user_aces += 1
            user_score, user_aces = adjust_for_aces(user_score, user_aces)
            print("Your current score:", user_score)
        elif choice == 'n':
            break
        else:
            print("Please type 'y' or 'n'.")

    if user_score > 21:
        print("You busted! Your score:", user_score)
        return

    # Dealer turn
    for _ in range(2):
        card = deck.deal()
        dealer_hand.append(card)
        val = card_value(card)
        dealer_score += val
        if card.rank == 'A':
            dealer_aces += 1
    dealer_score, dealer_aces = adjust_for_aces(dealer_score, dealer_aces)

    print("\nDealer's cards:", ", ".join(str(c) for c in dealer_hand))
    print("Dealer's score:", dealer_score)

    while dealer_score < 17:
        card = deck.deal()
        print("Dealer hits:", card)
        dealer_hand.append(card)
        val = card_value(card)
        dealer_score += val
        if card.rank == 'A':
            dealer_aces += 1
        dealer_score, dealer_aces = adjust_for_aces(dealer_score, dealer_aces)
        print("Dealer's score:", dealer_score)

    # Determine outcome
    print("\nFinal Scores -> You:", user_score, "Dealer:", dealer_score)
    if user_score > 21:
        print("You busted, you lose!")
    elif dealer_score > 21:
        print("Dealer busted, you win!")
    elif user_score > dealer_score:
        print("You win!")
    elif user_score == dealer_score:
        print("It's a tie!")
    else:
        print("Dealer wins!")

# Main game loop
deck = DeckOfCards()

while True:
    play = input("\nDo you want to play Blackjack? (y/n): ").lower()
    if play == 'y':
        start_game(deck)
    elif play == 'n':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Please type 'y' or 'n'.")
