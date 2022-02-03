import sys
sys.path.append('../poker_components')
from card import Card
from pair_probability import calculate_pair
from two_pair_probability import calculate_two_pair
#testing pair
# hand = [Card("heart", 1), Card("heart", 2)]
# table = []
# print(calculate_pair(hand, table, "preflop"))
# table = [Card("heart", 1), Card("heart", 4), Card("heart", 5)]
# print(calculate_pair(hand, table, "flop"))
# table.append(Card("heart", 5))
# print(calculate_pair(hand, table, "turn"))
# table.append(Card("heart", 6))
# print(calculate_pair(hand, table, "river"))

#testing 2 pairs
hand = [Card("heart", 1), Card("heart", 2)]
table = []
print(calculate_two_pair(hand, table, "preflop"))
table = [Card("heart", 1), Card("heart", 3), Card("heart", 5)]
print(calculate_two_pair(hand, table, "flop"))
table.append(Card("heart", 6))
print(calculate_two_pair(hand, table, "turn"))
table.append(Card("heart", 7))
print(calculate_two_pair(hand, table, "river"))
