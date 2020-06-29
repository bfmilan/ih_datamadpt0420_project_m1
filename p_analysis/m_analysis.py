import pandas as pd
import numpy as np

def clean_data(data):
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
def compute_quantity(data):
	# Deactivating SettingWithCopyWarning.
	# A value is trying to be set on a copy of a slice from a DataFrame.

	pd.set_option('mode.chained_assignment', None)

	print('Getting rid of NaN values...')
	data = data[['Country', 'Job Title', 'Gender', 'uuid']]
	data.columns = ['Country', 'Job Title', 'Gender', 'uuid', 'caca1', 'caca2', 'caca3']
	data = data[['Country', 'Job Title', 'Gender', 'uuid']]
	data.dropna(subset=['Job Title'], axis = 0, inplace = True)
	print('NaN values gone!')
	print(f'Table: Data info after Nan cleaning \nRows: {data.shape[0]} \nColumns: {data.shape[1]}\n\nNull values:\n{data.isnull().sum()}')
	data = data.groupby(['Country', 'Job Title', 'Gender'])['uuid'].count().reset_index()
	data.rename(columns={'uuid': 'Quantity'},
				  inplace=True)
	# data.groupby(['Country', 'Gender'], as_index=False).agg({'Job Title': pd.Series.nunique})
	print(data)
	country_filter = data['Country'] == 'Spain'
	# country_filter = df_ch1['Country'] == country.capitalize()
	data = data.loc[country_filter]
	print(data)
	check_quantity = data['Quantity'].sum()
	print(f'we have the quantity calculated! {check_quantity}')
	data.to_csv('data/results/data_quantity.csv', index=False)
	return data


def compute_quantity_percent(data):
	data = pd.read_csv('/Users/Blanca/ironhack/gitrepo/ih_datamadpt0420_project_m1/data/results/data_quantity.csv')
	# data = data.groupby(['Country', 'Job Title', 'Gender'])['Quantity'].count().reset_index()
	# data['Percentage'] = data.apply(lambda row: row['Quantity'] / row['Quantity'], axis=1)
	data['Percentage'] = data['Quantity'] / data['Quantity'].sum() * 1000
	print(data.head(10))
	# data['Percentage'] = (data['Quantity'] / 1000)
	# print(f'Check Percentage Sym: {data['Percentage'].sum()}')
	print(f'My final data shape: {data.shape}\n My final data type: {type(data)}\n My final data head:\n{data.head(10)}')
	data.to_csv('data/results/data_final.csv', index=False)
	return data


def analysis(data: object) -> object:
	clean_data(data)
	compute_quantity(data)
	compute_quantity_percent(data)
	# data.to_csv('data/results/data_final.csv', index=False)
	return data
