from straight_flush_probability import calculate_straight_flush
from pair_probability import calculate_pair
from two_pair_probability import calculate_two_pair
from threes_probability import calculate_threes
from fours_probability import  calculate_fours
from fullhouse_probability import calculate_full_house
from flush_probability import calculate_flush
from royal_flush_probability import calculate_royal_flush
from straight_probability import calculate_straight
from card import Card

hand = [Card("spade", 6), Card("diamond", 9)]
table = list()
print('Preflop:')
print('Set Type:   Flop Odds:    Turn Odds:    River Odds:      End of game odds')
print('Pair: ',calculate_pair(hand, table, 'preflop'))
print('2 Pairs: ',calculate_two_pair(hand, table, 'preflop'))
print('3 of a kind:', calculate_threes(hand, table, 'preflop'))
print('Straight:', calculate_straight(hand, table, 'preflop'))
print('Flush:', calculate_flush(hand, table, 'preflop'))
print('Full House:', calculate_full_house(hand, table, 'preflop'))
print('4 of a Kind:', calculate_fours(hand, table, 'preflop'))
# print('Straight Flush:', calculate_straight_flush(hand, table, 'preflop'))
print('Royal Flush:', calculate_royal_flush(hand, table, 'preflop'))

table = [Card("spade", 7), Card("heart", 9), ("spade", 4)]
print('Flop:')
print('Set Type:   Flop Odds:    Turn Odds:    River Odds:      End of game odds')
print('Pair: ',calculate_pair(hand, table, 'flop'))
print('2 Pairs: ',calculate_two_pair(hand, table, 'flop'))
print('3 of a kind:', calculate_threes(hand, table, 'flop'))
print('Straight:', calculate_straight(hand, table, 'flop'))
print('Flush:', calculate_flush(hand, table, 'flop'))
print('Full House:', calculate_full_house(hand, table, 'flop'))
print('4 of a Kind:', calculate_fours(hand, table, 'flop'))
# print('Straight Flush:', calculate_straight_flush(hand, table, 'flop'))
print('Royal Flush:', calculate_royal_flush(hand, table, 'flop'))

table.append(Card("spade", 5))
print('Turn:')
print('Set Type:   Flop Odds:    Turn Odds:    River Odds:      End of game odds')
print('Pair: ',calculate_pair(hand, table, 'turn'))
print('2 Pairs: ',calculate_two_pair(hand, table, 'turn'))
print('3 of a kind:', calculate_threes(hand, table, 'turn'))
print('Straight:', calculate_straight(hand, table, 'turn'))
print('Flush:', calculate_flush(hand, table, 'turn'))
print('Full House:', calculate_full_house(hand, table, 'turn'))
print('4 of a Kind:', calculate_fours(hand, table, 'turn'))
# print('Straight Flush:', calculate_straight_flush(hand, table, 'turn'))
print('Royal Flush:', calculate_royal_flush(hand, table, 'turn'))

table.append(Card("club", 8))
print('River:')
print('Set Type:   Flop Odds:    Turn Odds:    River Odds:      End of game odds')
print('Pair: ',calculate_pair(hand, table, 'river'))
print('2 Pairs: ',calculate_two_pair(hand, table, 'river'))
print('3 of a kind:', calculate_threes(hand, table, 'river'))
print('Straight:', calculate_straight(hand, table, 'river'))
print('Flush:', calculate_flush(hand, table, 'river'))
print('Full House:', calculate_full_house(hand, table, 'river'))
print('4 of a Kind:', calculate_fours(hand, table, 'river'))
# print('Straight Flush:', calculate_straight_flush(hand, table, 'river'))
print('Royal Flush:', calculate_royal_flush(hand, table, 'river'))