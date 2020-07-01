import pandas as pd
from sqlalchemy import create_engine
from functools import reduce
import requests
from bs4 import BeautifulSoup
import re


# acquisition functions
def get_tables(path):
    engine = create_engine(f'sqlite:///{path}')
    df_personal = pd.read_sql("SELECT * FROM personal_info", engine)
    df_country = pd.read_sql("SELECT * FROM country_info", engine)
    df_career = pd.read_sql("SELECT * FROM career_info", engine)
    df_poll = pd.read_sql("SELECT * FROM poll_info", engine)
    dfs = [df_personal, df_country, df_career, df_poll]
    df_final = reduce(lambda left, right: pd.merge(left, right, on='uuid'), dfs)
    return df_final

print(df_final)



----
df_clean = raw_data[
    'uuid', 'education_level', 'full_time_job', 'Job Title', 'uuid', 'basic_income_awareness', 'basic_income_vote',
    'basic_income_effect', 'basic_income_arguments_for', 'basic_income_arguments_against', 'uuid', 'Country', 'Area',
    'uuid', 'age', 'Gender', 'Children', 'Age']
df_clean.columns = ['uuid', 'Education_level', 'Full_time_job', 'Job Title', 'caca', 'basic_income_awareness',
                    'basic_income_vote',
                    'basic_income_effect', 'basic_income_arguments_for', 'basic_income_arguments_against', 'caca1',
                    'Country', 'Area',
                    'caca2', 'age', 'Gender', 'Children', 'Age']
df_clean = df_clean[
    'uuid', 'Education_level', 'Full_time_job', 'Job Title', 'basic_income_awareness', 'basic_income_vote',
    'basic_income_effect', 'basic_income_arguments_for', 'basic_income_arguments_against', 'Country', 'Area',
    'Gender', 'Children', 'Age']