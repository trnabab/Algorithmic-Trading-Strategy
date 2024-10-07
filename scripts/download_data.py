import yfinance as yf
import pandas as pd
import datetime as dt

def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f'../data/{ticker}.csv')

if __name__ == "__main__":
    enddate = dt.datetime.now().date()
    startdate = enddate - dt.timedelta(days=365*5)
    download_data('CRM', start_date=startdate, end_date=enddate)