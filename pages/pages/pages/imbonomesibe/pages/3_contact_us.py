import streamlit as st

st.set_page_config(page_title="Contact Us | Imbo Nomxesibe Hearty Meals", page_icon="📞", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #fefdf7; color: #1f241d; }
    .contact-hero {
        background: linear-gradient(135deg, #1f2b1c 0%, #365314 60%, #ca8a04 100%);
        color: #ffffff;
        padding: 2.75rem 2rem;
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
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-hero">
    <p style="color: #fef08a; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; font-size: 0.85rem; margin-bottom: 0.3rem;">Let's Plan Your Next Event</p>
    <h1 style="color: #ffffff; margin: 0;">Partner With Imbo Nomxesibe Hearty Meals</h1>
    <p style="color: #fefce8; max-width: 720px; margin-top: 0.6rem;">From first consultation to the final plate served, our team delivers seamless, stress-free catering for schools, government departments, and corporate gatherings.</p>
</div>
""", unsafe_allow_html=True)

# 3-Step Process Strip
st.subheader("How Our Catering Process Works")
s1, s2, s3 = st.columns(3, gap="medium")
with s1:
    st.markdown("""
    <div class="step-box">
        <strong style="color: #3f6212;">1. Share Your Event Brief</strong>
        <p style="font-size: 0.9rem; margin-top: 0.4rem;">Tell us your event date, venue, guest count, and preferred meal style.</p>
    </div>
    """, unsafe_allow_html=True)
with s2:
    st.markdown("""
    <div class="step-box">
        <strong style="color: #3f6212;">2. Receive a Tailored Proposal</strong>
        <p style="font-size: 0.9rem; margin-top: 0.4rem;">We send a customized menu and formal quotation suited to your budget.</p>
    </div>
    """, unsafe_allow_html=True)
with s3:
    st.markdown("""
    <div class="step-box">
        <strong style="color: #3f6212;">3. Punctual Setup & Service</strong>
        <p style="font-size: 0.9rem; margin-top: 0.4rem;">We arrive on schedule with fresh, hearty meals and full serving support.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
left, right = st.columns([1, 1.35], gap="large")

with left:
    st.markdown("""
    <div class="profile-card">
        <h3 style="color: #a16207; margin-top: 0;">Headquarters & Direct Desk</h3>
        <p style="color: #57534e; font-size: 0.95rem;">Available for school tenders, state RFQs, corporate accounts, and private bookings.</p>
        <hr style="border: 0; border-top: 1px solid #fef08a; margin: 1rem 0;" />
        <p><strong>📞 Phone & WhatsApp:</strong><br/>073 379 1648</p>
        <p><strong>✉️ Official Email:</strong><br/>thenjinjoli@gmail.com</p>
        <p><strong>📍 Kitchen & Office Address:</strong><br/>22661 Nosethu Street, Mfuleni, Cape Town, 7100</p>
        <p><strong>🕒 Operating Hours:</strong><br/>Monday – Saturday: 07:00 – 19:00<br/><em>(Sunday functions catered by prior booking)</em></p>
        <a href="https://wa.me" target="_blank" class="whatsapp-cta">💬 Instant WhatsApp Quote (073 379 1648)</a>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.subheader("Send an Event & Quote Inquiry")
    with st.form("executive_quote_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Contact Person Full Name *")
            email = st.text_input("Email Address *")
            event_type = st.selectbox("Event Category *", ["School Event", "State / Municipal Event", "Corporate Meeting", "Other Function"])
        with c2:
            org = st.text_input("School / Department / Company Name")
            phone = st.text_input("Phone or WhatsApp Number *")
            guests = st.number_input("Estimated Guest Count *", min_value=10, value=60, step=10)

        d1, d2 = st.columns(2)
        with d1:
            event_date = st.date_input("Event Date *")
        with d2:
            venue = st.text_input("Event Venue / Suburb", placeholder="e.g. Mfuleni, Blue Downs, Cape Town CBD")

        notes = st.text_area("Menu Preferences & Special Requirements", placeholder="Describe preferred dishes, serving style (buffet, platters, lunch packs), or dietary needs...")

        if st.form_submit_button("Request Formal Quote"):
            if name and email and phone:
                st.success(
                    f"Thank you, **{name}**! Your inquiry for **{org or event_type}** ({guests} guests on {event_date}) has been logged. "
                    "Imbo Nomxesibe Hearty Meals will respond via email or WhatsApp shortly."
                )
            else:
                st.error("Please fill in your Full Name, Email Address, and Phone Number.")
