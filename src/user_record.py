from utils import generate_session_id, combine_times, which_marketing_channel
from product import was_product_purchased
from device import which_browser, which_OS


def generate_user_record(date):
    return {
        'session_id': generate_session_id(),
        'visitStartTime': combine_times(date),
        'transaction': was_product_purchased(),
        'marketing_channel': which_marketing_channel(),
        'deviceBrowser': which_browser(),
        'which_OS': which_OS()}
