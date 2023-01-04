import streamlit as st
import os
import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

st.set_page_config(
    page_title="Attendance Management",
    page_icon="🎓",
)
st.title("Attendance Management System")
st.sidebar.success("Select a page above.")



# --- USER AUTHENTICATION ---
names = ["Yukti", "Shivam"]
usernames = ["yukti", "shivam"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
     st.warning("Please enter your username and password")

if authentication_status:
    if "Roll_No" not in st.session_state:
        st.session_state["Roll_No"] = ""

    Roll_No = st.text_input("Enter Roll Number", st.session_state["Roll_No"])


    if "Password" not in st.session_state:
        st.session_state["Password"] = ""

    Password = st.text_input("Enter Password", st.session_state["Password"])
    submit = st.button("Submit")
    if submit:
        st.session_state["Password"] = Password
        st.session_state["Roll_No"] = Roll_No
    st.success("Authenticated")
