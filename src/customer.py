import random


def calculate_customer_column(df, retention_rate):
    '''
    Given a dataframe create a new column of customer ID numbers.
    '''
    customers = set()
    customer_list = []
    for num, visit in enumerate(df.index):
        if num == 0:
            new_id = create_new_customer_id()
            customers.add(new_id)
            customer_list.append(new_id)
        else:
            if check_new_customer(retention_rate) == 0:
                customer_list.append(random.sample(customers, 1))
            else:
                new_id = create_new_customer_id()
                customers.add(new_id)
                customer_list.append(new_id)

    return customer_list


def create_new_customer_id():
    '''
    creates a new customer id with n digits.
    '''
    n = 8
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def check_new_customer(retention_rate):
    '''
    Given the retention rate, checks if this customer is new
    '''
    X = random.random()
    if X <= retention_rate:
        return 0
    else:
        return 1
