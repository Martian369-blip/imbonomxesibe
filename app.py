import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Imbo Nomxesibe Hearty Meals | Event Catering",
    page_icon="🍽️",
    layout="wide"
)

# Custom Styling inspired by Fork & Nice
st.markdown("""
<style>
    .stApp {
        background-color: #faf8f5;
        color: #1c1917;
    }
    .top-bar {
        background-color: #1c1917;
        color: #e7e5e4;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 0.9rem;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        margin-bottom: 1.5rem;
    }
    .hero-box {
        background: linear-gradient(135deg, #632712 0%, #8b3a1d 100%);
        color: #ffffff;
        padding: 3.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero-box h1 {
        color: #ffffff !important;
        font-size: 2.4rem;
        margin-bottom: 0.75rem;
    }
    .hero-box p {
        color: #fef3c7;
        font-size: 1.15rem;
        max-width: 750px;
        margin: 0 auto;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e7e5e4;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        height: 100%;
    }
    .card h3 {
        color: #8b3a1d !important;
        margin-top: 0;
    }
    .menu-card {
        background-color: #ffffff;
        border-left: 5px solid #8b3a1d;
        padding: 1.25rem;
        border-radius: 6px;
        border-top: 1px solid #e7e5e4;
        border-right: 1px solid #e7e5e4;
        border-bottom: 1px solid #e7e5e4;
        margin-bottom: 1rem;
    }
    .badge {
        display: inline-block;
        background-color: #fef3c7;
        color: #92400e;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .footer-box {
        background-color: #1c1917;
        color: #d6d3d1;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Portfolio Data in Session State
if "portfolio" not in st.session_state:
    st.session_state.portfolio = [
        {
            "title": "Annual High School Awards & Staff Banquet",
            "category": "School Event",
            "guests": "240 Guests • School Hall",
            "image": "https://unsplash.com",
            "summary": "Full buffet setup featuring slow-roasted herb chicken, beef stew, savoury rice, fresh garden salads, and warm Malva pudding for educators, parents, and top achievers."
        },
        {
            "title": "Provincial Departmental Stakeholder Imbizo",
            "category": "State Event",
            "guests": "350 Delegates • Civic Centre",
            "image": "https://unsplash.com",
            "summary": "Morning tea and scone arrival stations followed by a two-course hearty traditional lunch served simultaneously across four buffet lines."
        },
        {
            "title": "Quarterly Corporate Strategy & Boardroom Summit",
            "category": "Corporate Meeting",
            "guests": "45 Executives • Office Park",
            "image": "https://unsplash.com",
            "summary": "Artisanal breakfast wraps, gourmet sandwich platters, grilled chicken skewers, and individual plated hot lunches delivered promptly for executive sessions."
        }
    ]

# Top Contact Bar
st.markdown("""
<div class="top-bar">
    <span><strong>Imbo Nomxesibe Hearty Meals</strong> — School, State & Corporate Catering</span>
    <span>Tel: 000 000 0000 | Email: info@imbonomxesibe.co.za</span>
</div>
""", unsafe_allow_html=True)

# Top Navigation Tabs
page = st.radio(
    "Navigation",
    ["Home", "Our Portfolio", "Contact Us"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# ==========================================
# PAGE 1: HOME
# ==========================================
if page == "Home":
    st.markdown("""
    <div class="hero-box">
        <p style="text-transform: uppercase; letter-spacing: 2px; font-weight: bold; font-size: 0.85rem; margin-bottom: 0.5rem;">Welcome to Imbo Nomxesibe Hearty Meals</p>
        <h1>Wholesome, Reliable Catering for Schools, State & Corporate Events</h1>
        <p>We bring generous, freshly prepared South African and continental meals to institutional gatherings, executive boardrooms, and community functions—delivered on time and with professional service.</p>
    </div>
    """, unsafe_allow_html=True)

    # About Section
    col1, col2 = st.columns([1, 1.2], gap="large")
    with col1:
        st.image(
            "https://unsplash.com",
            use_container_width=True
        )
    with col2:
        st.subheader("About Imbo Nomxesibe Hearty Meals")
        st.write(
            "At **Imbo Nomxesibe Hearty Meals**, we believe great food brings people together and fuels productive, memorable events. "
            "Whether feeding hundreds of learners at a school sports day, hosting dignified state delegates, or catering an executive strategy session, "
            "we treat every function with precision and pride."
        )
        st.markdown("""
        - **High-Volume Capacity:** Equipped to cater smoothly for 20 to 1,000+ guests.
        - **Procurement Ready:** Compliant with school, municipal, and corporate standards.
        - **Flexible Menus:** Halaal-friendly, vegetarian, and special dietary options available.
        - **Full-Service Logistics:** Chafing dishes, crockery, uniformed servers, and cleanup included.
        """)

    st.write("")
    st.subheader("Events We Specialize In")
    s1, s2, s3 = st.columns(3, gap="medium")
    with s1:
        st.markdown("""
        <div class="card">
            <h3>School Events</h3>
            <p>Nutritious, crowd-pleasing meals for prize-giving ceremonies, parent-teacher meetings, sports tournaments, matric farewells, and educator workshops.</p>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="card">
            <h3>State & Government Events</h3>
            <p>Dignified, reliable catering for municipal imbizo gatherings, departmental conferences, community outreach programs, and official functions.</p>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="card">
            <h3>Corporate Meetings</h3>
            <p>Punctual breakfast platters, executive working lunches, boardroom refreshments, and year-end functions that keep your team energized.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Hearty Dining & Menu Selections")
    m1, m2 = st.columns(2, gap="medium")
    with m1:
        st.markdown("""
        <div class="menu-card">
            <h4>Corporate & Morning Platters</h4>
            <p>Freshly baked muffins, assorted gourmet sandwiches, savoury samoosas, chicken skewers, seasonal fruit platters, and tea/coffee stations.</p>
        </div>
        <div class="menu-card">
            <h4>Traditional & Hearty Buffets</h4>
            <p>Slow-cooked beef stew, roasted herb chicken, lamb curry, fragrant savoury rice, creamy samp & beans, roasted vegetables, and fresh salads.</p>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown("""
        <div class="menu-card">
            <h4>VIP & State Plated Dining</h4>
            <p>Three-course plated service featuring starters, prime cuts or grilled linefish with seasonal sides, and classic desserts like Malva pudding.</p>
        </div>
        <div class="menu-card">
            <h4>School & Event Lunch Packs</h4>
            <p>Hygienically sealed individual meal boxes containing juicy burgers, wors rolls, or quarter-chicken & chips with a bottled beverage.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Why Choose Imbo Nomxesibe?")
    w1, w2, w3 = st.columns(3, gap="medium")
    with w1:
        st.info("**Punctual & Dependable**\n\nWe respect strict school bells, government itineraries, and corporate agendas—your food arrives hot and ready on schedule.")
    with w2:
        st.info("**Generous Portions**\n\nWe use fresh, locally sourced ingredients and never compromise on portion sizes, ensuring every guest leaves satisfied.")
    with w3:
        st.info("**What Our Clients Say**\n\n*\"Imbo Nomxesibe catered for over 250 guests at our school awards ceremony. Piped hot, well-seasoned, and right on time.\"*")

# ==========================================
# PAGE 2: OUR PORTFOLIO (WITH MANUAL UPLOAD)
# ==========================================
elif page == "Our Portfolio":
    st.header("Event Portfolio & Past Projects")
    st.write("Browse summaries of school, state, and corporate events catered by **Imbo Nomxesibe Hearty Meals**, or add new entries manually below.")

    # Manual Portfolio Entry Form
    with st.expander("➕ Add New Portfolio Event (Manual Entry)", expanded=False):
        with st.form("manual_portfolio_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                p_title = st.text_input("Event Title *", placeholder="e.g. Regional Department Summit Luncheon")
                p_category = st.selectbox("Event Category *", ["School Event", "State Event", "Corporate Meeting"])
                p_guests = st.text_input("Guests Served & Venue/Date *", placeholder="e.g. 180 Guests • November 2026")
            with c2:
