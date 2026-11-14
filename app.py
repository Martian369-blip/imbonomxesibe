import streamlit as st

st.set_page_config(
    page_title="Imbo Nomxesibe Hearty Meals | Event Catering",
    page_icon="🍽️",
    layout="wide"
)

# Custom Styling: Goldish Yellow & Young Green Palette
st.markdown("""
<style>
    .stApp {
        background-color: #fefdf7;
        color: #1f241d;
    }
    .top-bar {
        background-color: #1f2b1c;
        color: #fef08a;
        padding: 10px 20px;
        border-radius: 6px;
        font-size: 0.9rem;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #eab308;
    }
    .hero-box {
        background: linear-gradient(135deg, #ca8a04 0%, #eab308 55%, #65a30d 100%);
        color: #ffffff;
        padding: 3.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 6px 18px rgba(161, 98, 7, 0.18);
    }
    .hero-box h1 {
        color: #ffffff !important;
        font-size: 2.4rem;
        margin-bottom: 0.75rem;
        text-shadow: 0 1px 4px rgba(0,0,0,0.25);
    }
    .hero-box p {
        color: #fefce8;
        font-size: 1.15rem;
        max-width: 750px;
        margin: 0 auto;
        text-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #fde047;
        border-top: 4px solid #eab308;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        height: 100%;
    }
    .card h3 {
        color: #a16207 !important;
        margin-top: 0;
    }
    .menu-card {
        background-color: #ffffff;
        border-left: 5px solid #65a30d;
        padding: 1.25rem;
        border-radius: 6px;
        border-top: 1px solid #fef08a;
        border-right: 1px solid #fef08a;
        border-bottom: 1px solid #fef08a;
        margin-bottom: 1rem;
    }
    .menu-card h4 {
        color: #854d0e !important;
        margin-bottom: 0.4rem;
    }
    .badge {
        display: inline-block;
        background-color: #ecfccb;
        color: #3f6212;
        border: 1px solid #bef264;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .whatsapp-btn {
        display: inline-block;
        background-color: #65a30d;
        color: #ffffff !important;
        padding: 0.65rem 1.25rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 700;
        margin-top: 0.5rem;
    }
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

# Initialize Sample Portfolio Data
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
    <span><strong>Imbo Nomxesibe Hearty Meals</strong> — Mfuleni, Cape Town</span>
    <span>Tel / WhatsApp: 073 379 1648 | Email: thenjinjoli@gmail.com</span>
</div>
""", unsafe_allow_html=True)

# Navigation Menu
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
        <p>Based in Mfuleni, Cape Town, we bring generous, freshly prepared South African and continental meals to school functions, government events, and corporate meetings.</p>
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
            "Whether feeding learners and staff at a school function, hosting state delegates, or catering an executive meeting, "
            "we prepare every meal with care, generous portions, and strict hygiene standards."
        )
        st.markdown("""
        - **High-Volume Capacity:** Equipped to cater smoothly for small boardrooms up to large institutional gatherings.
        - **Institutional & Corporate Ready:** Tailored service for schools, government departments, and private companies across Cape Town.
        - **Flexible Menu Options:** Custom buffets, morning platters, and individual lunch packs available on quote.
        - **Reliable Delivery & Setup:** Punctual service from our Mfuleni base to your event venue.
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
            <p>Dignified, dependable catering for municipal gatherings, departmental conferences, community outreach programs, and official state functions.</p>
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
    st.subheader("Sample Menu Selections (Custom Quotes Available)")
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
            <p>Multi-course plated service featuring starters, prime cuts or grilled linefish with seasonal sides, and classic desserts like Malva pudding.</p>
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
        st.success("**Punctual & Dependable**\n\nWe respect strict school bells, government itineraries, and corporate agendas—your food arrives hot and ready on schedule.")
    with w2:
        st.warning("**Generous Portions**\n\nWe use fresh, quality ingredients and never compromise on portion sizes, ensuring every guest leaves satisfied.")
    with w3:
        st.success("**Tailored Quotes**\n\nContact us on **073 379 1648** or via the **Contact Us** tab for a custom menu proposal tailored to your guest count.")

# ==========================================
# PAGE 2: OUR PORTFOLIO (MANUAL UPLOAD)
# ==========================================
elif page == "Our Portfolio":
    st.header("Event Portfolio & Past Projects")
