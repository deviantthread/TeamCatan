from enum import Enum


class Card:
    pass


class DevCard(Card):
    def __init__(self, dev_card_type):
        self.dev_card_type = dev_card_type


class DevCardType(Enum):
    Knight = 1
    VictoryPoint = 2
    YearOfPlenty = 3
    Monopoly = 4
    RoadBuilding = 5

    @staticmethod
    def _details():
        return {
            DevCardType.Knight: [14,
                                 "Move the robber. Steal 1 resource card from the owner of an adjacent settlement or city."],
            DevCardType.VictoryPoint: [5, "1 Victory Point!"],
            DevCardType.YearOfPlenty: [2,
                                       "Take any 2 resources from the bank. Add them to your hand. They can be 2 of the same "
                                       "resource or 2 different resources."],
            DevCardType.Monopoly: [2,
                                   "When you play this card, announce 1 type of resource. All other players must give you their "
                                   "resource cards of that type."],
            DevCardType.RoadBuilding: [2, "Place 2 new roads as if you had just built them."]
        }

    def get_starting_count(self):
        return DevCardType._details()[self][0]

    def get_desc(self):
        return DevCardType._details[self][1]


class ResourceCardType(Enum):
    Wheat = 1
    Ore = 2
    Wood = 3
    Sheep = 4
    Brick = 5

    def get_starting_count(self):
        return 19

