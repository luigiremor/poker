
import os
from model.card import Card
from model.deck import Deck
from model.player import Player


class Game():
    MAX_CARDS_ON_TABLE = 5

    def __init__(self) -> None:
        self.deck: Deck = None
        self.players: list[Player] = []
        self.players_in_game: list[Player] = []
        self.dealer_index: int = 0
        self.cards_on_table: list[Card] = []
        self.pot: int = 0

    def __str__(self) -> str:
        return f"{self.players}"

    def __repr__(self) -> str:
        return f"{self.players}"

    def __len__(self) -> int:
        return len(self.players)

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def remove_player(self, player: Player) -> None:
        if player in self.players:
            self.players.remove(player)
        else:
            raise ValueError("Player not found in the game.")

    def get_pot(self) -> int:
        return self.pot

    def set_pot(self, pot: int) -> None:
        self.pot = pot

    def add_to_pot(self, amount: int) -> None:
        self.pot += amount

    def get_players_in_game(self) -> list[Player]:
        return self.players_in_game

    def set_players_in_game(self, players: list[Player]) -> None:
        self.players_in_game = players

    def init_deck(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

    def deal_cards(self) -> None:
        for player in self.players:
            player.add_card(self.deck.deal(), self.deck.deal())

    def deal_card_on_table(self) -> None:
        if len(self.cards_on_table) < 4:
            for _ in range(3):
                self.cards_on_table.append(self.deck.deal(is_visible=False))
        else:
            self.cards_on_table.append(self.deck.deal())

    def show_table(self) -> list[Card]:
        return f"{self.cards_on_table}"

    def show_player_hand(player: Player) -> tuple[Card, Card]:
        return f"{player.get_hand()}"

    def setup(self):
        self.init_deck()
        self.players[self.dealer_index].set_is_dealer(True)
        self.set_players_in_game(self.players)
        self.deal_cards()
        self.deal_card_on_table()

    def show_current_state(self, current_player: Player) -> None:
        os.system('clear')

        print(f"Your hand: {current_player.get_hand()}")
        print(f"Money: R$ {current_player.get_money()}")
        print("Cards on table:")
        print(self.show_table())

    def ask_for_bet(self):
        return input("Do you want to bet? (y/n) ")

    def process_bet(self, current_player):
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

    def run(self):
        self.setup()

        while len(self.get_players_in_game()) > 1 and len(self.cards_on_table) < self.MAX_CARDS_ON_TABLE:
            num_players = len(self.players_in_game)

            for i in range(num_players):
                current_player = self.players_in_game[(
                    self.dealer_index + i + 1) % num_players]

                if current_player.is_folded() or current_player.get_money() <= 0:
                    continue

                self.show_current_state(current_player)

                print(self.players_in_game)
                will_bet = self.ask_for_bet()
                if will_bet.lower() == "y":
                    self.process_bet(current_player)
                elif will_bet.lower() == "n":
                    current_player.fold()

            # Remove players who have no money left or have folded
            players_last_round: list[Player] = self.players_in_game.copy()
            self.players_in_game = [
                player for player in players_last_round if not player.is_folded() and player.get_money() > 0]

            # If only one player is left, break the loop
            if len(self.get_players_in_game()) <= 1:
                break

            self.dealer_index = (self.dealer_index + 1) % num_players
            self.players[self.dealer_index].set_is_dealer(True)

            if len(self.cards_on_table) < self.MAX_CARDS_ON_TABLE:
                self.deal_card_on_table()

    def get_cards_on_table(self) -> list[Card]:
        return self.cards_on_table
