from app.logic.AuditLog import AuditLog
from app.logic.Store import Store


class Game:
    def __init__(self):
        self.store = None
        self.players = []
        self.staging = False
        self.audit_log = None
        self.temp_var = 1

    def start_staging(self):
        self.staging = True
        self.players = []

    def add_player(self, player):
        if self.staging:
            self.players.append(player)

    def start_game(self):
        self.staging = False
        self.store = Store()
        self.audit_log = AuditLog()

