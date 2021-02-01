import random


class Dice:
    def __init__(self, audit_log, store_manager):
        self.current_roll = 0
        self.audit_log = audit_log
        self.store_manager = store_manager
        self.resource_mapping = {}

    def roll_dice(self, game):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        self.current_roll = a + b
        self.audit_log.append("Dice rolled {} ({} + {})".format(self.current_roll, a, b))
        self._withdraw_from_store(self.current_roll, game)
        return self.current_roll

    def last_roll(self):
        return self.current_roll

    # dice roll -> player -> resource -> count
    # resources is the common resources map eg {'Wheat': 2}
    def update_mapping(self, player_name, dice_roll, resources):
        print("updating mapping")
        player_name = player_name.lower()
        if dice_roll not in self.resource_mapping:
            self.resource_mapping[dice_roll] = {}

        self.resource_mapping[dice_roll][player_name] = resources

    def _withdraw_from_store(self, dice_roll, game):
        if dice_roll not in self.resource_mapping:
            return

        player_names = self.resource_mapping[dice_roll]
        for player_name, resources in player_names.items():
            self.store_manager.withdraw(game.get_player(player_name), resources)
