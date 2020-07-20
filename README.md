# Ironhack Data Analytics Module 1 Project
Survey answers Pipeline showing quantity and percentage of respondents per country, job and living area.

---
### :computer: **Technology stack**
Python

### :boom: **Core technical concepts**
Reporting tool to analyze survey results.
It generates a .csv every time the script runs.
- It provides two options for the final user to select when executing: 
**(1)** To get the table for every country included in the dataset (All), 
**(2)** To get the table for a specific country imputed by the user (i.e. Spain)
- GitHub repository which includes a README file (this file) that explains the aim and content of my code. 
- Data Pipeline that retrieves the following table as well as `.csv` file including a table with . 
| Country | Job Title      | Gender (1) | Quantity | Percentage |
|---------|----------------|------------|----------|------------|
| Spain   | Data Scientist | Male       | 25       | 5%         |
| Spain   | Data Scientist | Female     | 25       | 5%         |
| ...     | ...            | ...        | ...      | ...        |
- Image (jpg), that adds to a pdf report: includes pie plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc. 
![Image](./data/reporting/gender_distribution_pie.jpeg)
- 3 minutes presentation (ppt) to explain my project. 
![Image](./data/reporting/project1_rm.png)


### :wrench: **Configuration**
See needed libraries in: requirements.txt.
Database used can be found in: /data/raw/raw_data_project_m1.db.
### :see_no_evil: **Usage**
When running the script it will export all countries by default. 

In case filtering by one or more countries is needed, run the script using `-c or --country` parameters including a blank space between each country as shown below:

`python main_script -c Spain Austria`

The script will export a .csv per each stage of the project which you'll find in the /data folder.

### :file_folder: **Folder structure**
The folders marked with * are still to be included 
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env*
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── your_path.py
    ├── notebooks
    │   ├── acquisitions.ipynb
    │   └── analysis.ipynb
    │   ├── other-code.ipynb
    │   └── reporting.ipynb    
    │   └── wrangling.ipynb
    ├── p_acquisition
    │   └── m_acquisition.py
    ├── p_analysis
    │   └── m_analysis.py
    ├── p_reporting
    │   └── m_reporting.py
    ├── p_wrangling
    │   └── m_wrangling.py
    └── data
        ├── raw
           ├── raw_data_all.csv
           ├── raw_data_info.csv
           ├── raw_data_project_m1.db
        ├── processed
        └── results
           ├── ch1_quantity.csv
           ├── data_final.csv

``` 

### :information_source: **Further info**
Web Api links: 
Country data: https://restcountries.eu/rest/v2/alpha/
Job data: http://api.dataatwork.org/v1/jobs/

---
Libraries

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- [Requests](https://requests.readthedocs.io/)

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [Argparse](https://docs.python.org/3.7/library/argparse.html)












 


 

