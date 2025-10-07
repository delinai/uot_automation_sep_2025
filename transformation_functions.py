# Defined Functions
import pandas as pd

def next_action(brand):
    
    """
    The purpose of this function is to assign a next action
    based on the brand that the customer purchased.
    """

    if brand == 'ABC':
        return 'Call Customer'
    elif brand == 'Brand2':
        return 'Ship Directly with Purolator'
    elif brand =='DT':
        return 'Ship Directly with FedEx'

def delivery_date(x):

    """
    The purpose of the function is to calculate the shipping date
    If the order is placed Sat/Sun, ships next business day, otherwise
    within 2 business days
    """

    x = pd.to_datetime(x)
    if x.day_name() in ['Saturday','Sunday']:
        return x + pd.offsets.BDay(1)
    else:
        return x + pd.offsets.BDay(2)