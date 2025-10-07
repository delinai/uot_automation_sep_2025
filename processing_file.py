import pandas as pd
import datetime as dt
from transformation_functions import next_action, delivery_date

# Maintainable mapping
route_map = {'Call Customer':'Personalized Delivery', 'Ship Directly with Purolator':'Purolator_123', 
             'Ship Directly with FedEx':'FedEx_Express'}

# Import source data
am = pd.read_csv(r'/Users/delinaivanova/Downloads/account_managers.csv') 
co = pd.read_csv(r'/Users/delinaivanova/Downloads/customer_orders.csv') 

# Clean up order_date field to be datetime data type instead of a string object
co['order_date'] = pd.to_datetime(co['order_date'])

# Aligning each account manager to the correct product group
co.drop('account_manager', axis=1, inplace=True)
co = pd.merge(left = am, right=co, left_on='brand', right_on='brand', how='inner')

# Determine the next action, using next_action() function
co['next_action'] = co['brand'].apply(next_action)

# Determine delivery date
co['delivery_date'] = co['order_date'].apply(delivery_date)

# Detrmine delivery route
co['delivery_route'] = co['next_action'].map(route_map)

co.to_csv('/Users/delinaivanova/Downloads/final_order_routing.csv')
