from app.logic.AuditLog import AuditLog
from app.logic.Player import Player
from app.logic.Store import Store


class Game:
    def __init__(self):
        self.store = None
        self.players = {}
        self.staging = False
        self.audit_log = None

    def start_staging(self):
        self.staging = True
        self.players = {}
        self.store = None
        self.audit_log = AuditLog()

    def add_player(self, player_name):
        if self.staging and player_name not in self.players:
            self.players[player_name] = Player(player_name, self.audit_log)

    def start_game(self):
        self.staging = False
        self.store = Store()

