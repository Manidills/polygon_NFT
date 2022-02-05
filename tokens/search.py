import streamlit as st
import numpy as np
import pandas as pd
from load import load, load_meta
import requests, json


def search():
    input = st.text_input("Enter Token ID ",)

    if input:
        df = load()
        try:
            data = df[df['token_id'] == int(input)]
            data.drop(['token_id_hash','token_bundle_count','payment_token_address'], axis=1, inplace=True)
            url = f"https://api.covalenthq.com/v1/137/tokens/0x8634666ba15ada4bbc83b9dbf285f73d9e46e4c2/nft_metadata/{input}/?key=ckey_eb29565e970e4b46930dca374df"
            response = requests.request("GET", url)
            if response.status_code ==200:
                data1 = response.json()
                data1 = data1['data']['items']
                basic_data = data1[0]['nft_data']
                metadata = basic_data[0]['external_data']
            else:
                st.warning("error")
            st.markdown('####')
            col1, col2 = st.columns((4,3))
            with col1:
                data= data.set_index('created_at')
                st.info('Token Details')
                data['time'] = data.index
                data = data.sort_values(by="time")
                last_sold = data[data['is_sold'] == True]
                last_sold = last_sold['sale_price_usd'].iloc[-1]
                name = metadata['name']
                max_date = data['time'].max()
                avg_price = '$'+str(data['sale_price_usd'].mean())
                max_price = '$'+str(data['sale_price_usd'].max())
                original_owner= basic_data[0]['original_owner']
                current_owner = basic_data[0]['owner']
                burned = basic_data[0]['burned']
                att = metadata['attributes']
                st.text(f'Name = {name}')
                st.text(f'Last transaction date = {max_date}')
                st.text(f'Last price sold = {last_sold}')
                st.text(f'Max price sold = {max_price}')
                st.text(f'Initial owner = {original_owner}')
                st.text(f'Current owner = {current_owner}')
                st.text(f'Burned = {burned}')
                st.write(f'Attributes = {att}')
                st.success(f'Avg / Suggested price = {avg_price}')
            with col2:
                st.info('Token Image')
                st.image(metadata['image'],width=500,)
            st.markdown('####')
            st.info('Transaction details')
            st.dataframe(data)
            st.markdown('####')
            st.info('Price chart')
            
            st.line_chart(data['sale_price_eth'])
                    
                
                    
        except:
            st.warning("Info not found in DB")
    else:
        df = load()
        net = df.groupby(['token_id']).agg({'sale_price_usd': 'sum'}).reset_index() 
        net = net.nlargest(10,'sale_price_usd')
        net = net['token_id'].to_list()
        
        st.markdown("##")
        st.warning("Top 4 Most sold Token by volume")


        col1, col2= st.columns((3,3))
        with col1:
            try:
                meta, basic_data = load_meta(net[0])
                name = meta['name']
                current_owner = basic_data[0]['owner']
                token_id = basic_data[0]['token_id']
                att = meta['attributes']
                st.image(meta['image'],width=300,)
                st.text(f'Current owner = {current_owner}')
                st.text(f'Token_id = {token_id}')
                st.text(f'Name = {name}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        with col2:
            try:
                meta, basic_data = load_meta(net[1])
                name = meta['name']
                current_owner = basic_data[0]['owner']
                token_id = basic_data[0]['token_id']
                att = meta['attributes']
                st.image(meta['image'],width=300,)
                st.text(f'Current owner = {current_owner}')
                st.text(f'Token_id = {token_id}')
                st.text(f'Name = {name}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")

        

        with col1:
            try:
                meta, basic_data = load_meta(net[2])
                name = meta['name']
                current_owner = basic_data[0]['owner']
                token_id = basic_data[0]['token_id']
                att = meta['attributes']
                st.image(meta['image'],width=300,)
                st.text(f'Current owner = {current_owner}')
                st.text(f'Token_id = {token_id}')
                st.text(f'Name = {name}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        with col2:
            try:
                meta, basic_data = load_meta(net[3])
                name = meta['name']
                current_owner = basic_data[0]['owner']
                token_id = basic_data[0]['token_id']
                att = meta['attributes']
                st.image(meta['image'],width=300,)
                st.text(f'Current owner = {current_owner}')
                st.text(f'Token_id = {token_id}')
                st.text(f'Name = {name}')
                st.info(f'Attributes = {att}')

            except:
                st.warning("Info not found")
        
        


