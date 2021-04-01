import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

views_count= ad_clicks.groupby('utm_source')['user_id'].count().reset_index()
print(views_count)

ad_clicks['is_click']= ad_clicks['ad_click_timestamp'].isnull()
print(ad_clicks)

clicks_by_source= ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
print(clicks_by_source)

clicks_pivot= clicks_by_source.pivot(columns= 'is_click', index= 'utm_source', values= 'user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked']= clicks_pivot[True]/(clicks_pivot[True]+ clicks_pivot[False])
print(clicks_pivot)


print(ad_clicks.groupby('experimental_group').user_id.count())

print(ad_clicks.head())

is_click_count= ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
print(is_click_count)
is_click_count_pivot= is_click_count.pivot(columns= 'is_click', index= 'experimental_group', values= 'user_id').reset_index()
print(is_click_count_pivot)

is_click_count_pivot['percent_clicked_by_group']= is_click_count_pivot[True]/(is_click_count_pivot[True]+is_click_count_pivot[False])*100
print(is_click_count_pivot)

a_clicks= ad_clicks[ad_clicks['experimental_group']== 'A']
b_clicks= ad_clicks[ad_clicks['experimental_group']== 'B']

print(a_clicks)
print(b_clicks)

a_clicks_byday= a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(columns= 'is_click', index= 'day', values= 'user_id').reset_index()
print(a_clicks_byday)
a_clicks_byday['percent_clicked']= a_clicks_byday[True]/(a_clicks_byday[True]+a_clicks_byday[False])* 100
print(a_clicks_byday)


b_clicks_byday= b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(columns= 'is_click', index= 'day', values= 'user_id').reset_index()
print(b_clicks_byday)
b_clicks_byday['percent_clicked']= b_clicks_byday[True]/(b_clicks_byday[True]+b_clicks_byday[False])* 100
print(b_clicks_byday)
