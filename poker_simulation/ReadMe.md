# Poker Simulation

This portion of the project was something I created on the side.

Essentially, this package is for simulating poker games. The while loop in simulation decides how many times
to simulate poker round. It opens the data file(which is currently empty) and writes down the __str__ method
from the table class, which looks something like this

Spade:3$Heart:2$  -> Player 1 hand
Spade:1$Heart:9$ -> Player 2 hand
Spade:8$Diamond:2$ -> Player 3 hand
Club:12$Club 10:2$ -> Player 4 hand
Club:3$Spade:2$Diamond:13$Heart:12$Spade:13$ -> Community/Table cards

It writes text formatted as such as x amount of times. You can look in old data.txt for an example

Next data_collection splits these lines twice, first by $ (representing a separation of cards) then by : (representing a
separation of suit:rank/value). These lists are stored in variables and then head to data_processing. data_processing
checks what's the best hand a group of cards can make, then returns a number based on it, with the best hand(Royal Flush)
being a 9 and the worst hand(High Card) being a 0. This is done 16 times per block of text, 4 players over 4 rounds. First,
just the player's hand is checked, then with the flop, then with the flop and turn, and finally the flop, turn and
river. 

The number returned is used as an index in data from data_collection. data is a list of lists, with the base list
having a size of 4 (one for each round), and the inner lists having a size of 10 (one for each card). The returned number
is used as an index, along with the current turn(which is tracked in data_collection). The spot given from the
[turn][hand value] index is incremented by one. Finally, once all the processing is done, the collection prints the 4
lists. The first one is preflop, then flop, and so on. It shows how many times a player had a certain hand by a certain 
round.

I ran this with a bunch of different-sized groups of data, the largest being 10 million. I was curious if my code was 
actually correct, and I know if you test something many times it should regress to the mean. After running my 10 million
cases (which the text in old data.txt is a snippet of) I saw all of my percentages of getting a specific hand
were nearly identical to the percentages I found online. For example, the odds of getting a pocket pair is 0.0588. My 
test gave me a result of .0588 as well. 

As of right now, there is no way to run this code in the program. I intend to eventually make it accessible, however, it does
take significant time to run massive groups of data (my 10 million cases took a hour and a half), so I may implement a cap
to the number of cases. 
