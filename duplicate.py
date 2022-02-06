from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
import requests
import json
from hydralit import HydraHeadApp
from metric import polygon_metric
from predict import predict
from load import load_meta

class Duplicate(HydraHeadApp):
    def run(self):
        values = ["Chicken Derby"]
        default_ix = values.index("Chicken Derby")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)
        input = st.text_input("Enter Token Id ",)
        if input:
            url = "https://api.nftport.xyz/v0/duplicates/tokens"
            payload = {
                "chain": 'polygon',
                "contract_address": '0x8634666ba15ada4bbc83b9dbf285f73d9e46e4c2',
                "token_id": str(input),
                "page_number": 1,
                "page_size": 5,
                "threshold": 0.99
            }

            headers = {
                'Content-Type': "application/json",
                'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
                }

            response = requests.request("POST", url, data=json.dumps(payload), headers=headers, json=True)

            data = response.json()
            if data['response'] == 'OK':
                data = data['similar_nfts']
                req = []
                for i in range(len(data)):
                    if not data[i]['token_id'] == input:
                        req.append(data[i])
                req = [k for j, k in enumerate(req) if k not in req[j + 1:]]
                top_2 = [{"image" : i['cached_file_url'], 'token_id': i['token_id'], 'metadata': i['metadata']} for i in req ]
                top_2 = top_2[:2]
            else:
                st.warning("something went wrong")

            co1, co2 = st.columns((3,3))
            metadata, basicdata = load_meta(str(input))

            with co1:
                st.image(metadata['image'],width=400,)
            with co2:
                name = metadata['name']
                current_owner = basicdata[0]['owner']
                token_id = basicdata[0]['token_id']
                att = metadata['attributes']
                st.text(f'Current owner = {current_owner}')
                st.text(f'Token_id = {token_id}')
                st.text(f'Name = {name}')
                st.info(f'Attributes = {att}')
            
            st.markdown("####")
            st.info("Near Duplicates")
            col1,col2 = st.columns((3,3))
            with col1:
                st.image(top_2[0]['image'],width=400,)
                st.info(f"Token Id = {top_2[0]['token_id']}")
                st.success(f"Metadata = {top_2[0]['metadata']}")
                st.write(f"check out this [link](https://opensea.io/assets/matic/0x8634666ba15ada4bbc83b9dbf285f73d9e46e4c2/{top_2[0]['token_id']})")

            with col2:
                st.image(top_2[1]['image'],width=400)
                st.info(f"Token Id = {top_2[1]['token_id']}")
                st.success(f"Metadata = {top_2[1]['metadata']}")
                st.write(f"check out this [link](https://opensea.io/assets/matic/0x8634666ba15ada4bbc83b9dbf285f73d9e46e4c2/{top_2[1]['token_id']})")
