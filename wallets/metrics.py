import streamlit as st
import numpy as np
import pandas as pd
from load import load


def wal():
    df = load()
    col1, col2 = st.columns((1,5))
    unique_wallets = df[["seller", "buyer"]].values.ravel()
    unique_wallets = len(pd.unique(unique_wallets))
    net = df[df['event'] != 'mint']
    net_seller = net.groupby(['seller']).agg({'sale_price_eth': 'sum'}).reset_index() 
    net_seller = net_seller.nlargest(1,'sale_price_eth')
    net_buyer = net.groupby(['buyer']).agg({'sale_price_eth': 'sum'}).reset_index() 
    net_buyer = net_buyer.nlargest(1,'sale_price_eth')
    count = len(df)
    col1.metric(label = "UNIQUE_WALLETS", value = unique_wallets)
    col2.metric(label = "TOP SELLER BY VOLUME", value = net_seller['seller'].max())
    col1.metric(label = "TRANSACTION COUNTS", value = count)
    col2.metric(label = "TOP BUYER BY VOLUME", value = net_buyer['buyer'].max())