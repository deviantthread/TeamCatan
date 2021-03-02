import random


class Dice:
    def __init__(self, audit_log, store_manager):
        self.current_roll = 0
        self.current_roll_view = []
        self.audit_log = audit_log
        self.store_manager = store_manager
        self.resource_mapping = {}
        self.dice_cards = []
        self._init_dice_cards()

    def _init_dice_cards(self):
        permutations = []
        for a in range(1, 7):
            for b in range(1, 7):
                permutations.append([a, b])

        self.dice_cards = []

        # 10 decks of cards
        for i in range(10):
            self.dice_cards.extend(permutations.copy())

        random.shuffle(self.dice_cards)

    def roll_dice(self, game):
        if len(self.dice_cards) == 0:
            self._init_dice_cards()

        a, b = self.dice_cards.pop()
        self.current_roll = a + b
        current_roll_audit_log = "{} ({} + {})".format(self.current_roll, a, b)
        self.audit_log.append("Dice rolled " + current_roll_audit_log)
        self._withdraw_from_store(self.current_roll, game)
        self.current_roll_view = [a, b]
        return self.current_roll_view

    def last_roll(self):
        return self.current_roll_view

    # dice roll -> player -> resource -> count
    # resources is the common resources map eg {'Wheat': 2}
    def update_mapping(self, player_name, dice_roll, resources):
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
