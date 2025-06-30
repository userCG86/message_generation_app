import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from data_read import fetch_data
from utils import *

if "row" not in st.session_state:
    st.session_state["row"] = 0

st.title("Generate voucher messages for your batch!")

purpose = st.selectbox(
    label="Which exam would you like to generate messages for?", 
    options=["PCEP", "Azure DP-900", "Scikit-learn Associate"], 
    index=None)

if purpose:
    keyword = purpose.split()[0].split("-")[0]

    if (spreadsheet := st.text_input(f"Enter the instructor comments sheet URL")):
        df = fetch_data(spreadsheet, keyword)
        st.markdown("---")
        
        generate_messages(df, st.session_state["row"], keyword)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state["row"] > 0:
                if st.button("Previous message"):
                    st.session_state["row"] -= 1
                    st.rerun()
        with col2:
            if st.session_state["row"] < df.shape[0]:
                if st.button("Next message"):
                    st.session_state["row"] += 1
                    st.rerun()
        

