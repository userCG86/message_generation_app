import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def fetch_data(spreadsheet, keyword):
    conn = st.connection("gsheets", type=GSheetsConnection)

    if keyword == "LinkedIn":
        df = conn.read(spreadsheet=spreadsheet, worksheet="LinkedIn Learning")[["Vorname", "Username", "Password"]].dropna(subset="Password")
    else:
        df = conn.read(spreadsheet=spreadsheet, worksheet="Vouchers", header=[0,1])[[("Student","Unnamed: 0_level_1"), (keyword, "Voucher")]]

    return df