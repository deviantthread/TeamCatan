from app.logic.AuditLog import AuditLog
from app.logic.Dice import Dice
from app.logic.Player import Player
from app.logic.Store import Store
from app.logic.StoreManager import StoreManager


class Game:
    def __init__(self):
        self.store = Store()
        self.players = {}
        self.audit_log = AuditLog()
        self.store_manager = StoreManager(self.store)
        self.dice = Dice(self.audit_log, self.store_manager)

    def reset_game(self):
        self.store = Store()
        self.players = {}
        self.audit_log = AuditLog()
        self.store_manager = StoreManager(self.store)
        self.dice = Dice(self.audit_log, self.store_manager)

    def add_player(self, player_name):
        if player_name.lower() not in self.players:
            self.players[player_name.lower()] = Player(player_name, self.audit_log)

    def get_player(self, player_name):
        return self.players[player_name.lower()]
