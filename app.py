import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Construction Estimator")
st.title("🏗️ Upload Blueprint for AI-Based Estimate")

# Upload
blueprint = st.file_uploader("Upload Blueprint (Image or PDF)", type=["jpg", "jpeg", "png", "pdf"])

# Client Input Form
st.subheader("📝 Project Details")
project_name = st.text_input("Project Name")
zip_code = st.text_input("ZIP Code")
project_type = st.selectbox("Project Type", ["Kitchen Remodel", "Bathroom Addition", "Basement Finish", "Other"])
sq_ft = st.number_input("Square Footage", step=50)
floor_type = st.multiselect("Floor Type", ["Tile", "Wood", "Laminate", "Carpet"])
fixtures = st.text_input("Fixtures Needed (comma-separated)")
timeline = st.selectbox("Timeline", ["2 Weeks", "4 Weeks", "8 Weeks"])
buffer = st.slider("Material Buffer %", min_value=0, max_value=30, value=20)

# Generate Estimate
if st.button("✅ Generate Estimate"):
    base_price_per_sqft = 35  # Example fixed rate
    base_estimate = sq_ft * base_price_per_sqft
    buffer_amount = base_estimate * buffer / 100
    total_estimate = base_estimate + buffer_amount

    st.success("✅ Estimate Complete")
    st.write("### 💰 Estimated Cost Breakdown")
    st.write(f"**Base Estimate (materials + labor):** ${base_estimate:,.2f}")
    st.write(f"**Buffer ({buffer}%):** ${buffer_amount:,.2f}")
    st.markdown("---")
    st.write(f"### 🧾 **Total Estimate: ${total_estimate:,.2f}**")
