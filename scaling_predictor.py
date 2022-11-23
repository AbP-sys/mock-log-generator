import re
import pandas as pd
import matplotlib.dates as mpl_dates
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def modify(df):
        df['TimestampEpoch']=pd.to_datetime(df['Timestamp'])
        #df[['CPU','Memory']]=df[['CPU','Memory']].astype(float)
        df.reset_index(inplace=True)
        df['TimestampEpoch']=df['TimestampEpoch'].apply(mpl_dates.date2num)
        df[['CPU','Memory','TimestampEpoch']] = df[['CPU','Memory','TimestampEpoch']].astype(float)
        return df

def create_indicators(df):
    df['SMA30'] = df['CPU'].rolling(30).mean()
    k = df['SMA30'].ewm(span=12, adjust=False, min_periods=12).mean()
    # Get the 12-day EMA of the closing price
    d = df['SMA30'].ewm(span=26, adjust=False, min_periods=26).mean()
    # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
    macd = k - d
    # Get the 9-Day EMA of the MACD for the Trigger line
    macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
    macd_h = macd - macd_s
    # Add all of our new values for the MACD to the dataframe
    df['macd'] = df.index.map(macd)
    df['macd_h'] = df.index.map(macd_h)
    df['macd_s'] = df.index.map(macd_s)
    return df

def calculate(df):
    time=[]
    for i in range(df.shape[0]-1):
        if (df['macd'].loc[i+1] > df['macd_s'].loc[i+1]) and (df['macd'].loc[i]<df['macd_s'].loc[i]):
            slope = (df['SMA30'].loc[i+1] - df['SMA30'].loc[i])/((df['TimestampEpoch'].loc[i+1] - df['TimestampEpoch'].loc[i])*100)
            slope_macd = (df['macd'].loc[i+1] - df['macd'].loc[i])/((df['TimestampEpoch'].loc[i+1] - df['TimestampEpoch'].loc[i])*100)
            if slope>200  and slope_macd>0 and slope_macd<35:
                #print("TRUE SLOPE: " , slope , slope_macd)
                time.append(df['TimestampEpoch'].loc[i])
            #else:
                 #print("FALSE SLOPE: ",slope,slope_macd)
    return time

def plot_data(df,time):
    fig = plt.figure(figsize=(25,8))
    sns.lineplot(data=df,x='TimestampEpoch',y='CPU')
    sns.lineplot(data=df,x='TimestampEpoch',y='macd',color='red')
    sns.lineplot(data=df,x='TimestampEpoch',y='macd_s',color='black')
    sns.lineplot(data=df,x='TimestampEpoch',y='SMA30',color='black') 
    for i in time:
        plt.axvline(i)
    return fig