import pandas as pd
from glob import glob
from time import strftime, sleep
import numpy as np
from datetime import datetime
from pandas_datareader import data as pdr
from pandas.tseries.offsets import BDay
import yfinance as yf
yf.pdr_override()

# simple function to make headers nicer
def clean_header(df):
    df.columns = df.columns.str.strip().str.lower().str.replace('.', '').str.replace('(', '').str.replace(')', '').str.replace(' ', '_').str.replace('_/_', '/')

# timestamp for file names
def get_now():
    now = datetime.now().strftime('%Y-%m-%d_%Hh%Mm')
    return now

last_file = glob('/home/miensop51_gmail_com/MIMI/mimi/portfolio/inputs/transactions_all/tan.xlsx')[-1] # path to file in the folder
print(last_file[-(len(last_file))+(last_file.rfind('/')+1):])
all_transactions = pd.read_excel(last_file)
all_transactions.date = pd.to_datetime(all_transactions.date, format='%d/%m/%Y')