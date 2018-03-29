import random
import numpy as np


def was_product_purchased():
    X = random.random()
    if X >= .95:
        return True
    else:
        return False


def which_product_was_purchased():
    p_id = np.random.multinomial(1, [1/7.]*5 + [2/7.], size=1).argmax()
    return {'id': '{0}'.format(p_id)}


def how_much_was_the_product(p_id):
    X = {
        '1': 10,
        '2': 20,
        '3': 30,
        '4': 40,
        '5': 50,
        '0': 5}
    return X[p_id]
