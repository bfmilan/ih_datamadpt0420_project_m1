import pandas as pd
import numpy as np

def clean_data(data):
	pd.set_option('mode.chained_assignment', None)
	print(f' These are the initial data columns to show: {data.columns.values.tolist()}')
	data = data[['Country', 'Job Title', 'Gender', 'uuid']]
	data.columns = ['Country', 'Job Title', 'Gender', 'uuid', 'caca1', 'caca2', 'caca3']
	data = data[['Country', 'Job Title', 'Gender', 'uuid']]
	print(f' These are the FINAL data columns to show: {data.columns.values.tolist()}')
	print()
	null_cols = data.isnull().sum()
	print(null_cols[null_cols > 0])
	# education_level 663
	# Job Title 3947
	print()
	print(f'{null_cols[null_cols > 0] / len(data) * 100}')
	# education_level: 6.871178
	# Job Title: 40.905793
	print(f'My final data shape: {data.shape}\n My final data type: {type(data)}\n My final data head:\n{data.head(10)}')
	print(data.head(10))
	print(f'Table: Data info\nRows: {data.shape[0]} \nColumns: {data.shape[1]}\n\nNull values:\n{data.isnull().sum()}')
	return data


# analysis functions
# Challenge 1
def challenge1(data, country='All'):
	ch1 = data.groupby(['Country', 'Job Title', 'Gender'])['uuid'].count().reset_index()
	ch1.rename(columns={'uuid': 'Quantity'},
				  inplace=True)
	country_filter = ch1['Country'] == country
	if country == 'All':
		check_quantity = ch1['Quantity'].sum()
		print(f'we have the quantity calculated for all! {check_quantity}')
		ch1.to_csv('data/results/ch1_quantity.csv', index=False)
	else:
		ch1 = ch1.loc[country_filter]
		check_quantity = ch1['Quantity'].sum()
		print(f'we have the quantity calculated for {country}! {check_quantity}')
		print(ch1)
		ch1.to_csv('data/results/ch1_quantity.csv', index=False)

	ch1['Percentage'] = ch1['Quantity'] / ch1['Quantity'].sum() * 1000
	print(ch1.head(10))
	print(f'My final data shape: {ch1.shape}\n My final data type: {type(ch1)}\n My final data head:\n{ch1.head(10)}')
	ch1.to_csv('data/results/data_final.csv', index=False)
	return ch1


def analysis(data, country):
	data_clean = clean_data(data)
	final_data = challenge1(data_clean, country)
	return final_data