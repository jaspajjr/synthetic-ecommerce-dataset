import numpy as np


def which_browser():
    browser = {
        0: 'edge',
        1: 'chrome',
        2: 'firefox',
        3: 'apple',
        4: 'other'
    }
    return browser[np.random.multinomial(1, [1/5.]*5, size=1).argmax()]


def which_OS():
    OS = {
        0: 'windows',
        1: 'linux',
        2: 'apple',
        3: 'gentoo'
    }
    return OS[np.random.multinomial(1, [5/10., 3/10., 3/20., 1/20.], size=1).argmax()]
