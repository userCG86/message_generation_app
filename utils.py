import streamlit as st
import pandas as pd
from datetime import date, timedelta

def set_exam_dates(days):
    first_date = st.date_input(
            label="What is the first scheduled day for this exam?", 
            value="today",
            key="exam_date")
    
    next_date = skip_weekends(first_date+timedelta(days=1))
    last_date = ""
    exam_dates = [first_date, next_date, last_date]
    
    if days == "three":
        last_date = skip_weekends(next_date+timedelta(days=1))
        exam_dates[-1] = last_date
    
    try:
        test_dates = [date_.strftime("%d. %B, %Y") for date_ in exam_dates]
        if next_date.year == last_date.year:
            test_dates[1] = test_dates[1][:-6]
    except AttributeError:
        test_dates = [date_.strftime("%d. %B, %Y") for date_ in exam_dates[:2]]
    
    if first_date.year == next_date.year:
            test_dates[0] = test_dates[0][:-6]
    return test_dates

def skip_weekends(date_):
    while date_.weekday() > 4:
        date_ += timedelta(days=1)
    return date_

def generate_messages(df, row, keyword):
    keyword_dict = {
        "PCEP": {
            "name": "PCEP",
            "link": "https://edube.org/assign-voucher",
            "days": "three",
            "retries": "one retake"
        },
        "Azure": {
            "name": "DP-900",
            "link": "https://learn.microsoft.com/en-us/credentials/certifications/schedule-through-pearson-vue?examUid=exam.DP-900&examUrl=https%3A%2F%2Flearn.microsoft.com%2Fcredentials%2Fcertifications",
            "days": "two",
            "retries": "no retakes"
        },
        "Scikit": {
            "name": "Scikit-learn Associate",
            "link": "https://www.webassessor.com/wa.do?page=enterCatalog&tabs=7",
            "days": "two",
            "retries": "no retakes"
        }
    }
    
    if row >= df.shape[0]:
        st.write("You're all done!")
        return 0
        
    else:
        st.markdown(
            voucher_message(df.iloc[row, 0].split()[0], df.iloc[row, 1], keyword_dict[keyword])
        )
        return 0

def voucher_message(name, voucher, details):
    exam_dates = set_exam_dates(details["days"])
    return f"""
    Hey {name},
        
    I'm writing to give you your voucher to [sign up for the {details["name"]} exam]({details["link"]}). Your voucher number is **{voucher}**. Your voucher includes *{details["retries"]}*.
        
    We've set aside {details["days"]} days for taking the exam during the course: **{", ".join(exam_dates[0:-1])} and {exam_dates[-1]}**. Take your exam by these dates, while the knowledge is still fresh in your mind. 
        
    Good luck!"""

