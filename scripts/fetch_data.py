import json
import time 
import pandas as pd
import yfinance as yf
from tqdm import tqdm 
import logging

logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False

class DataLoader:
    def __init__(self, tickers):
        self.tickers = tickers
        self.df_list = []

    def load_data(self, interval, period, output_file='./data/sp500_dataset.csv'):
        for i in tqdm(range(len(self.tickers)), desc="Fetching Data..."):
            ticker = self.tickers[i]
            stock = yf.Ticker(ticker)
            stock_df = stock.history(period=period, interval=interval)
            stock_df['Ticker'] = ticker
            self.df_list.append(stock_df)
        
        print("Data fetched.")

        master_df = pd.concat(self.df_list)
        master_df.to_csv(output_file)

        print("Datset file created.")


df = pd.read_csv('./data/sp500_companies.csv')
tickers = df['Symbol'].tolist()

data_loader = DataLoader(tickers)
data_loader.load_data('1d', '5y')





