import streamlit as st
import numpy as np
import pandas as pd
import requests, json


       
@st.cache(allow_output_mutation=True)
def load():
    df = pd.read_csv('./data/chicken_nft.csv')
    return df

@st.cache(allow_output_mutation=True)
def load_meta(x):
    url = f"https://api.covalenthq.com/v1/137/tokens/0x8634666ba15ada4bbc83b9dbf285f73d9e46e4c2/nft_metadata/{x}/?key=ckey_eb29565e970e4b46930dca374df"
    response = requests.request("GET", url)
    if response.status_code ==200:
        data1 = response.json()
        data1 = data1['data']['items']
        basic_data = data1[0]['nft_data']
        metadata = basic_data[0]['external_data']
        return metadata, basic_data
    else:
        return 'error', 'error'
        
