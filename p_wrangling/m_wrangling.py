import requests
import pandas as pd
from copy import deepcopy


# Function to build the API and make requests. Input: string, job code. Output: string, job name.
def response_api(job_code):
	print('Calling job api...')
	return requests.get(f'http://api.dataatwork.org/v1/jobs/{job_code}').json().get('title')
	print('Job api call finished..')


# Function to build the API and make requests. Input: string, job code. Output: string, job name.
def response_api2(country_code):
	print('Calling the country api...')
	return requests.get(f'https://restcountries.eu/rest/v2/alpha/{country_code}').json().get('name')
	print('Country api call finished..')


# Function to clean job_title column. It gets a dictionary containing every unique job code in the df. Its keys are
# job codes, its values are job names it iterates over the column.
def jobs_column(raw_data):
	print('Merging job info..')
	# raw_data["normalized_job_code"].fillna('none', inplace=True)
	job_codes_list = list(raw_data['normalized_job_code'].dropna().unique())
	jobs_dict = {job: response_api(job) for job in job_codes_list}
	raw_data['normalized_job_code'] = raw_data['normalized_job_code'].apply(lambda job: jobs_dict.get(job))
	return raw_data
	print('Job info there!')


def country_column(raw_data):
	print('Merging country info..')
	country_codes_list = list(raw_data['country_code'].dropna().unique())
	country_dict = {country: response_api2(country) for country in country_codes_list}
	raw_data['country_code'] = raw_data['country_code'].apply(lambda country: country_dict.get(country))
	raw_data['country_code'] = raw_data['country_code'].str.replace('United Kingdom of Great Britain and Northern '
																	'Ireland', 'UK')

	return raw_data
	print('Country info there!')


# Function to clean rural column. The aim is to get only two values: 'rural' or 'urban'.
def rural_column(raw_data):
	print('Cleaning the rural column..')
	raw_data['rural'] = raw_data['rural'].str.lower()
	raw_data['rural'] = raw_data['rural'].str.replace('city', 'urban') \
		.replace('non-rural', 'urban') \
		.replace('countryside', 'rural') \
		.replace('country', 'rural')
	return raw_data['rural']
	print('Rural column clean!')


# Function to clean gender column. The aim is to get only two values: 'Male' or Female'.
def gender_column(raw_data):
	print('Cleaning the gender column..')
	raw_data['gender'] = raw_data['gender'].str.lower()
	# raw_data["gender"].replace("Fem", "Female", inplace=True).replace('Male', 'male')
	raw_data['gender'] = raw_data['gender'].str.replace('fem', 'female') \
		.replace('Male', 'male')
	return raw_data['gender']
	print('Gender column clean!')



# Function to clean gender column. The aim is to get only two values: 'Male' or Female'.
def rename_column(raw_data):
	print('Renaming rest of the columns...')
	raw_data.rename(columns={'country_code': 'Country', 'gender': 'Gender',
							 'rural': 'Area',
							 'age_group': 'Age',
							 'dem_has_children': 'Children',
							 'dem_education_level': 'education_level',
							 'dem_full_time_job': 'full_time_job',
							 'normalized_job_code': 'Job Title',
							 'question_bbi_2016wave4_basicincome_awareness': 'basic_income_awareness',
							 'question_bbi_2016wave4_basicincome_vote': 'basic_income_vote',
							 'question_bbi_2016wave4_basicincome_effect': 'basic_income_effect',
							 'question_bbi_2016wave4_basicincome_argumentsfor': 'basic_income_arguments_for',
							 'question_bbi_2016wave4_basicincome_argumentsagainst': 'basic_income_arguments_against'},
					inplace=True)
	return raw_data
	print('All columns renamed!')


def wrangling(raw_data):
    jobs_column(raw_data)
    country_column(raw_data)
    rural_column(raw_data)
    gender_column(raw_data)
    rename_column(raw_data)
    raw_data.to_csv('data/raw/raw_data_all.csv', index=False)
    print(raw_data.shape)
    print(raw_data.columns.values.tolist())
    return raw_data
