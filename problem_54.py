from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Card:
    value: str
    suit: str


VALUE_TO_INT = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def get_poker_rank(cards: list[Card]) -> tuple:
    """Get the poker rank of the given hand"""
    if _is_royal_flush(cards):
        return 10, 0
    if v := _is_straight_flush(cards):
        return 9, v
    if v := _is_four_of_a_kind(cards):
        return 8, v
    if pairs := _is_full_house(cards):
        return 7, pairs[0], pairs[1]
    if _is_flush(cards):
        return 6, _get_highest_value_card(cards)
    if v := _is_straight(cards):
        return 5, v
    if v := _is_three_of_a_kind(cards):
        return 4, v
    if pairs := _is_two_pairs(cards):
        return 3, pairs[0], pairs[1]
    if pair_value := _is_one_pair(cards):
        return 2, pair_value
    return 1, _get_highest_value_card(cards)


def _is_one_pair(cards: list[Card]) -> int | None:
    """Check if the hand has one pair"""
    d = defaultdict(int)
    for card in cards:
        d[card.value] += 1
    if 2 not in d.values():
        return None
    return max([VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 2])


def _is_two_pairs(cards: list[Card]) -> tuple[int, int] | None:
    """Check if the hand has two pairs"""
    d = defaultdict(int)
    for card in cards:
        d[card.value] += 1
    if len([v for v in d.values() if v == 2]) != 2:
        return None

    pairs = [VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 2]
    return max(pairs), min(pairs)


def _is_three_of_a_kind(cards: list[Card]) -> int | None:
    """Check if the hand has three of a kind"""
    d = defaultdict(int)
    for card in cards:
        d[card.value] += 1

    if 3 not in d.values():
        return None

    return max([VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 3])


def _is_straight(cards: list[Card]) -> int | None:
    """Check if the hand has a straight"""
    if len(set([card.value for card in cards])) != 5:
        return False

    if set([card.value for card in cards]) == {"2", "3", "4", "5", "A"}:
        return 5

    values = sorted([VALUE_TO_INT.get(card.value) for card in cards])
    if not all(values[i] == values[i - 1] + 1 for i in range(1, 5)):
        return None

    return max(values)


def _is_flush(cards: list[Card]) -> bool:
    """Check if the hand has a flush"""
    return len(set([card.suit for card in cards])) == 1


def _is_full_house(cards: list[Card]) -> tuple[int, int] | None:
    """Check if the hand has a full house"""
    d = defaultdict(int)
    for card in cards:
        d[card.value] += 1

    if 3 not in d.values() or 2 not in d.values():
        return None

    three_of_a_kind = max([VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 3])
    pair = max([VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 2])
    return three_of_a_kind, pair


def _is_four_of_a_kind(cards: list[Card]) -> int | None:
    """Check if the hand has four of a kind"""
    d = defaultdict(int)
    for card in cards:
        d[card.value] += 1

    if 4 not in d.values():
        return None

    return max([VALUE_TO_INT.get(card.value) for card in cards if d[card.value] == 4])


def _is_straight_flush(cards: list[Card]) -> int | None:
    """Check if the hand has a straight flush"""
    if not _is_flush(cards):
        return None

    return _is_straight(cards)


def _is_royal_flush(cards: list[Card]) -> bool:
    """Check if the hand has a royal flush"""
    return _is_flush(cards) and _is_straight(cards) and all(card.value in {"10", "J", "Q", "K", "A"} for card in cards)


def _get_highest_value_card(cards: list[Card]) -> int:
    """Get the highest value card in the hand"""
    return max(VALUE_TO_INT.get(card.value) for card in cards)


with open('0054_poker.txt') as f:
    games = [line.rstrip() for line in f]

total = 0
for game in games:
    player_1_hand, player_2_hand = game.split(" ")[:5], game.split(" ")[5:]
    player_1_cards = [Card(value=card[0], suit=card[1]) for card in player_1_hand]
    player_2_cards = [Card(value=card[0], suit=card[1]) for card in player_2_hand]
    if get_poker_rank(player_1_cards) > get_poker_rank(player_2_cards):
        total += 1

print(total)
