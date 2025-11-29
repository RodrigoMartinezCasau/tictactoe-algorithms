class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def __str__(self):
        return f"{self.name} ({self.symbol})"
