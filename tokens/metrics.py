import streamlit as st
import numpy as np
import pandas as pd
from load import load


def metrics():
    col1, col2, col3 = st.columns((3,3,3))
    df = load()
    #unique_token
    unique_tokens = len(df['token_id'].unique())
    #High volume
    net = df.groupby(['token_id']).agg({'sale_price_usd': 'sum'}).reset_index() 
    net = net.nlargest(1,'sale_price_usd')
    #frequent_token
    frequent = df['token_id'].value_counts()[:3].index.tolist()
    
    col1.metric(label = "Unique Tokens", value = unique_tokens)
    col2.metric(label = "Highest sold Token ID  (volume)", value = net['token_id'].max())
    col3.metric(label = "Most transferred Token ID ", value = frequent[0])