from operator import itemgetter
import os
from model.card import Card
from model.deck import Deck
from model.player import Player
from collections import defaultdict

from model.rules import Rules


class Game():
    MAX_CARDS_ON_TABLE = 5

    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.players: list[Player] = []
        self.players_in_game: list[Player] = []
        self.cards_on_table: list[Card] = []
        self.pot: int = 0

    def add_to_pot(self, amount: int) -> None:
        self.pot += amount

    def add_player(self, player: Player) -> None:
        self.players.append(player)
        self.players_in_game.append(player)

    def remove_player(self, player: Player) -> None:
        self.players.remove(player)
        self.players_in_game.remove(player)

    def set_cards_on_table(self, cards: list[Card]) -> None:
        self.cards_on_table = cards

    def show_table(self) -> str:
        return f"{self.cards_on_table}"

    def show_current_state(self, current_player: Player) -> None:
        os.system('clear')

        print(f"Your hand: {current_player.get_hand()}")
        print(f"Money: R$ {current_player.get_money()}")
        print("Cards on table:")
        print(self.show_table())

    def deal_cards(self) -> None:
        for player in self.players_in_game:
            player.add_card(self.deck.deal(), self.deck.deal())

    def flop(self) -> None:
        self.cards_on_table.extend([self.deck.deal() for _ in range(3)])

    def turn(self) -> None:
        self.cards_on_table.append(self.deck.deal())

    def river(self) -> None:
        self.cards_on_table.append(self.deck.deal())

    def process_bet(self, current_player: Player) -> None:
        amount = 0
        while True:
            try:
                amount = int(input("How much? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        bet_amount = min(amount, current_player.get_money())
        current_player.bet(bet_amount)
        self.add_to_pot(bet_amount)

        if bet_amount == current_player.get_money():
            current_player.is_all_in()

        return current_player.is_all_in()

    def collect_bets(self) -> None:
        for player in self.players_in_game:
            self.show_current_state(player)
            will_fold = input("Fold? (y/n) ")
            if will_fold == "y":
                player.fold()
                self.remove_player(player)
                continue
            self.process_bet(player)

    def play_round(self) -> None:
        self.deck.shuffle()
        self.deal_cards()
        self.collect_bets()
        self.flop()
        self.collect_bets()
        self.turn()
        self.collect_bets()
        self.river()
        self.collect_bets()
        winner = self.get_winner()
        print(f"The winner is {winner.get_name()}")

    def get_winner(self) -> Player:
        players_rank = [(player, self.evaluate_rank(player))
                        for player in self.players_in_game]
        sorted_players_rank = sorted(
            players_rank, key=itemgetter(1), reverse=True)
        return sorted_players_rank[0][0]

    def evaluate_rank(self, player: Player) -> int:
        cards_values = [card.get_value() for card in player.get_hand()]
        cards_values.extend([card.get_value() for card in self.cards_on_table])

        suits = [card.get_suit() for card in player.get_hand()]
        suits.extend([card.get_suit() for card in self.cards_on_table])

        values_by_suit = defaultdict(list)

        for suit, value in zip(suits, cards_values):
            values_by_suit[suit].append(value)

        rank = [
            10 if Rules.is_royal_flush(values_by_suit) else 0,
            9 if Rules.is_straight_flush(values_by_suit) else 0,
            8 if Rules.is_four_of_a_kind(cards_values) else 0,
            7 if Rules.is_full_house(cards_values) else 0,
            6 if Rules.is_flush(suits) else 0,
            5 if Rules.is_straight(cards_values) else 0,
            4 if Rules.is_three_of_a_kind(cards_values) else 0,
            3 if Rules.is_two_pairs(cards_values) else 0,
            2 if Rules.is_pair(cards_values) else 0,
            1 if Rules.is_high_card(cards_values) else 0
        ]

        return max(rank)

    def run(self) -> None:
        self.play_round()
