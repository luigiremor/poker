# Poker Game

## Overview

This project is a Python implementation of the classic card game, Poker. It supports multiple players in the same console and implements the standard rules. The goal of the game is to obtain the highest-ranking hand at the end of the betting rounds.

## Classes

- Player: A class that represents a player in the game, holding their current hand.
- Deck: A class that represents the deck of cards used in the game.
- Card: A class that represent the cards used in the game, having suits and its values.
- Game: This is the main class that drives the game, handling player turns and evaluating hands.
- Rules: A class that contains the logic for evaluating poker hands based on standard poker rules.

## Rules applied

The following are the poker hand ranks evaluated by this implementation, ordered from highest (10) to lowest (1):

- [X] **Royal Flush (10):** A hand that includes A, K, Q, J, 10, all in the same suit.
- [X] **Straight Flush (9):** Any straight with all five cards of the same suit.
- [X] **Four of a Kind (8):** All four cards of the same rank.
- [X] **Full House (7):** Three of a kind with a pair.
- [X] **Flush (6):** Any five cards of the same suit, not in sequence.
- [X] **Straight (5):** Any five consecutive cards of different suits.
- [X] **Three of a Kind (4):** Three cards of the same rank.
- [X] **Two Pairs (3):** Two different pairs.
- [X] **Pair (2):** Two cards of the same rank.
- [X] **High Card (1):** When you haven't made any of the hands above, the highest card plays.

## Features

Those are the current features implemented

- [X] Round
- [X] Bet
- [X] Fold
- [X] Winning evaluation
- [ ] Dealer
- [ ] Auto-increase bet value
- [ ] LAN Multiplayer
- [ ] Non-CLI interface

## Running the Game

You need Python3 to run it. To start it just use the following command in the root of project:

```
python3 -m main.py
```
You can also run tests for this project

```
python3 -m unittest ./test/rules.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT

