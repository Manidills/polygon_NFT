from email.mime import image
import streamlit as st
import altair as alt
import datetime
import numpy as np
import pandas as pd
from load import load, load_meta, nfts
import requests, json


def search():
    input = st.text_input("Enter Wallet address ",)
    

    if input:
        
        try:
            df = load()
            st.markdown('####')
            data = df[(df['seller'] == str(input)) | (df['buyer'] == str(input)) ]
            data1= data[data['is_sold'] == True]
            st.info("Wallet Summary")
            Trans_count = len(data[data['event'] == 'transfer'])
            mint_count = len(data[data['event'] == 'mint'])
            coin = data['token_symbol'].value_counts().idxmax()
            data2 = data[data['seller'] != '0x0000000000000000000000000000000000000000']
            interacted = data2.groupby(['seller','buyer']).size().idxmax()
            max_value = data['sale_price_eth'].max()
            min_value = data1['sale_price_eth'].min()
            avg_value = data['sale_price_eth'].mean()
            overall = data['sale_price_eth'].sum()
            st.text(f"Total Transactions Counts = {Trans_count}")
            st.text(f"Mint Counts = {mint_count}")
            st.text(f'Most Used Token Symbol = {coin}')
            st.text(f"Most Interacted Wallet = {interacted}")
            st.text(f"Max Sale = {max_value}" + "ETH")
            st.text(f"Min Sale = {min_value}" + 'ETH')
            st.text(f"Avg Sale = {avg_value}" + 'ETH')
            st.success(f"Overall Sale Volume = {overall}" + 'ETH')
            st.markdown('####')
            st.info("Transaction Table")
            st.dataframe(data)
            data1['created_at'] = pd.to_datetime(data1['created_at'])
            data1['date'] = data1['created_at'].dt.date
            data1 = data1.sort_values(by="date")
            line = alt.Chart(data1).mark_bar().encode(
                    x = 'date',
                    y = 'sale_price_eth'
                ).properties(width = 1100, height = 400, ).interactive()
            st.markdown('####')
            st.info('Sale Chart')
            st.altair_chart(line)

            st.info('Holding tokens')

            holding_nfts = nfts(str(input))

            if not holding_nfts:
                st.warning("Address currently not holding any NFTS in chicken derby")
            else:
                df = pd.DataFrame(holding_nfts)
                st.dataframe(df)

           
           

            


        except:
            st.warning("Info not found in DB")
    else:
        df = load()
        df['created_at'] = pd.to_datetime(df['created_at'])
        df.sort_values(by='created_at',ascending=False, inplace=True)
        st.markdown("####")
        st.info("Recent 100 Transaction")
        st.dataframe(df.head(100), height=900)