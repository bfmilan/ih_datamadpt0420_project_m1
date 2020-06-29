import pandas as pd
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine


# Function to connect the database and get a dataframe from it. It also exports it to a csv.
def acquire(path):
    print('importing the db...')
    engine = create_engine(f'sqlite:///{path}', poolclass=StaticPool)
    raw_data = pd.read_sql("""SELECT * FROM career_info   
    inner join poll_info on career_info.uuid = poll_info.uuid  
    inner join country_info on country_info.uuid = poll_info.uuid 
    inner join personal_info on personal_info.uuid = career_info.uuid""", engine)
    raw_data.to_csv('data/raw/raw_data_info.csv', index=False)
    print('db saved...')
    return raw_data
