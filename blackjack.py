# Attempt at making Blackjack in Python
# BLACKJACK: Put down a wager
# Gets 2 cards (21 initially = blackjack)
# Can choose to hit or stand
# if cards > 21 = bust

from random import shuffle

card_values = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
card_suits = ['SPADES','CLUBS','DIAMONDS','HEARTS']
deck = [[value,suit] for value in card_values for suit in card_suits]

def handTotals(hand):
    total = 0
    for card in hand:
        if card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Jack':
            total += 10
        elif card[0] == 'Ace' and (total + 11) <= 21:
            total += 11
        elif card[0] == 'Ace' and (total + 11) > 21:
            total += 1
        else:
            total += card[0]
    return total
        
def blackjack():
    shuffle(deck)
    playerHand = [deck.pop(),deck.pop()]
    dealerHand = [deck.pop(),deck.pop()]
    print()
    print('Dealer\'s Hand: ',[['??????'],dealerHand[1]])
    while handTotals(dealerHand) <= 16:
        dealerHand.append(deck.pop())
    while True:
        print('Your Hand: ',playerHand)
        action = input('Hit (1) or Stand (2)?: ')   
        print()
        if action == '1':
            playerHand.append(deck.pop())
        if handTotals(playerHand) > 21:
            print('Your Hand: ',playerHand)
            print('Total = ',handTotals(playerHand))
            print('BUST! YOU LOSE!')
            return
        elif action == '2':
            print('Your Hand: ',playerHand)
            print('Total = ',handTotals(playerHand))
            print()
            print('Dealer\'s Hand: ',dealerHand)
            print('Total = ',handTotals(dealerHand))
            if handTotals(dealerHand) > 21:
                print()
                print('DEALER BUST! YOU WIN!')
            elif handTotals(dealerHand) > handTotals(playerHand):
                print()
                print('YOU LOSE!')
            elif handTotals(dealerHand) < handTotals(playerHand):
                print()
                print('YOU WIN!')
            else:
                print()
                print('DRAW!')
            return

option = input('START (1) OR QUIT (2) ?: ')
if option == '1':
    while True:
        blackjack()
        print()
        restart = input('PLAY AGAIN (1) OR QUIT (2)?: ')
        if restart == '1':
            continue
        elif restart == '2':
            quit()
elif option == '2':
    quit()
    
    
    
    
        
    