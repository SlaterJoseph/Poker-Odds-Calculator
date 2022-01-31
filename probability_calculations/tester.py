from flush_probability import calculate_flush
from threes_probability import calculate_threes
import sys
sys.path.append('../poker_components')

from card import Card

# # testing flush
# hand = [Card("spade", 1), Card("spade", 1)]
# # table = []
# # print(calculate_flush(hand, table, "preflop"))

# table = [Card("heart", 1), Card("spade", 1), Card("spade", 1)]
# print(calculate_flush(hand, table, "flop"))

# # table.append(Card("spade", 1))
# # print(calculate_flush(hand, table, "turn"))

# # table.append(Card("spade", 1))
# # print(calculate_flush(hand, table, "river"))

#testing 3 of a kind
hand = [Card("spade", 1), Card("spade", 2)]
table = []
print(calculate_threes(hand, table, "preflop"))

table = [Card("heart", 8), Card("spade", 8), Card("spade", 2)]
print(calculate_threes(hand, table, "flop"))

table.append(Card("spade", 4))
print(calculate_threes(hand, table, "turn"))

table.append(Card("spade", 1))
print(calculate_threes(hand, table, "river"))
