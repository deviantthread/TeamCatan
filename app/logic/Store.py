import random

from app.logic.Card import ResourceCardType, DevCardType, DevCard


class Store:
    def __init__(self):
        self.resource_cards = self._load_resource_cards()
        self.dev_cards = self._load_dev_cards()
        # loop over all the dev cards type/count, create a card for each, put in list, shuffle list
        # keep a count of all resource cards in store. have methods to increment/decrement and get a dev card

    def _load_resource_cards(self):
        cards = {}
        for card in ResourceCardType:
            cards[card] = card.get_starting_count()

        return cards

    def _load_dev_cards(self):
        cards = []
        for card in DevCardType:
            for count in card.get_starting_count():
                cards.append(DevCard(card))

        random.shuffle(cards)
        return cards

    def pop_dev_card(self):
        if len(self.dev_cards) > 0:
            return self.dev_cards.pop()

    def deposit(self, resource_card_type):
        if self.resource_cards[resource_card_type] + 1 <= resource_card_type.get_starting_count():
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] + 1
            return True
        return False

    def withdraw(self, resource_card_type):
        if self.resource_cards[resource_card_type] > 0:
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] - 1
            return True
        return False