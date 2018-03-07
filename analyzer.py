import pandas as pd

#Read txt file into a dataframe
data_table = pd.read_csv('data/data.txt',encoding='latin-1')
data_table = data_table.dropna(subset = ['ZIPCODE'])

#Sort then drop duplicates in order to keep lastest inspected date
data_table = data_table.sort_values(by=['INSPDATE'])
data_table = data_table.drop_duplicates(subset='CAMIS',keep='last')

#Drop all rows in the series with zipcodes that appear less than 100 times 
def display_valid_zips(zip_series):
    for zip, frequency in zip_series.iteritems():
        if frequency <= 100:
            zip_series = zip_series.drop(zip)
    return zip_series

zip_restaurants = display_valid_zips(data_table['ZIPCODE'].value_counts())

#Gather 92 series/list of all 92 restaurants and tally up the average scores
average_scores = {}
for k,v in zip_restaurants.iteritems():
    zip_df = data_table[data_table['ZIPCODE'] == k]
    zip_average = zip_df['SCORE'].sum() / v
    
    average_scores.update({k:float('%.1f'%zip_average)})

final_data = []
for k,v in zip_restaurants.iteritems():
    score = average_scores.get(k)
    data = (k, score, v)
    final_data.append(data)

#Sort by second item in tuple
final_data = sorted(final_data, key=lambda tup: tup[1], reverse=True)

#Output final results into output.txt
output = open('output.txt', 'w')
for data in final_data:
    output.write(str(data)[1:-1]+ "\n")

print(final_data)