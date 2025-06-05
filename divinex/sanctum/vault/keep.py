# vault/keep.py

class Keep:
    def __init__(self):
        self.relics = {}
        self.currency = 0

    def store_relic(self, relic_name, quantity=1):
        if relic_name in self.relics:
            self.relics[relic_name] += quantity
        else:
            self.relics[relic_name] = quantity
        return f"{quantity}x {relic_name} added to your Keep."

    def withdraw_relic(self, relic_name, quantity=1):
        if relic_name not in self.relics:
            return f"{relic_name} not found in Keep."
        if self.relics[relic_name] < quantity:
            return f"Not enough {relic_name} in Keep."
        self.relics[relic_name] -= quantity
        if self.relics[relic_name] == 0:
            del self.relics[relic_name]
        return f"{quantity}x {relic_name} withdrawn."

    def deposit_currency(self, amount):
        self.currency += amount
        return f"{amount} tribute added to your Keep."

    def withdraw_currency(self, amount):
        if self.currency < amount:
            return "Not enough tribute stored."
        self.currency -= amount
        return f"{amount} tribute withdrawn from your Keep."

    def check_balance(self):
        return {
            "currency": self.currency,
            "relics": self.relics
        }
