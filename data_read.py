import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def fetch_data(spreadsheet, keyword):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=spreadsheet, worksheet="Vouchers", header=[0,1])[[("Unnamed: 0_level_0","Unnamed: 0_level_1"), (keyword, "Voucher")]]

    return df