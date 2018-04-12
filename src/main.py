import pandas as pd
from user_record import generate_user_record
from product import which_product_was_purchased, how_much_was_the_product
from customer import calculate_customer_column
from utils import how_many_visits_today
import json



def read_config():
    with open('./config.json') as f:
        config = json.load(f)
    return config


def main():
    record_list = []
    config = read_config()
    for d in pd.date_range(start=config['start-date'], end=config['end-date']):
        record_list.extend(
            [generate_user_record(d) for x in xrange(
                how_many_visits_today(100, 500))])

    df = pd.DataFrame(record_list)
    df['product_id'] = df.apply(which_product_was_purchased, axis=1)
    df['revenue'] = df['product_id'].apply(how_much_was_the_product)
    df['customer_id'] = calculate_customer_column(df, .05)
    df.to_csv('/output/synthetic_data.csv', index=False)


if __name__ == '__main__':
    main()
