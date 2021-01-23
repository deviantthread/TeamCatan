from app.logic.Card import ResourceCardType
import random


class Player:
    def __init__(self, name, audit_log):
        self.name = name
        self.resource_cards = self._init_resource_cards()
        self.played_dev_cards = []
        self.unplayed_dev_cards = []
        self.audit_log = audit_log
        self.victory_points = 0

    def earn_resource(self, resource_card_type, audit=True):
        self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] + 1
        if audit:
            self.audit_log.append("{} earned a {}".format(self.name, resource_card_type))

    def spend_resource(self, resource_card_type, audit=True):
        if self.resource_cards[resource_card_type] > 0:
            self.resource_cards[resource_card_type] = self.resource_cards[resource_card_type] - 1
            if audit:
                self.audit_log.append("{} spent a {}".format(self.name, resource_card_type))
            return True
        return False

    def steal_random_from_player(self, player):
        possible_cards = [card for card in player.resource_cards.keys if player.resource_cards[card] > 0]
        if len(possible_cards) == 0:
            return

        chosen_card = random.choice(possible_cards)
        self.earn_resource(chosen_card, False)
        self.spend_resource(chosen_card, False)

        self.audit_log.append("{} stole a card from {}".format(self.name, player.name))

    def gain_dev_card(self, dev_card):
        self.unplayed_dev_cards.append(dev_card)
        self.audit_log.append("{} bought a dev card".format(self.name))

    def play_dev_card(self, dev_card):
        card = next(card for card in self.unplayed_dev_cards if card.dev_card_type == dev_card.dev_card_type)
        if card:
            self.unplayed_dev_cards.remove(card)
            self.played_dev_cards.append(card)
            self.audit_log("{} played a {}".format(self.name, card.dev_card_type))

    def _init_resource_cards(self):
        cards = {}
        for card_type in ResourceCardType:
            cards[card_type] = 0

        return cards

    def send_cards_to_player(self, player, resource_card_types):
        count = 0
        for card in resource_card_types:
            if self.spend_resource(card):
                player.earn_resource(card)
                count = count + 1

        if count > 0:
            self.audit_log.append("{} sent {} {} cards".format(self.name, player.name, count))

    def gain_victory_point(self):
        self.victory_points = self.victory_points + 1
        self.audit_log.append("{} gained a victory point".format(self.name))

    def lose_victory_point(self):
        if self.victory_points > 0:
            self.victory_points = self.victory_points - 1
            self.audit_log.append("{} lost a victory point".format(self.name))