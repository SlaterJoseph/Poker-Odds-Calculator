# Poker Probability Calculator

It is based on the variant Texas Hold 'em, and if you are unfamiliar with the rules go to the Rules Of Texas Hold 'em 
file. I'd suggest breifly reading it anyway just to refresh youself on the terms of poker, as well as learning my terms
(I believe I primarily used the common terms but just to double check)

Each package has it's own ReadMe further explaining that packages use in the program.

## How It Works

As of now, this project randomly deals a chosen amount of players cards, then calculate the probability of
that starting hand ending with different hands. In the future I want to implement a setting to select cards, 
and a setting to swap between players to see all of their odds of different hands. 

If you only have your two cards avialable, it will calculate your odds of getting a hand by the end of the flop, turn
and river, then a final total of getting a set by the end of the round. It repeats this process when the flop is revealed,
calculating the probability of getting sets by the turn using the flop, and calculating the probability of getting a set 
by the river, using the flop, and assuming you did not get the set by the turn. So, if you do not have a pair and the flop
is out, the river calculation will assume you did not get a pair on the turn. It then repeats this one more time once the
turn is revealed, calculating the probability for the river using all of the cards. Finally the program checks if you did 
indeed get the hand, returning a 100 if you did and 0 if you did not.

## Probability Mathematics
The math behind all the probability calculations can be found [here](https://docs.google.com/document/d/1szqOczJywvRkg0WPcQOf7wx_OYCvQWnpwpCjL35v0sE/edit?usp=sharing). After any line of code with a probability, 
is a name and number, which you lookup in the document. So for Flush - 1, click Flush 1 on the side bar and 
it will bring you to a detailed explanation. 

Some of the probabilities found here are higher then numbers found online. This is because I am counting community
hands. So, generally the odds of flopping a pair is approximitly 32% according to resources online, however this does not 
account for if the flop itself contains a pair. That increases the total to approximitly 38%. I am also including hands
which contain other hands. For instance, if you have a four of a kind, you also have a pair and three of a kind, as both
are included in a four of a kind. 

However, this does some weird things to the total probability for some calculations. For instance, according to my 
definition of a getting a pair, you have a 38% chance of getting a pair on the flop, assuming you did not get a pair on
the flop you have a 32% chance of getting a pair on the turn, and 39% chance of getting a pair on the river. That total is 
greater then 100%, which does not make sense, as some games you will not get a pair, and the probability cannor be greater 
then 100%. 