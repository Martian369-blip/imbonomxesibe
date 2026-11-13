import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Imbo Nomxesibe Hearty Meals",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit margins and header padding
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
