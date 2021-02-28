import economy_simulator.individual as ind

class Model:
    individuals = []
    conf = {}
    def __init__(self, conf):
        self.conf = conf
        # 1 Individuals are created
        products = conf["products"]
        nb_individuals = conf["individuals"]["number"]
        self.individuals = []
        for _ in range(nb_individuals):
            self.individuals.append(ind.Individual(products))
    
    def run(self, _interations):
        # 1 Companies product produces

        # 2 Companies give the result of the production to the individuals
        # 3 Individuals exchange the products
        quantities = {}
        for product in self.conf["products"]:
            quantities[product] = 10
        for individual in self.individuals:
            individual.give_money(10)

        for individual in self.individuals:
            utility = individual.utility(quantities, self.conf['individuals']['utility'])
            print(utility)