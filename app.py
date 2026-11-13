import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Imbo Nomxesibe Hearty Meals", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=2200, scrolling=True)
