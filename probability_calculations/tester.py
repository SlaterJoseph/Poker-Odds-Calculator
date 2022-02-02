import sys
sys.path.append('../poker_components')
from card import Card
from pair_probability import calculate_pair
#testing pair
hand = [Card("heart", 1), Card("heart", 2)]
table = []
print(calculate_pair(hand, table, "preflop"))
table = [Card("heart", 1), Card("heart", 4), Card("heart", 5)]
print(calculate_pair(hand, table, "flop"))
table.append(Card("heart", 5))
print(calculate_pair(hand, table, "turn"))
table.append(Card("heart", 6))
print(calculate_pair(hand, table, "river"))
