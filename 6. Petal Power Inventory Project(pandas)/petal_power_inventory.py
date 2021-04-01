import codecademylib
import pandas as pd

inventory=  pd.read_csv('inventory.csv')

print(inventory.head())

staten_island= inventory.iloc[:10,:]
print(staten_island)

product_request= staten_island['product_description']

is_location_brooklyn= inventory['location']== 'Brooklyn'
print(is_location_brooklyn)

is_producttype_seed= inventory['product_type']== 'seeds'
print(is_producttype_seed) 

seed_request= inventory[is_location_brooklyn & is_producttype_seed ]
print(seed_request)

inventory['in_stock']= inventory.apply(lambda x: True if x.quantity> 0 else False, axis= 1)
print(inventory)

inventory['total_value']= inventory['price']* inventory['quantity']
print(inventory)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description']= inventory.apply(combine_lambda, axis= 1)
print(inventory)
