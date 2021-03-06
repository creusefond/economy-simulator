from .ln_utility import LnUtility

UTILITIES = {
    "ln": LnUtility
}

def utility_factory(utility_name):
    return UTILITIES[utility_name]()
