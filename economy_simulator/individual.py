import random
from .utilities.utility_factory import utility_factory

class Individual():
    utility_weights = None
    available_money = 0
    utility_function = None

    def __init__(self, products, utility_function_name="ln"):
        self.utility_weights = {}
        sum_utility_weights = 0
        for product_name, product_content in products.items():
            product_weight = product_content["utility_weight"]
            self.utility_weights[product_name] = random.random() * product_weight
            sum_utility_weights += self.utility_weights[product_name]

        for product_name, utility_weight in self.utility_weights.items():
            self.utility_weights[product_name] = utility_weight / sum_utility_weights
        
        self.utility_function = utility_factory(utility_function_name)

    def utility(self, products_quantities):
        return self.utility_function.utility(self, products_quantities)
    
    def get_utility_weights(self):
        return self.utility_weights

    def get_available_money(self):
        return self.available_money
    
    def give_money(self, amount):
        self.available_money += amount