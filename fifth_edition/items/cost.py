"""Cost Base Class"""

__author__ = "Grant Colasurdo"


class Cost:
    def __init__(self, coins=None):
        self.copper_pieces: int = 0
        self.silver_pieces: int = 0
        self.electrum_pieces: int = 0
        self.gold_pieces: int = 0
        self.platinum_pieces: int = 0
        if isinstance(coins, list):
            if len(coins) == 5:
                self.copper_pieces = coins[0]
                self.silver_pieces = coins[1]
                self.electrum_pieces = coins[2]
                self.gold_pieces = coins[3]
                self.platinum_pieces = coins[4]

    def __add__(self, other):
        self.copper_pieces += other.copper_pieces
        self.silver_pieces += other.silver_pieces
        self.electrum_pieces += other.silver_pieces
        self.gold_pieces += other.gold_pieces
        self.platinum_pieces += other.platinum_pieces
        
    def __sub__(self, other):
        if (
                self.copper_pieces >= other.copper_pieces and
                self.silver_pieces >= other.silver_pieces and
                self.electrum_pieces >= other.electrum_pieces and
                self.gold_pieces >= other.gold_pieces and
                self.platinum_pieces >= other.platinum_pieces
        ):
            self.copper_pieces -= other.copper_pieces
            self.silver_pieces -= other.silver_pieces
            self.electrum_pieces -= other.electrum_pieces
            self.gold_pieces -= other.electrum_pieces
            self.platinum_pieces -= other.platinum_pieces

    @property
    def calculated_reduced_value(self):
        reduced_cost = Cost()
        remaining_value = self.calculated_base_cost
        while remaining_value >= 1000:
            reduced_cost.platinum_pieces += 1
            remaining_value -= 1000
        while remaining_value >= 100:
            reduced_cost.gold_pieces += 1
            remaining_value -= 100
        while remaining_value >= 50:
            reduced_cost.electrum_pieces += 1
            remaining_value -= 50
        while remaining_value >= 10:
            reduced_cost.silver_pieces += 1
            remaining_value -= 10
        while remaining_value >= 1:
            reduced_cost.copper_pieces += 1
            remaining_value -= 1
        return reduced_cost

    @property
    def calculated_base_cost(self):
        base_cost = self.copper_pieces
        base_cost += self.silver_pieces * 10
        base_cost += self.electrum_pieces * 50
        base_cost += self.gold_pieces * 100
        base_cost += self.platinum_pieces * 1000
        return base_cost
