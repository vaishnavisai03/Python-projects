import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

want_to_play = input("Do you want to play blackjack? type y/n: ").lower()

if want_to_play == "y":

    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)

    sum_of_user_cards = sum(user_cards)
    sum_of_computer_cards = sum(computer_cards)

    print(f"Your cards: {user_cards}, total: {sum_of_user_cards}")
    print(f"Computer first card: {computer_cards[0]}")

    # 🎯 USER TURN
    while sum_of_user_cards < 21:
        ask = input("Do you want another card? y/n: ").lower()

        if ask == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            sum_of_user_cards = sum(user_cards)

            # Handle Ace (11 → 1)
            if sum_of_user_cards > 21 and 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                sum_of_user_cards = sum(user_cards)

            print(f"Your cards: {user_cards}, total: {sum_of_user_cards}")

            if sum_of_user_cards > 21:
                print("You went over. Bust! You lose.")
                break
        else:
            break

    # 🎯 COMPUTER TURN
    if sum_of_user_cards <= 21:
        while sum_of_computer_cards < 17:
            new_card = random.choice(cards)
            computer_cards.append(new_card)
            sum_of_computer_cards = sum(computer_cards)

            # Handle Ace
            if sum_of_computer_cards > 21 and 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
                sum_of_computer_cards = sum(computer_cards)

    # 🎯 FINAL RESULT
    print("\nFinal Results:")
    print(f"Your cards: {user_cards}, total: {sum_of_user_cards}")
    print(f"Computer cards: {computer_cards}, total: {sum_of_computer_cards}")

    if sum_of_user_cards > 21:
        print("You lose.")
    elif sum_of_computer_cards > 21:
        print("Computer bust. You win!")
    elif sum_of_user_cards > sum_of_computer_cards:
        print("You win!")
    elif sum_of_user_cards == sum_of_computer_cards:
        print("Draw.")
    else:
        print("Computer wins.")