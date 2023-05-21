
from collections import Counter


class Rules:

    @staticmethod
    def is_royal_flush(values_by_suit: dict) -> bool:
        for suit, values in values_by_suit.items():
            if len(values) < 5:
                continue

            values_list = sorted([value.value for value in values])

            if values_list[-5:] == [10, 11, 12, 13, 14]:
                return True

        return False

    @staticmethod
    def is_straight_flush(values_by_suit: dict) -> bool:
        for suit, values in values_by_suit.items():
            if len(values) < 5:
                continue

            values_list = sorted([value.value for value in values])

            for i in range(len(values_list) - 4):
                if values_list[i:i+5] == list(range(values_list[i], values_list[i] + 5)):
                    return True

        return False

    @staticmethod
    def is_four_of_a_kind(cards_values: list) -> bool:
        number_of_cards_by_value = Counter(cards_values)
        return 4 in number_of_cards_by_value.values()

    @staticmethod
    def is_full_house(cards_values: list) -> bool:
        number_of_cards_by_value = Counter(cards_values)
        return 3 in number_of_cards_by_value.values() and 2 in number_of_cards_by_value.values()

    @staticmethod
    def is_flush(suits: list) -> bool:
        number_of_cards_by_suit = Counter(suits)
        return 5 in number_of_cards_by_suit.values() or 6 in number_of_cards_by_suit.values() or 7 in number_of_cards_by_suit.values()

    @staticmethod
    def is_straight(cards_values: list) -> bool:
        values_list = sorted([value.value for value in cards_values])

        for i in range(len(values_list) - 4):
            if values_list[i:i+5] == list(range(values_list[i], values_list[i] + 5)):
                return True

        return False

    @staticmethod
    def is_three_of_a_kind(cards_values: list) -> bool:
        number_of_cards_by_value = Counter(cards_values)
        return 3 in number_of_cards_by_value.values()

    @staticmethod
    def is_two_pairs(cards_values: list) -> bool:
        number_of_cards_by_value = Counter(cards_values)
        return list(number_of_cards_by_value.values()).count(2) == 2

    @staticmethod
    def is_pair(cards_values: list) -> bool:
        number_of_cards_by_value = Counter(cards_values)
        return 2 in number_of_cards_by_value.values()

    @staticmethod
    def is_high_card(cards_values: list) -> bool:
        return True
