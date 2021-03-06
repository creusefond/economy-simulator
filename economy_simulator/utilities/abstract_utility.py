from abc import ABC

class AbstractUtility(ABC):
    def quantities_to_purchase(self, individual, product_prices):
        pass

    def population_quantities_from_prices(self, individuals, product_prices):
        pass

    def utility(self, individual, product_quantities):
        pass