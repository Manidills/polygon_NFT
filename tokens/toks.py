import streamlit as st
import numpy as np
import pandas as pd
from .metrics import metrics
from .search import search
#add an import to Hydralit
from hydralit import HydraHeadApp



#create a wrapper class

class Token(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        values = ["Chicken Derby"]
        default_ix = values.index("Chicken Derby")
        window_ANTICOR = st.selectbox('Select', values, index=default_ix)
        metric = metrics()
        check = search()
       

        

        

