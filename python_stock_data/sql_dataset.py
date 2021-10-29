import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
df = web.DataReader("TQQQ", "yahoo", start, end)