import streamlit as st

st.set_page_config(
    page_title="Imbo Nomxesibe Hearty Meals | Home",
    page_icon="🍽️",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background-color: #fefdf7; color: #1f241d; }
    .top-bar {
        background-color: #1f2b1c;
        color: #fef08a;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 0.9rem;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #eab308;
    }
    .hero-box {
        background: linear-gradient(135deg, #ca8a04 0%, #eab308 55%, #65a30d 100%);
        color: #ffffff;
        padding: 4rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 6px 18px rgba(161, 98, 7, 0.18);
    }
    .hero-box h1 { color: #ffffff !important; font-size: 2.5rem; margin-bottom: 0.75rem; }
    .hero-box p { color: #fefce8; font-size: 1.15rem; max-width: 750px; margin: 0 auto; }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #fde047;
        border-top: 4px solid #eab308;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        height: 100%;
    }
    .card h3 { color: #a16207 !important; margin-top: 0; }
    .footer-box {
        background-color: #1f2b1c;
        color: #fefce8;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
        border-top: 4px solid #eab308;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-bar">
    <span><strong>Imbo Nomxesibe Hearty Meals</strong> — Mfuleni, Cape Town</span>
    <span>Tel / WhatsApp: 073 379 1648 | Email: thenjinjoli@gmail.com</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <p style="text-transform: uppercase; letter-spacing: 2px; font-weight: bold; font-size: 0.85rem; margin-bottom: 0.5rem;">Welcome to Imbo Nomxesibe Hearty Meals</p>
    <h1>Hearty, Dependable Catering for Schools, State & Corporate Events</h1>
    <p>From Mfuleni to Greater Cape Town, we deliver generous, freshly cooked meals tailored for institutional gatherings, government functions, and executive boardrooms.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("What We Do Best")
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown("""
    <div class="card">
        <h3>School Events</h3>
        <p>Wholesome, crowd-pleasing meals for awards ceremonies, sports tournaments, staff workshops, and matric functions.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="card">
        <h3>State & Government Events</h3>
        <p>Reliable, dignified catering for municipal gatherings, departmental conferences, and community outreach programs.</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="card">
        <h3>Corporate Meetings</h3>
        <p>Punctual morning platters, executive working lunches, and boardroom refreshments delivered fresh on schedule.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.info("👈 Use the **left sidebar menu** to explore **About Us**, view our **Portfolio**, or visit **Contact Us** to request a custom quote.")

st.markdown("""
<div class="footer-box">
    <h4 style="color: #fde047; margin-bottom: 0.4rem;">Imbo Nomxesibe Hearty Meals</h4>
    <p style="font-size: 0.9rem; margin-bottom: 0.3rem;">22661 Nosethu Street, Mfuleni, Cape Town, 7100</p>
    <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">Tel / WhatsApp: 073 379 1648 | Email: thenjinjoli@gmail.com</p>
    <p style="font-size: 0.8rem; color: #bef264;">&copy; 2026 Imbo Nomxesibe Hearty Meals. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
