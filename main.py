from hydralit import HydraApp
import streamlit as st
from PIL import Image
from stats import Stats
from home import Home
from tokens.toks import Token
from wallets.wallets import Wallet
#ckey_eb29565e970e4b46930dca374df

st.set_page_config(
    page_title="NFT",
    layout="wide"
)

title_image = Image.open("/home/dills/Music/ethglobal/images/CryptoMode-Polygon-DeFi.jpg")
#st.image(title_image, width=1000, height=1500)
#fil = '<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;text-align: center;">NFT MARKETCAP</p>'
new_title = '<p style="font-family:Bodoni; text-align: center; color:#FEB440; font-size: 60px;">POLYGON NFT ANALYZER</p>'
st.markdown(new_title, unsafe_allow_html=True)


if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='Sample Hydralit App',favicon="🐙")

    
    #add all your application classes here
    app.add_app("🐵", app = Home())
    app.add_app("Token", icon="😉", app=Token())
    app.add_app("Wallet", icon="😀", app=Wallet())
    app.add_app("Stats Table", icon="😀", app=Stats())
    
    

    #run the whole lot
    app.run()