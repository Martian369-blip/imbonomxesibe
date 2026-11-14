import streamlit as st

st.set_page_config(page_title="About Us | Imbo Nomxesibe Hearty Meals", page_icon="🍲", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #fefdf7; color: #1f241d; }
    .banner {
        background: linear-gradient(90deg, #ca8a04, #65a30d);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .menu-card {
        background-color: #ffffff;
        border-left: 5px solid #65a30d;
        padding: 1.25rem;
        border-radius: 6px;
        border: 1px solid #fef08a;
        margin-bottom: 1rem;
    }
    .menu-card h4 { color: #854d0e !important; margin-bottom: 0.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
    <h1 style="color: white; margin: 0;">About Imbo Nomxesibe Hearty Meals</h1>
    <p style="color: #fefce8; margin-top: 0.5rem;">Rooted in hospitality, generous portions, and dependable event execution across Cape Town.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1], gap="large")
with col1:
    st.subheader("Our Story & Mission")
    st.write(
        "Founded in **Mfuleni, Cape Town**, **Imbo Nomxesibe Hearty Meals** was built on a simple commitment: "
        "to serve generous, home-style South African and continental meals with the reliability that institutions and businesses depend on."
    )
    st.write(
        "Whether catering for 30 executives in a boardroom or 500+ attendees at a school or state function, "
        "we handle menu preparation, punctual transport, buffet presentation, and serving logistics with pride."
    )
    st.markdown("""
    ### Our Core Standards
    - **High-Volume Cooking Capacity:** Prepared to scale smoothly for large institutional and municipal events.
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
