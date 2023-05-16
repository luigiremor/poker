
import os
from model.card import Card
from model.deck import Deck
from model.player import Player


class Game():

    def __init__(self) -> None:
        self.players: list[Player] = []
        self.deck: Deck = None
        self.cards_on_table: list[Card] = []
        self.pot: int = 0
        self.dealer_index: int = 0

    def __str__(self) -> str:
        return f"{self.players}"

    def __repr__(self) -> str:
        return f"{self.players}"

    def __len__(self) -> int:
        return len(self.players)

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def remove_player(self, player: Player) -> None:
        self.players.remove(player)

    def get_pot(self) -> int:
        return self.pot

    def set_pot(self, pot: int) -> None:
        self.pot = pot

    def add_to_pot(self, amount: int) -> None:
        self.pot += amount

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
        self.deal_cards()
        self.deal_card_on_table()

    def play_poker_round(self):
        for i in range(self.dealer_index + 1, len(self.players)+self.dealer_index):
            index_normalized = i % 5
            os.system('clear')

            print("")
            print(f"Your hand: {self.players[index_normalized].get_hand()}")
            print("")
            print(f"Money: R$ {self.players[index_normalized].get_money()}")
            print("")
            print("Cards on table:")
            print(self.show_table())
            print("")
            will_bet = input("Do you want to bet? (y/n) ")
            if will_bet == "y":
                amount = int(input("How much? "))
                if amount > self.players[index_normalized].get_money():
                    self.add_to_pot(self.players[index_normalized].get_money())
                    self.players[index_normalized].is_all_in()
                else:
                    self.players[index_normalized].bet(amount)
                    self.add_to_pot(amount)
            elif will_bet == "n":
                self.players[index_normalized].fold()
        os.system('clear')
        print(self.get_pot())
        self.dealer_index += 1
        self.deal_card_on_table()

    def get_cards_on_table(self) -> list[Card]:
        return self.cards_on_table
