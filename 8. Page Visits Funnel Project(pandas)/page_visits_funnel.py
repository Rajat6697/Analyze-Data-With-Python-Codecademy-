import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart= pd.merge(visits, cart, how= 'left')
print(len(visits_cart))
#The length og our merged DF is 2000

print(visits_cart['cart_time'].isnull().sum())
#There are 1652 null values in column cart_time

not_added_to_cart= (float(visits_cart['cart_time'].isnull().sum())/len(visits_cart['cart_time']))*100
print(not_added_to_cart)
# 82.6% users didn't added t-shirt in their cart

cart_checkout= pd.merge(cart, checkout, how= 'left')
not_checked_out= cart_checkout['checkout_time'].isnull().sum()
not_checked_out_per= float(not_checked_out)/len(cart_checkout)*100
print(not_checked_out_per)
# 25% of users didn't checked out the item after adding them in their cart

all_data= visits.merge(cart, how= 'left').merge(checkout, how= 'left').merge(purchase, how= 'left')

print(all_data.head())

not_bought= (all_data['purchase_time'].notnull().sum()/float(all_data['checkout_time'].notnull().sum())) * 100
print(not_bought)
# 83.11% people proceeded to checkout but didn't actually bought the item.
print('Not added to cart:')
print(not_added_to_cart)
print('Not checked out:')
print(not_checked_out_per)
print('not bought:')
print(not_bought)


all_data['avg_time_to_purchase']= all_data['purchase_time']-all_data['visit_time']
print(all_data.head())

print(all_data['avg_time_to_purchase'])

print(all_data['avg_time_to_purchase'].mean())
