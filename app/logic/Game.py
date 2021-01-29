from app.logic.AuditLog import AuditLog
from app.logic.Player import Player
from app.logic.Store import Store


class Game:
    def __init__(self):
        self.store = Store()
        self.players = {}
        self.audit_log = AuditLog()

    def reset_game(self):
        self.store = Store()
        self.players = {}
        self.audit_log = AuditLog()

    def add_player(self, player_name):
        if player_name.lower() not in self.players:
            self.players[player_name.lower()] = Player(player_name, self.audit_log)

    def get_player(self, player_name):
        return self.players[player_name.lower()]
