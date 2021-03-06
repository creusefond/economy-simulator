from .abstract_utility import AbstractUtility

import math

class LnUtility(AbstractUtility):
    def quantities_to_purchase(self, individual, product_prices):
        result = {}
        for product in product_prices:
            available_money = individual.get_available_money()
            weight = individual.get_utility_weights()[product]
            product_price = product_prices[product]
            result[product] = available_money * weight / product_price

        return result

    def population_quantities_from_prices(self, individuals, product_prices):
        result = {}
        for product in product_prices:
            sum_mu_wup = 0
            for individual in individuals:
                available_money = individual.get_available_money()
                weight = individual.get_utility_weights()[product]
                sum_mu_wup += available_money * weight
            result[product] = sum_mu_wup / product_prices[product]
        return result

    def utility(self, individual, product_quantities):
        result = 0
        for product in product_quantities:
            weight = individual.get_utility_weights()[product]
            quantity = product_quantities[product]
            result += weight * math.log(quantity)
        return result



