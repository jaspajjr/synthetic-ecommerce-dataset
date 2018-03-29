import pandas as pd
from user_record import generate_user_record
import datetime


def main():
    for d in pd.date_range(start='2018-01-01', end='2018-01-31'):
        user_record = generate_user_record(d)
    print (user_record)


if __name__ == '__main__':
    main()
