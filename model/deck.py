
from model.card import Card
from model.enum.card_value import CardValue
from model.enum.suit import Suit


class Deck():

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.build()

    def __str__(self) -> str:
        return f"{self.cards}"

    def __repr__(self) -> str:
        return f"{self.cards}"

    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]

    def build(self) -> None:
        for suit in Suit:
            for value in CardValue:
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)

    def deal(self, is_visible: bool = True) -> Card:
        card = self.cards.pop()
        card.set_visible(is_visible)
        return card

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)
