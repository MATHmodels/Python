import random
class Deck:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '0', 'J', 'Q', 'K'] # 0表示10
        suits = ['C', 'D', 'H', 'S']
        self.deck = [s+r for s in suits for r in ranks]
        random.shuffle(self.deck)
    def hand(self, n=1):
        hand = [self.deck[i] for i in range(n)]
        del self.deck[:n]
        return hand
    def deal(self, cards_per_hand, no_of_players):
        return [self.hand(cards_per_hand) \
                for i in range(no_of_players)]

    def putback(self, card):
        self.deck.append(card)

    def __str__(self):
        s = ', '.join(self.deck[  :13])+'\n'+\
            ', '.join(self.deck[13:26])+'\n'+\
            ', '.join(self.deck[26:39])+'\n'+\
            ', '.join(self.deck[39:52])
        return s
    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.deck)

if  __name__ == '__main__':
    deck = Deck()
    print(deck)
    players = deck.deal(5, 4)
    import pprint
    pprint.pprint(players)
