import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
# from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class

class Stats(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #-------------------existing untouched code------------------------------------------
        Current_Date = datetime.datetime.today().strftime ('%Y-%m-%d')
        Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
        Previous_Date = Previous_Date.strftime ('%Y-%m-%d')
        input = st.text_input("Enter Contract address ",)
        
            

        if input:
            @st.cache
            def contract_api():
                url = f"https://api.covalenthq.com/v1/137/nft_market/collection/{input}/?key=ckey_eb29565e970e4b46930dca374df"
                response = requests.request("GET", url)
                if response.status_code ==200:
                    data = response.json()
                    data = data['data']['items']
                    df = pd.DataFrame(data)
                    #df.drop(['volume_wei_24h', 'volume_quote_24h','avg_volume_wei_24h','avg_volume_quote_24h'],axis=1, inplace=True)
                    return df
                else:
                    st.info("something wrong")
            
        #     gb = GridOptionsBuilder.from_dataframe(contract_api())
        #     gb.configure_pagination()
        #     gb.configure_grid_options(rowHeight=50)
        #     gridOptions = gb.build()

        #     AgGrid(contract_api(), gridOptions=gridOptions, height=800
        #  )
        
        else:
            @st.cache
            def api():
                url = f"https://api.covalenthq.com/v1/137/nft_market/?quote-currency=USD&format=JSON&from={Previous_Date}&to={Current_Date}&key=ckey_eb29565e970e4b46930dca374df"
                response = requests.request("GET", url)
                if response.status_code ==200:
                    data = response.json()
                    data = data['data']['items']
                    df = pd.DataFrame(data)
                    df.drop(['volume_wei_24h', 'volume_quote_24h','avg_volume_wei_24h','avg_volume_quote_24h'],axis=1, inplace=True)
                    return df
                else:
                    st.info("something wrong")
            st.info('All Collection Info')
            # gb = GridOptionsBuilder.from_dataframe(api())
            # gb.configure_pagination()
            # gb.configure_grid_options(rowHeight=50)
            # gridOptions = gb.build()
            # AgGrid(api(), gridOptions=gridOptions, height=800 )

        