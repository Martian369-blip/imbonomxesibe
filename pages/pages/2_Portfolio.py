yimport streamlit as st

st.set_page_config(page_title="Portfolio | Imbo Nomxesibe Hearty Meals", page_icon="📸", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #fefdf7; color: #1f241d; }
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
</style>
""", unsafe_allow_html=True)

st.title("Event Portfolio & Past Projects")
st.write("Explore our catering track record across schools, state departments, and corporate offices. Use the manual uploader below to add real event photos and summaries as they become available.")

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
            "category": "Corporate Meeting",
            "guests": "Executive Group & Venue • Date Pending",
            "has_image": False,
            "image": None,
            "summary": "Placeholder summary: Morning breakfast platters and warm boardroom lunches delivered on schedule. Add your corporate client summary and photos here."
        }
    ]

with st.expander("➕ Add Real Portfolio Event & Photo Manually", expanded=False):
    with st.form("add_event_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Event Title *", placeholder="e.g. Mfuleni High School Prize-Giving")
            category = st.selectbox("Category *", ["School Event", "State Event", "Corporate Meeting"])
            guests = st.text_input("Guests & Venue/Date *", placeholder="e.g. 200 Guests • November 2026")
        with col2:
            photo = st.file_uploader("Upload Event Photo (JPG/PNG)", type=["jpg", "jpeg", "png"])
            summary = st.text_area("Event Summary & Menu Served *", placeholder="Write a short summary of the food served and event setup...")

        if st.form_submit_button("Publish to Portfolio"):
            if title and guests and summary:
                st.session_state.portfolio_items.insert(0, {
                    "title": title,
                    "category": category,
                    "guests": guests,
                    "has_image": photo is not None,
                    "image": photo,
                    "summary": summary
                })
                st.success(f"Added '{title}' to your portfolio!")
            else:
                st.error("Please fill in Event Title, Guests/Venue, and Summary.")

st.divider()

filter_cat = st.selectbox("Filter by Category", ["All Categories", "School Event", "State Event", "Corporate Meeting"])
visible_items = [
    i for i in st.session_state.portfolio_items
    if filter_cat == "All Categories" or i["category"] == filter_cat
]

cols = st.columns(3, gap="medium")
for idx, item in enumerate(visible_items):
    with cols[idx % 3]:
        if item["has_image"] and item["image"] is not None:
            st.image(item["image"], use_container_width=True)
        else:
            st.markdown("""
            <div class="placeholder-banner">
                <strong>📷 Event Photo Pending</strong><br/>
                <span style="font-size: 0.85rem;">Upload a photo via the Manual Entry panel above</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f'<span class="badge">{item["category"]}</span>', unsafe_allow_html=True)
        st.subheader(item["title"])
        st.caption(item["guests"])
        st.write(item["summary"])
        if st.button("Remove Card", key=f"rm_{idx}_{item['title']}"):
            st.session_state.portfolio_items.remove(item)
            st.rerun()
