# Graphical libs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Email libs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Reading images lib
from PIL import Image

def graph_reporting(molins):
    print('Lets get the data...')
    # df_ch1 = pd.read_csv('./../data/results/ch1_quantity.csv')
    df_ch1 = molins
    # df_all = pd.read_csv('./../data/raw/raw_data_all.csv')
    print('Creating gender distribution chart.')
    graph_pie = df_ch1.drop(df_ch1.loc[df_ch1['Job Title'] == 'none'].index, inplace=True)
    graph_pie = df_ch1[['Gender', 'Quantity']].set_index('Gender').groupby('Gender').sum().reset_index()
    ax = graph_pie.set_index('Gender').plot.pie(y='Quantity', x='Gender', figsize=(8, 8))
    fig = ax.get_figure()
    fig.savefig('./data/reporting/gender_distribution_pie.jpeg')
    print('Pie figure with gender distribution saved in the results folder\n')
    return fig


def pdf_reporting():
    img1 = Image.open('./data/reporting/gender_distribution_pie.jpeg')
    # img2 = Image.open('./../data/reporting/gender_distribution_bar.jpeg')

    img1.save(r'./data/reporting/reporting.pdf', save_all=True)
    # img1.save(r'./../data/reporting/reporting.pdf', save_all=True, append_images=[img2])
    print('PDF report with key results generated and saved in the reporting folder\n')
    return img1

def email_reporting(email):
    # https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/

    fromaddr = "bfmilan@gmail.com"  # <--------------------------------------  Cuenta envío
    # toaddr = "marmilan60@gmail.com"  # <----------------------------------------  Email receptor
    rec_list = ['bfmilan@gmail.com', 'bfmilan@gmail.com']
    rec = ', '.join(rec_list)
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = rec

    # storing the subject
    msg['Subject'] = "Our first kiss - one of a million to come..."

    # string to store the body of the mail
    body = '''Dear Py,
        This is my first gesture of love, with many others to come...
        LuvYa'''

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = "reporting.pdf"
    attachment = open("./data/reporting/project1.pdf", "rb")  # <--------------------------------------  Attachements

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "....")  # <----------------------------------------  Contraseña de aplicación

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, rec_list, text)

    # terminating the session
    s.quit()

    print(f'Report sent to {rec_list}!')



