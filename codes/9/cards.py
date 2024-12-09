import random
def make_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '0', 'J', 'Q', 'K'] # 0表示10
    suits = ['C', 'D', 'H', 'S'] # ['梅','方','红','黑']
    deck = [s+r for s in suits for r in ranks]
    random.shuffle(deck)
    return deck

def deal_hand(n, deck):
    hand = [deck[i] for i in range(n)]
    del deck[:n]
    return hand, deck

def deal(cards_per_hand, no_of_players):
    deck = make_deck()
    hands = []
    for i in range(no_of_players):
        hand, deck = deal_hand(cards_per_hand, deck)
        hands.append(hand)
    return hands

def same_rank(hand, n_of_a_kind):
    # 给定一手牌，返回具有指定张数相同牌面的数量
    ranks = [card[1:] for card in hand]
    counter = 0
    for rank in set(ranks):
        if ranks.count(rank) == n_of_a_kind:
            counter += 1
    return counter

def same_suit(hand):
    # 给定一手牌，返回手牌中每种花色的牌的数量
    suits = [card[0] for card in hand]
    counter = {}      # counter[suit] 存放suit花色的数量
    for suit in suits:
        count = suits.count(suit)
        if count > 1: # 只记录同种花色数量大于1的
            counter[suit] = count
    return counter

if __name__ == '__main__':
    random.seed(43)
    players = deal(5, 4)
    import pprint; pprint.pprint(players)

    for hand in players:
        print('手牌 %s\n    有%d个对, %s个三条，%4s张同花色\n' % \
        (', '.join(hand), same_rank(hand,2), same_rank(hand,3),
         '+'.join([str(s) for s in same_suit(hand).values()])))
