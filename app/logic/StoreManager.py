class StoreManager:
    def __init__(self, store):
        self.store = store

    def deposit(self, player, resources):
        spent_resources = player.spend_resources(resources)
        self.store.deposit(spent_resources)

    def withdraw(self, player, resources):
        withdrawn_resources = self.store.withdraw(resources)
        player.earn_resources(withdrawn_resources)

    def buy_dev_card(self, player):
        card = self.store.pop_dev_card()
        if card:
            player.gain_dev_card(card)
