import pandas as pd
import streamlit as st
import requests as rq
import matplotlib.pyplot as plt
import datetime as dt

st.set_page_config(page_title ="Weather History Dashboard",
                   page_icon ="🌦️",
                   layout="centered")
st.title=("🌍 Global Weather History Dashboard")
st.write=("Analyse **monthly historical temperature and precipitation data**, valid data till 2024 only")


