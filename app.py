import streamlit as st

st.set_page_config(
    page_title="Imbo Nomxesibe Hearty Meals | Event Catering",
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
        gap: 10px;
        margin-bottom: 1rem;
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
    .hero-box h1 { color: #ffffff !important; font-size: 2.4rem; margin-bottom: 0.75rem; }
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
    .menu-card {
        background-color: #ffffff;
        border-left: 5px solid #65a30d;
        padding: 1.25rem;
        border-radius: 6px;
        border: 1px solid #fef08a;
        margin-bottom: 1rem;
    }
    .menu-card h4 { color: #854d0e !important; margin-bottom: 0.4rem; }
    .placeholder-banner {
        background-color: #fef9c3;
        border: 2px dashed #eab308;
        border-radius: 10px;
        padding: 2.2rem 1rem;
        text-align: center;
        color: #854d0e;
        margin-bottom: 0.75rem;
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
    .contact-hero {
        background: linear-gradient(135deg, #1f2b1c 0%, #365314 60%, #ca8a04 100%);
        color: #ffffff;
        padding: 2.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    .profile-card {
        background-color: #ffffff;
        padding: 1.75rem;
        border-radius: 10px;
        border: 1px solid #fde047;
        border-left: 6px solid #eab308;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }
    .step-box {
        background-color: #f7fee7;
        border: 1px solid #bef264;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .whatsapp-cta {
        display: block;
        text-align: center;
        background-color: #65a30d;
        color: #ffffff !important;
        padding: 0.85rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 1rem;
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
    /* Style the top navigation tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #fef9c3;
        padding: 8px 12px;
        border-radius: 8px;
        border: 1px solid #fde047;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 700;
        color: #1f2b1c;
    }
</style>
""", unsafe_allow_html=True)

# Top Contact Bar
st.markdown("""
<div class="top-bar">
    <span><strong>Imbo Nomxesibe Hearty Meals</strong> — Mfuleni, Cape Town</span>
    <span>Tel / WhatsApp: 073 379 1648 | Email: thenjinjoli@gmail.com</span>
</div>
""", unsafe_allow_html=True)

# Clickable Top Tabs (Single-File Navigation)
tab_home, tab_about, tab_portfolio, tab_contact = st.tabs([
    "🏠 Home",
    "🍲 About Us",
    "📸 Portfolio",
    "📞 Contact Us"
])

# ==========================================
# TAB 1: HOME
# ==========================================
with tab_home:
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

# ==========================================
# TAB 2: ABOUT US
# ==========================================
with tab_about:
    st.header("About Imbo Nomxesibe Hearty Meals")
    st.write("Rooted in hospitality, generous portions, and dependable event execution across Cape Town.")
    st.divider()

    col1, col2 = st.columns([1.2, 1], gap="large")
    with col1:
        st.subheader("Our Story & Mission")
        st.write(
            "Founded in **Mfuleni, Cape Town**, **Imbo Nomxesibe Hearty Meals** was built on a simple commitment: "
            "to serve generous, home-style South African and continental meals with the reliability that institutions and businesses depend on."
        )
        st.write(
            "Whether catering for 30 executives in a boardroom or 500+ attendees at a school or state function, "
            "we prepare every meal with care, strict hygiene standards, and punctual delivery."
        )
        st.markdown("""
        ### Our Core Standards
        - **High-Volume Cooking Capacity:** Equipped to scale smoothly for large institutional and municipal events.
        - **Strict Food Hygiene & Safety:** Fresh ingredients prepared in clean, compliant kitchen facilities.
        - **Punctual Delivery Guarantee:** Aligned with strict school timetables, government programs, and meeting agendas.
        - **Custom Dietary Care:** Halaal-friendly, vegetarian, and health-conscious meal options available upon request.
        """)

    with col2:
        st.subheader("Sample Menu Selections")
        st.caption("All menus are customizable and quoted according to your event size and preferences.")
        st.markdown("""
        <div class="menu-card">
            <h4>Corporate & Morning Platters</h4>
            <p>Freshly baked muffins, gourmet sandwich assortments, savoury samoosas, chicken skewers, seasonal fruit platters, and tea/coffee stations.</p>
        </div>
        <div class="menu-card">
            <h4>Traditional & Hearty Buffets</h4>
            <p>Slow-cooked beef stew, roasted herb chicken, lamb curry, fragrant savoury rice, creamy samp & beans, roasted vegetables, and crisp salads.</p>
        </div>
        <div class="menu-card">
            <h4>VIP & State Plated Dining</h4>
            <p>Multi-course plated meals featuring starters, prime cuts or grilled linefish with seasonal sides, and warm Malva pudding.</p>
        </div>
        <div class="menu-card">
            <h4>School & Event Lunch Packs</h4>
            <p>Sealed individual meal boxes with burgers, wors rolls, or quarter-chicken & chips paired with a cold beverage.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 3: PORTFOLIO
# ==========================================
with tab_portfolio:
    st.header("Event Portfolio & Past Projects")
    st.write("Explore our catering track record across schools, state departments, and corporate offices. Use the manual uploader below to add real event photos and summaries.")

    if "portfolio_items" not in st.session_state:
        st.session_state.portfolio_items = [
            {
                "title": "School Function Showcase (Content Pending)",
                "category": "School Event",
                "guests": "Guest Count & School Name • Date Pending",
                "has_image": False,
                "image": None,
                "summary": "Placeholder summary: Full buffet and lunch pack catering for school awards, sports days, or staff workshops. Upload real event photos and menu highlights using the form above."
            },
            {
                "title": "State & Municipal Event Showcase (Content Pending)",
                "category": "State Event",
                "guests": "Delegate Count & Department • Date Pending",
                "has_image": False,
                "image": None,
                "summary": "Placeholder summary: Multi-station hearty buffet and refreshment service for government conferences and community imbizo events. Ready for your official event photos."
            },
            {
                "title": "Corporate Meeting Showcase (Content Pending)",
