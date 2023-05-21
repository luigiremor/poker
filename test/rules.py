import unittest
from model.card import Card

from model.enum.card_value import CardValue
from model.enum.suit import Suit
from model.game import Game
from model.player import Player


class RulesEvaluator(unittest.TestCase):

    def test_is_royal_flush_true(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.ACE)
        card_2 = Card(Suit.SPADES, CardValue.KING)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.SPADES, CardValue.QUEEN),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.SPADES, CardValue.TEN),
            Card(Suit.SPADES, CardValue.NINE),
            Card(Suit.DIAMONDS, CardValue.EIGHT)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 10)

    def test_is_straight_flush_true(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.SPADES, CardValue.THREE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.SPADES, CardValue.TWO),
            Card(Suit.SPADES, CardValue.FOUR),
            Card(Suit.SPADES, CardValue.SIX),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 9)

    def test_is_four_of_a_kind(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.DIAMONDS, CardValue.FIVE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.HEARTS, CardValue.FIVE),
            Card(Suit.CLUBS, CardValue.FIVE),
            Card(Suit.SPADES, CardValue.SIX),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 8)

    def test_is_full_house(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.DIAMONDS, CardValue.FIVE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.HEARTS, CardValue.FIVE),
            Card(Suit.CLUBS, CardValue.SIX),
            Card(Suit.SPADES, CardValue.SIX),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 7)

    def test_is_flush(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.SPADES, CardValue.TWO)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.SPADES, CardValue.SIX),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.SPADES, CardValue.KING),
            Card(Suit.SPADES, CardValue.ACE),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 6)

    def test_is_straight(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.DIAMONDS, CardValue.THREE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.HEARTS, CardValue.TWO),
            Card(Suit.CLUBS, CardValue.FOUR),
            Card(Suit.SPADES, CardValue.SIX),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 5)

    def test_is_three_of_a_kind(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.DIAMONDS, CardValue.FIVE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.HEARTS, CardValue.FIVE),
            Card(Suit.CLUBS, CardValue.SIX),
            Card(Suit.SPADES, CardValue.SEVEN),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 4)

    def test_is_two_pairs(self):
        game = Game()

        player_1 = Player("Player 1", 100)

        card_1 = Card(Suit.SPADES, CardValue.FIVE)
        card_2 = Card(Suit.DIAMONDS, CardValue.FIVE)

        player_1.add_card(card_1, card_2)

        game.set_cards_on_table([
            Card(Suit.HEARTS, CardValue.SIX),
            Card(Suit.CLUBS, CardValue.SIX),
            Card(Suit.SPADES, CardValue.SEVEN),
            Card(Suit.SPADES, CardValue.JACK),
            Card(Suit.CLUBS, CardValue.KING)
        ])

        game.add_player(player_1)

        rank = game.evaluate_rank(player_1)

        self.assertTrue(rank == 3)
