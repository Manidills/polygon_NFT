from hydralit import HydraApp
import streamlit as st
from PIL import Image
from stats import Stats
from home import Home
from tokens.toks import Token
from wallets.wallets import Wallet
from collection import Collection

#ckey_eb29565e970e4b46930dca374df

st.set_page_config(
    page_title="ETH Global hack",
    layout="wide"
)

#title_image = Image.open("/home/dills/Music/ethglobal/images/CryptoMode-Polygon-DeFi.jpg")
# new_title = '<p style="font-family:Bodoni; text-align: center; color:#FEB440; font-size: 60px;">POLYGON NFT ANALYZER</p>'
# st.markdown(new_title, unsafe_allow_html=True)


if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!

    app = HydraApp(title='ETH Global hack')
    
    #add all your application classes here
    app.add_app("Home", app=Home(),is_home=True)
    app.add_app("Collection", app = Collection())
    app.add_app("Token", app=Token())
    app.add_app("Wallet", app=Wallet())
    app.add_app("Stats", app=Stats())
    

    #run the whole lot
    app.run()