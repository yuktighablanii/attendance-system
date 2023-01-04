import streamlit as st
import os

st.set_page_config(
    page_title="Attendance Management",
    page_icon="🎓",
)
st.title("Attendance Management System")
st.sidebar.success("Select a page above.")

if "Name" not in st.session_state:
    st.session_state["Name"] = ""

Name = st.text_input("Enter Student Name", st.session_state["Name"])



if "Roll_No" not in st.session_state:
    st.session_state["Roll_No"] = ""

Roll_No = st.text_input("Enter Roll Number", st.session_state["Roll_No"])


if "Email_id" not in st.session_state:
    st.session_state["Email_id"] = ""

Email_id = st.text_input("Enter college Email ID", st.session_state["Email_id"])


if "Phone" not in st.session_state:
    st.session_state["Phone"] = ""

Phone = st.text_input("Enter Contact Number", st.session_state["Phone"])




if "Password" not in st.session_state:
    st.session_state["Password"] = ""

Password = st.text_input("Enter Password", st.session_state["Password"])


uploadedfile = st.file_uploader(label = "Upload image here")

submit = st.button("Submit")
if submit:
    st.session_state["Password"] = Password
    st.session_state["Roll_No"] = Roll_No
    st.session_state["Name"] = Name
    st.session_state["Email_id"] = Email_id
    st.session_state["Phone"] = Phone

    if uploadedfile is not None:
        with open(os.path.join("uploadedImages",uploadedfile.name),"wb") as f:
            f.write(uploadedfile.getbuffer())
        st.success("Images uploaded")
    st.success("Image Not Uploaded")

