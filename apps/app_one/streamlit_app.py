import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Title & intro
st.title("🚀 My Dummy Streamlit App")
st.markdown("Welcome! This is a **dummy Streamlit app** showcasing common components.")

st.divider()

# --- Sidebar ---
st.sidebar.header("⚙️ Controls")
name = st.sidebar.text_input("Your Name", value="World")
age = st.sidebar.slider("Your Age", min_value=1, max_value=100, value=25)
theme = st.sidebar.selectbox("Favorite Color", ["Red", "Blue", "Green", "Purple"])
st.sidebar.success(f"Hello, {name}! 👋")

# --- Main Area ---
col1, col2, col3 = st.columns(3)
col1.metric("Users", "1,234", "+12%")
col2.metric("Revenue", "$5,678", "-3%")
col3.metric("Uptime", "99.9%", "+0.1%")

st.divider()

# --- Chart ---
st.subheader("📈 Random Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Series A", "Series B", "Series C"]
)
st.line_chart(chart_data)

# --- Table ---
st.subheader("📋 Sample Data Table")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [28, 34, 22, 45],
    "City": ["Mumbai", "Delhi", "Bangalore", "Chennai"],
    "Score": [88, 92, 76, 95]
})
st.dataframe(df, use_container_width=True)

# --- User Input ---
st.divider()
st.subheader("💬 User Input")
user_text = st.text_area("Write something:", placeholder="Type anything here...")
if st.button("Submit"):
    if user_text:
        st.success(f"You said: *{user_text}*")
    else:
        st.warning("Please write something first!")

# --- Progress / Status ---
st.divider()
st.subheader("⏳ Progress Bar")
progress = st.slider("Progress", 0, 100, 60)
st.progress(progress)

# --- Expandable Section ---
with st.expander("🔍 Show More Details"):
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Favorite Color:** {theme}")
    st.info("This section is expandable!")

st.divider()
st.caption("Built with ❤️ using Streamlit")