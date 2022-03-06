from card import Card
from pair_probability import calculate_pair
from two_pair_probability import calculate_two_pair
from threes_probability import calculate_threes
from fours_probability import  calculate_fours
from fullhouse_probability import calculate_full_house
from flush_probability import calculate_flush
from royal_flush_probability import calculate_royal_flush
from straight_probability import flop, turn, river

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
# hand = [Card("heart", 1), Card("heart", 2)]
# table = []
# print(calculate_two_pair(hand, table, "preflop"))
# table = [Card("heart", 1), Card("heart", 3), Card("heart", 5)]
# print(calculate_two_pair(hand, table, "flop"))
# table.append(Card("heart", 6))
# print(calculate_two_pair(hand, table, "turn"))
# table.append(Card("heart", 7))
# print(calculate_two_pair(hand, table, "river"))

#testing 3s
# hand = [Card("heart", 1), Card("heart", 1)]
# table = []
# print(calculate_threes(hand, table, "preflop"))
# table = [Card("heart", 2), Card("heart", 3), Card("heart", 3)]
# print(calculate_threes(hand, table, "flop"))
# table.append(Card("heart", 1))
# print(calculate_threes(hand, table, "turn"))
# table.append(Card("heart", 2))
# print(calculate_threes(hand, table, "river"))

#testing 4s
# hand = [Card("heart", 1), Card("heart", 2)]
# table = []
# print(calculate_fours(hand, table, "preflop"))
# table = [Card("heart", 2), Card("heart", 1), Card("heart", 2)]
# print(calculate_fours(hand, table, "flop"))
# table.append(Card("heart", 3))
# print(calculate_fours(hand, table, "turn"))
# table.append(Card("heart", 1))
# print(calculate_fours(hand, table, "river"))

#testing full house
# hand = [Card("heart", 1), Card("heart", 1)]
# table = []
# print(calculate_full_house(hand, table, "preflop"))
# table = [Card("heart", 1), Card("heart", 2), Card("heart", 3)]
# print(calculate_full_house(hand, table, "flop"))
# table.append(Card("heart", 1))
# print(calculate_full_house(hand, table, "turn"))
# table.append(Card("heart", 2))
# print(calculate_full_house(hand, table, "river"))

#testing flush 
# hand = [Card("heart", 1), Card("spade", 1)]
# table = []
# print(calculate_flush(hand, table, "preflop"))
# table = [Card("spade", 1), Card("spade", 2), Card("spade", 3)]
# print(calculate_flush(hand, table, "flop"))
# table.append(Card("diamond", 1))
# print(calculate_flush(hand, table, "turn"))
# table.append(Card("spade", 2))
# print(calculate_flush(hand, table, "river"))

#testing royal flush
# hand = [Card("heart", 10), Card("spade", 11)]
# table = []
# print(calculate_royal_flush(hand, table, "preflop"))
# table = [Card("heart", 1), Card("spade", 12), Card("heart", 13)]
# print(calculate_royal_flush(hand, table, "flop"))
# table.append(Card("heart", 1))
# print(calculate_royal_flush(hand, table, "turn"))
# table.append(Card("heart", 1))
# print(calculate_royal_flush(hand, table, "river"))

#flush testing
# Debugging straight_helper -> flop
# for x in range(14):
#     for y in range(14):
#         if x == 0 or y == 0:
#             continue
#         hand = [Card('heart', x), Card('spade', y)]
#         print('x: ',x, " y: ",y, " ",flop_helper(hand))

hand = [Card("heart", 6), Card("heart", 7)]
print(flop(hand))
print(turn(hand))
print(river(hand))