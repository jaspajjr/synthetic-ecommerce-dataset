import pandas as pd
from user_record import generate_user_record
from utils import how_many_visits_today
import datetime


def main():
    record_list = []
    for d in pd.date_range(start='2018-01-01', end='2018-01-31'):
        record_list.extend(
            [generate_user_record(d) for x in xrange(
                how_many_visits_today(100, 500))])

    df = pd.DataFrame(record_list)
    print(df.info())
    print df.head()


if __name__ == '__main__':
    main()
