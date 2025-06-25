import streamlit as st
import pandas as pd
from datetime import date, timedelta

def set_exam_dates():
    exam_date = st.date_input(
            label="What are the first scheduled day for this exam?", 
            value="today",
            key="exam_date")
    next_date = exam_date+timedelta(days=1)
    while next_date.weekday() > 4:
        next_date += timedelta(days=1)
    date1, date2 = [date_.strftime("%d. %B, %Y") for date_ in (exam_date, next_date)]
    if exam_date.year == next_date.year:
        date1 = date1[:-6]
    return (date1, date2)

def generate_messages(df, row, keyword):
    keyword_dict = {
        "PCEP": {
            "name": "PCEP",
            "link": "https://edube.org/assign-voucher"
        },
        "Azure": {
            "name": "DP-900",
            "link": "https://learn.microsoft.com/en-us/credentials/certifications/schedule-through-pearson-vue?examUid=exam.DP-900&examUrl=https%3A%2F%2Flearn.microsoft.com%2Fcredentials%2Fcertifications"
        },
        "Scikit": {
            "name": "Scikit-learn Associate",
            "link": "https://www.webassessor.com/wa.do?page=enterCatalog&tabs=7"
        }
    }
    
    if row >= df.shape[0]:
        st.write("You're all done!")
        return 0
        
    if keyword == "LinkedIn":
        st.markdown(
            learning_message(df.iloc[row, 0].split()[0], df.iloc[row, 1], df.iloc[row, 2])
        )
    else:
        st.markdown(
            voucher_message(df.iloc[row, 0].split()[0], df.iloc[row, 1], keyword_dict[keyword])
        )    

def voucher_message(name, voucher, details):
    exam_dates = set_exam_dates()
    return f"""
    Hey {name},
        
    I'm writing to give you your voucher to [sign up for the {details["name"]} exam]({details["link"]}). Your voucher number is **{voucher}**.
        
    We've set aside two days for taking the exam during the course: **{exam_dates[0]} and {exam_dates[1]}**. It is very highly recommended that you take your exam by these dates, while the knowledge is still fresh in your mind. 
        
    Good luck!"""

def learning_message(name, username, password):
    return f"""
    Hi {name},
    
    I'm writing to provide you with access to LinkedIn Learning during the bootcamp. Access is granted until the end of your course.

    Start by going to [this link](https://ecampus50.wbstraining.de/). Follow the steps in [this video](https://drive.google.com/file/d/1C3rRbKxrIJhw21O61N0F5isH0FwnX6mU/view?usp=drive_link) to complete the login and access LinkedIn Learning.

    Your username is "{username}" and your password is "{password}"."""