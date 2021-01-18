from Store import Store
from AuditLog import AuditLog


class Game:
    def __init__(self):
        self.store = None
        self.players = []
        self.staging = False
        self.audit_log = None

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

