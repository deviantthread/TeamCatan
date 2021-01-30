import random

from app.logic.Card import resource_card_starting_count


class Player:
    def __init__(self, name, audit_log):
        self.name = name
        self.resource_cards = self._init_resource_cards()
        self.played_dev_cards = []
        self.unplayed_dev_cards = []
        self.audit_log = audit_log
        self.victory_points = 0
        self.awards = set()

    def to_private_json(self):
        return {
            "name": self.name,
            "resource_cards": self.resource_cards,
            "played_dev_cards": self.played_dev_cards,
            "unplayed_dev_cards": self.unplayed_dev_cards,
            "victory_points": self.victory_points,
            "awards": list(self.awards)
        }

    def to_public_json(self):
        return {
            "name": self.name,
            "resource_cards": sum(self.resource_cards.values()),
            "played_dev_cards": self.played_dev_cards,
            "unplayed_dev_cards": len(self.unplayed_dev_cards),
            "victory_points": self.victory_points,
            "awards": list(self.awards)
        }

    def earn_resources(self, resources, audit=True):
        for resource_type in resources:
            self.resource_cards[resource_type] = self.resource_cards[resource_type] + resources[resource_type]

            if audit and resources[resource_type] > 0:
                self.audit_log.append("{} earned {} {}".format(self.name, resources[resource_type], resource_type))

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

    def spend_resources(self, resources, audit=True):
        spent = {}
        for resource_type in resources:
            if self.resource_cards[resource_type] >= resources[resource_type]:
                self.resource_cards[resource_type] = self.resource_cards[resource_type] - resources[resource_type]
                spent[resource_type] = resources[resource_type]

                if audit and spent[resource_type] > 0:
                    self.audit_log.append("{} spent {} {}".format(self.name, spent[resource_type], resource_type))

        return spent

    def steal_random_from_player(self, player):
        possible_cards = []
        for card in player.resource_cards:
            for i in range(player.resource_cards[card]):
                possible_cards.append(card)

        if len(possible_cards) == 0:
            return

        chosen_card = random.choice(possible_cards)
        self.earn_resources({chosen_card: 1}, False)
        player.spend_resources({chosen_card: 1}, False)

        self.audit_log.append("{} stole a card from {}".format(self.name, player.name))

    def gain_dev_card(self, dev_card):
        self.unplayed_dev_cards.append(dev_card)
        self.unplayed_dev_cards.sort()
        self.audit_log.append("{} bought a dev card".format(self.name))

    def play_dev_card(self, dev_card):
        if dev_card not in self.unplayed_dev_cards:
            return

        card = next(card for card in self.unplayed_dev_cards if card == dev_card)
        if card:
            self.unplayed_dev_cards.remove(card)
            self.played_dev_cards.append(card)
            self.played_dev_cards.sort()
            self.audit_log.append("{} played a {}".format(self.name, card))

    def _init_resource_cards(self):
        cards = {}
        for card_type in resource_card_starting_count:
            cards[card_type] = 0

        return cards

    '''
    resource_card_types is expected to be in this format
      {
        "Wheat": 1,
        "Ore": 0,
        "Wood": 0,
        "Sheep": 0,
        "Brick": 0
    }
    '''

    def send_cards_to_player(self, player, resources):
        spent = self.spend_resources(resources, audit=False)
        player.earn_resources(spent, audit=False)
        count = sum(spent.values())

        if count > 0:
            self.audit_log.append("{} sent {} {} cards".format(self.name, player.name, count))

    def gain_victory_point(self):
        self.victory_points = self.victory_points + 1
        self.audit_log.append("{} gained a victory point".format(self.name))

    def lose_victory_point(self):
        if self.victory_points > 0:
            self.victory_points = self.victory_points - 1
            self.audit_log.append("{} lost a victory point".format(self.name))
