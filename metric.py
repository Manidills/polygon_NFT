import numpy
import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def polygon_metric(file_path):

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['__timestamp']) - pd.to_timedelta(7, unit='d')

    total_volume = df['Total Volume'].sum()
    total_volume = str(numpy.round(total_volume/1000000000,2)) + ' B' 

    daily_avg  = df['Total Volume'].mean()
    daily_avg = str(numpy.round(daily_avg/1000000,2)) + ' M'     

    df1 = df.groupby([pd.Grouper(key='Date', freq='W-MON')])['Total Volume'].sum().reset_index().sort_values('Date')
    weekly_avg = str(numpy.round(df1['Total Volume'].sum()/len(df1)/1000000,2)) + ' M'  

    return total_volume,daily_avg,weekly_avg


@st.cache(allow_output_mutation=True)
def chicken_metric(file_path):

    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['__timestamp']) - pd.to_timedelta(7, unit='d')

    total_volume = df['Total Volume'].sum()
    total_volume = str(numpy.round(total_volume/1000000,2)) + ' M' 

    daily_avg  = df['Total Volume'].mean()
    daily_avg = str(numpy.round(daily_avg/1000,2)) + ' K'     

    df1 = df.groupby([pd.Grouper(key='Date', freq='W-MON')])['Total Volume'].sum().reset_index().sort_values('Date')
    weekly_avg = str(numpy.round(df1['Total Volume'].sum()/len(df1)/1000,2)) + ' k'  

    return total_volume,daily_avg,weekly_avg