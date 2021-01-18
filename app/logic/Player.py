from app.logic.Card import ResourceCardType


class Player:
    def __init__(self, name):
        self.name = name
        self.resource_cards = self._init_resource_cards()
        self.played_dev_cards = []
        self.unplayed_dev_cards = []

    def earn(self, resource_card_type):
        self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] + 1

    def spend(self, resource_card_type):
        if self.resource_cards[resource_card_type] > 0:
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] - 1
            return True
        return False

    def play_dev_card(self, dev_card):
        card = next(card for card in self.unplayed_dev_cards if card.dev_card_type == dev_card.dev_card_type)
        if card:
            self.unplayed_dev_cards.remove(card)
            self.played_dev_cards.append(card)

    def _init_resource_cards(self):
        cards = {}
        for card_type in ResourceCardType:
            cards[card_type] = 0

        return cards

    def send_card_to_player(self, player, resource_card_type):
        if self.spend(resource_card_type):
            player.earn(resource_card_type)
