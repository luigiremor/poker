
from model.enum.card_value import CardValue
from model.enum.suit import Suit


class Card():

    def __init__(self, suit: Suit, value: CardValue) -> None:
        self.suit = suit
        self.value = value
        self.is_visible: bool = False

    def __str__(self) -> str:
        return f"{self.value.name} of {self.suit.name}"

    def __repr__(self) -> str:
        return f"{self.value.name} of {self.suit.name}"

    def __eq__(self, other) -> bool:
        return self.suit == other.suit and self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value.value < other.value.value

    def __gt__(self, other) -> bool:
        return self.value.value > other.value.value

    def get_suit(self) -> Suit:
        return self.suit

    def get_value(self) -> CardValue:
        return self.value

    def set_suit(self, suit: Suit) -> None:
        self.suit = suit

    def set_value(self, value: CardValue) -> None:
        self.value = value

    def is_visible(self) -> bool:
        return self.is_visible

    def set_visible(self, is_visible: bool) -> None:
        self.is_visible = is_visible
