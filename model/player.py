
from model.card import Card


class Player():

    def __init__(self, name, money) -> None:
        self.name: str = name
        self.hand: tuple[Card, Card] = None
        self.money: int = money
        self.is_dealer: bool = False

    def __str__(self) -> str:
        return f"{self.hand}"

    def __repr__(self) -> str:
        return f"{self.hand}"

    def __len__(self) -> int:
        return len(self.hand)

    def add_card(self, card1: Card, card2: Card) -> None:
        self.hand = (card1, card2)

    def remove_card(self, card: Card) -> None:
        self.hand.remove(card)

    def get_hand(self) -> tuple[Card, Card]:
        return self.hand

    def set_hand(self, hand: tuple[Card, Card]) -> None:
        self.hand = hand

    def get_money(self) -> int:
        return self.money

    def set_money(self, money: int) -> None:
        self.money = money

    def get_is_dealer(self) -> bool:
        return self.is_dealer

    def set_is_dealer(self, is_dealer: bool) -> None:
        self.is_dealer = is_dealer

    def bet(self, amount: int) -> None:
        self.money -= amount

    def fold(self) -> None:
        self.hand = None

    def win(self, amount: int) -> None:
        self.money += amount

    def is_all_in(self) -> bool:
        return self.money == 0

    def is_folded(self) -> bool:
        return self.hand is None
