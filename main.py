import streamlit as st
import requests
from bs4 import BeautifulSoup


st.title("Meeting Links")
st.button("Join Meeting")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
