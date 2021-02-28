import random
import math

class Individual():
    utility_weights = None
    available_money = 0

    def __init__(self, products):
        self.utility_weights = {}
        sum_utility_weights = 0
        for product_name, product_content in products.items():
            product_weight = product_content["utility_weight"]
            self.utility_weights[product_name] = random.random() * product_weight
            sum_utility_weights += self.utility_weights[product_name]

        for product_name, utility_weight in self.utility_weights.items():
            self.utility_weights[product_name] = utility_weight / sum_utility_weights

    def utility(self, products_quantity, utility_function="linear"):
        utilities = {
            "linear": self._linear_utility,
            "ln": self._ln_utility,
            "quadratic": self._quadratic_utility
        }
        sum_utilities = 0
        for product_name, utility_weight in self.utility_weights.items():
            quantity = products_quantity.get(product_name, 0)
            sum_utilities += utility_weight * utilities[utility_function](quantity)
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