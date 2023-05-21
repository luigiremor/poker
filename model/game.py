import os
from model.card import Card
from model.deck import Deck
from model.player import Player
from collections import Counter


class Game():
    MAX_CARDS_ON_TABLE = 5

    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.players: list[Player] = []
        self.players_in_game: list[Player] = []
        self.dealer_index: int = 0
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

    def evaluate_rank(self, player: Player) -> int:
        values = [card.get_value().value for card in player.get_hand()]
        values.extend([card.get_value().value for card in self.cards_on_table])
        values.sort(reverse=True)

        suits = [card.get_suit().value for card in player.get_hand()]
        suits.extend([card.get_suit().value for card in self.cards_on_table])
        suits.sort(reverse=True)

        ranks = [
            (10, values[:5]) if self.is_royal_flush(values, suits) else
            (9, values[:5]) if self.is_straight_flush(values, suits) else
            (8, values[:5]) if self.is_four_of_a_kind(values) else
            (7, values[:5]) if self.is_full_house(values) else
            (6, values[:5]) if self.is_flush(suits) else
            (5, values[:5]) if self.is_straight(values) else
            (4, values[:5]) if self.is_three_of_a_kind(values) else
            (3, values[:5]) if self.is_two_pair(values) else
            (2, values[:5]) if self.is_pair(values) else
            (1, values[:5])
        ]

        return max(ranks)

    def is_royal_flush(self, values: list[int], suits: list[int]) -> bool:
        return self.is_straight_flush(sorted(values), suits) and max(values) == 14

    def is_straight_flush(self, values: list[int], suits: list[int]) -> bool:
        return self.is_flush(suits) and self.is_straight(values)

    def is_four_of_a_kind(self, values: list[int]) -> bool:
        value_counts = Counter(values)
        return 4 in value_counts.values()

    def is_full_house(self, values: list[int]) -> bool:
        value_counts = Counter(values)
        return set(value_counts.values()) == {2, 3}

    def is_flush(self, suits: list[int]) -> bool:
        suits_count = Counter(suits)
        return max(suits_count.values()) >= 5

    def is_straight(self, values: list[int]) -> bool:
        sorted_values = sorted(values)
        for i in range(len(sorted_values) - 4):
            if sorted_values[i:i+5] == list(range(sorted_values[i], sorted_values[i] + 5)):
                return True
        # Special case for Ace to 5 straight
        if sorted_values[:4] == [2, 3, 4, 5] and 14 in sorted_values:
            return True
        return False

    def is_three_of_a_kind(self, values: list[int]) -> bool:
        value_counts = Counter(values)
        return 3 in value_counts.values()

    def is_two_pair(self, values: list[int]) -> bool:
        value_counts = Counter(values)
        return list(value_counts.values()).count(2) >= 2

    def is_pair(self, values: list[int]) -> bool:
        value_counts = Counter(values)
        return 2 in value_counts.values()

    def run(self) -> None:
        self.play_round()
