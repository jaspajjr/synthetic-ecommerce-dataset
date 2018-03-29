import numpy as np
import uuid


def how_many_visits_today(lower_bound, upper_bound):
    return np.random.randint(lower_bound, upper_bound)


def generate_session_id():
    return uuid.uuid4()


def generate_time_of_day():
    return {
        'hours': random.randrange(0, 23),
        'minutes': random.randrange(0, 59),
        'seconds': random.randrange(0, 59)
    }


def combine_times(input_date):
    yield input_date + datetime.timedelta(**generate_time_of_day())


def which_marketing_channel():
    channels = {
        0: 'direct',
        1: 'seo',
        2: 'cpc',
        3: 'display',
        4: 'other'
    }
    return channels[np.random.multinomial(1, [1/5.]*5, size=1).argmax()]
