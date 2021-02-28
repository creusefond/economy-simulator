import random
import math

class Individual():
    preferences = None
    available_money = 0

    def __init__(self, products):
        self.preferences = {}
        sum_preferences = 0
        for product_name, product_content in products.items():
            product_weight = product_content["preference_weight"]
            self.preferences[product_name] = random.random() * product_weight
            sum_preferences += self.preferences[product_name]

        for product_name, preference in self.preferences.items():
            self.preferences[product_name] = preference / sum_preferences

    def utility(self, products_quantity, utility_function="linear"):
        utilities = {
            "linear": self._linear_utility,
            "ln": self._ln_utility,
            "quadratic": self._quadratic_utility
        }
        sum_utilities = 0
        for product_name, preference in self.preferences.items():
            quantity = products_quantity.get(product_name, 0)
            sum_utilities += preference * utilities[utility_function](quantity)
        return sum_utilities
    
    def quantities_to_purchase(self, products_price):
        # Get the lagrangien multiplicator corresponding to the condition that all the money is spent
        # Compute each quantity
        pass
    
    def give_money(self, amount):
        self.available_money += amount

    def _linear_utility(self, quantity):
        return quantity
    
    def _ln_utility(self, quantity):
        return math.log(quantity + 1 )
    
    def _quadratic_utility(self, quantity):
        # (- x - q)² - x²
        x = 5
        return (-1) * (x - quantity) * (x - quantity) + x * x