import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
import re

url = "https://pastebin.com/psRsW3fL"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
meet = soup.find_all("div", class_="de1")

#remove html tags
meet = str(meet)
meet = re.sub('<[^>]*>', '', meet)
meet = meet.replace('[', '')
meet = meet.replace(']', '')
meet = meet.replace(' ', '')


st.title("Meeting Links")
if st.button("Join Meeting"):
    webbrowser.open(f"{meet}")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
