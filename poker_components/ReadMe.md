# Poker Components

This package contains all the parts of the raw poker game. Each module is detailed below, explaining the use of the module 
and any methods contained in it.

It include:
    - card
    - deck
    - player
    - dealer
    - table

## card
    The card module is simple, only containing a Card class with suit and rank variables , along with getters for the suit 
    and rank

## deck
    The deck module is comprised of a Deck class. It has a method (build_deck) to build a deck (a list of cards), 
    assigning the proper variables to each card. It has a shuffle method (shuffle_deck), which clears the deck then runs 
    the build_deck method. It also contains a getter for the deck.

## player
    The player module is comprised of a Player class. It has variables for the player's hand (2 personal cards), their name,
    and if they are the player in focus. It has a getter for all the variables, and a setter for just the focus variable.

## dealer
    The dealer module is comprised of a Dealer class. It consists of a few methods which will be explained below. It also
    initializes it's own deck to be used for the game, and has a getter for the deck.
    - random_number - Generates a random number from 0 - Remaining cards in the deck
    - burn_card - Uses random_number to get a random index from the deck, then removes it from the deck
    - draw_card - Uses random_number to get a random index from the deck, removes the card and returns it for future used
    - deal_player - Calls draw_card twice, putting both cards in a list and returning it for a player to use as it's hand
    - deal_flop - Calls burn_card, then draw_card three times, placing those cards in a list and returning it for the flop
    - deal_turn_river - Calls burn_card, then draw_card, returning the card to be used in the turn or river 
    - shuffle_deck - Calls the deck's shuffle deck method

## table
    The table module is comprised of a Table class. This module is essentially where everything combnies to form the game.
    It initializes a dealer, as well has a player list(player_list) and community card list(cards_in_play).
    The Table class' methods will be detailed below.
    - add_player - Takes a name, calls the dealer's deal_player method, then intialzies a player with that name and hand
    and adds them to the player_list. If it is the first player is also sets them as focusable.
    - play_hand - This method is where the game is played. First it takes a input of amount of players, followed by their
    names, and calls add_player to add them to the player list. Next it calls for a flop from the dealer's deal_flop method
    adding the list of cards to the community cards list. Next it does the same for the turn and river, adding their cards
    to the list.
    - reset_round - Clears the player_list, has the dealer shuffle the deck through his shuffle_deck method, and calls
    play_hand
    - find_selected_player - Loops through the player list and returns the one focused
    - return_cards - returns a list of the focused player's hand and the community cards