from hydralit import HydraHeadApp
import streamlit as st
from PIL import Image
from hydralit import HydraHeadApp
from metric import polygon_metric
from predict import predict

class Home(HydraHeadApp):
    def run(self):
        img = Image.open("images/cover.jpg")
        st.image(img,  caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

        st.markdown('#') 

        total_volume,daily_avg,weekly_avg = polygon_metric('./data/polygon_volume.csv')

        col1, col2, col3 = st.columns((3,3,3))
        col1.metric(label = "Total Volume", value = total_volume , delta = "+$0.25")
        col2.metric(label = "Average Daily Volume", value = daily_avg , delta = "+$3.00")
        col3.metric(label = "Average Weekly Volume", value = weekly_avg, delta = "-$1.25")

        st.markdown('#') 
        st.markdown("<h4 style='text-align: center; color: white;'>Polygon(MATIC)  Volume Prediction </h4>", unsafe_allow_html=True)

        file_path_ = './data/polygon_volume.csv'
        split_percent_ = 0.65
        predict_model_ =  './data/polygon_volume.h5'
        volume_chart = predict(file_path_,split_percent_,predict_model_)

        st.altair_chart(volume_chart)  

        st.info("Polygon Volume prediction")
        st.write("""
        In the chart above, which is set in a daily time frame of volume traded over the period of time, we can see the Ascending Channel Trend pattern, which is the price action that takes place \n 
        in an upward direction  across a sloping parallel line throughout the months of May, June and July. Furthermore, the chart depicts the price pattern's Higher Highs and Higher Lows since last year.\n
        Polygon Matic Price Prediction on January 26th, volume was expected to trade between 4.4 M and 4.55 M and The actual trade happened was around 4.9M, likewise\n
        Polygon Matic Price Prediction on January 27th, volume was expected to trade between 4.6 M and 5 M and The actual trade happened was around 4M.
        """)



        st.markdown('#')
        st.markdown("<h4 style='text-align: center; color: white;'>Polygon(MATIC)  Wallet Prediction </h4>", unsafe_allow_html=True)  
        file_path = './data/polygon_wallet.csv'
        split_percent = 0.65
        predict_model =  './data/polygon_wallet.h5'
        wallet_chart = predict(file_path,split_percent,predict_model)
        
        st.altair_chart(wallet_chart)  
        

        st.info("Polygon Wallet prediction")
        st.write("""
        In the chart above, which is set in a daily time frame of unique wallets over the period of time, we can also see here the Ascending Channel Trend pattern, the number of number unique wallet counts increased  \n 
        in the months of May, June and July, since the volume over this period of time was increased rapidly.\n
        Polygon unique wallet count Prediction on January 26th, unique wallets are expected between 55k and 57k and The actual unique wallet added was around 51k, similarly\n
        Polygon unique wallet count Prediction on January 27th, unique wallets are expected between 70k and 75k and The actual unique wallet added was around 65k, 
        """)

