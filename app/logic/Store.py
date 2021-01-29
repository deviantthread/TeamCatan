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

    '''
    resources is in the following format
        {
            "Wheat": 1,
            "Ore": 0,
            "Wood": 0,
            "Sheep": 0,
            "Brick": 0
        }
    '''

    def deposit(self, resources):
        for resource_type in resources:
            if self.resource_cards[resource_type] + resources[resource_type] <= \
                    resource_card_starting_count[resource_type]:
                self.resource_cards[resource_type] = self.resource_cards[resource_type] + resources[resource_type]

    def withdraw(self, resources):
        withdrawn_resources = {}

        for resource_type in resources:
            if self.resource_cards[resource_type] >= resources[resource_type]:
                self.resource_cards[resource_type] = self.resource_cards[resource_type] - resources[resource_type]
                withdrawn_resources[resource_type] = resources[resource_type]

        return withdrawn_resources
