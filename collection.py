from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
from hydralit import HydraHeadApp
from metric import polygon_metric,chicken_metric
from predict import predict

class Collection(HydraHeadApp):

    def run(self):
        values = ["Chicken Derby"]
        default_ix = values.index("Chicken Derby")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)

        img = Image.open("./images/chicken.JPG")
        st.image(img,  caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

        st.markdown('#') 

        total_volume,daily_avg,weekly_avg = chicken_metric('./data/chicken_nft_volume.csv')

        col1, col2, col3 = st.columns((3,3,3))
        col1.metric(label = "Total Volume", value = total_volume , delta = "+$0.25")
        col2.metric(label = "Average Daily Volume", value = daily_avg , delta = "+$3.00")
        col3.metric(label = "Average Weekly Volume", value = weekly_avg, delta = "-$1.25")

        st.markdown('#') 

        file_path_ = './data./chicken_nft_volume.csv'
        split_percent_ = 0.75
        predict_model_ =  './data/volume.h5'
        volume_chart = predict(file_path_,split_percent_,predict_model_)

        st.altair_chart(volume_chart)  
        st.markdown("<h4 style='text-align: center; color: white;'>Chicken Derby Volume Prediction </h4>", unsafe_allow_html=True)
        
        st.markdown('#') 
        file_path = './data/chicken_nft_wallet.csv'
        split_percent = 0.75
        predict_model =  './data/wallet.h5'
        wallet_chart = predict(file_path,split_percent,predict_model)
        
        st.altair_chart(wallet_chart)  
        st.markdown("<h4 style='text-align: center; color: white;'>Chicken Derby Wallet Prediction </h4>", unsafe_allow_html=True) 


