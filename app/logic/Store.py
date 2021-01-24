import random

from app.logic.Card import resource_card_starting_count, dev_card_starting_count


class Store:
    def __init__(self):
        self.resource_cards = self._load_resource_cards()
        self.dev_cards = self._load_dev_cards()
        # loop over all the dev cards type/count, create a card for each, put in list, shuffle list
        # keep a count of all resource cards in store. have methods to increment/decrement and get a dev card

    def to_private_json(self):
        return {
            "resource_cards": self.resource_cards,
            "dev_cards": self.dev_cards
        }

    def to_public_json(self):
        return {
            "resource_cards": self.resource_cards,
            "dev_cards": len(self.dev_cards)
        }

    def _load_resource_cards(self):
        cards = {}
        for card in resource_card_starting_count:
            cards[card] = resource_card_starting_count[card]

        return cards

    def _load_dev_cards(self):
        cards = []
        for card in dev_card_starting_count:
            for count in range(dev_card_starting_count[card]):
                cards.append(card)

        random.shuffle(cards)
        return cards

    def pop_dev_card(self):
        if len(self.dev_cards) > 0:
            return self.dev_cards.pop()
        return None

    def deposit(self, resource_card_type):
        if self.resource_cards[resource_card_type] + 1 <= resource_card_starting_count[resource_card_type]:
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] + 1
            return True
        return False

    def withdraw(self, resource_card_type):
        if self.resource_cards[resource_card_type] > 0:
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] - 1
            return True
        return False
