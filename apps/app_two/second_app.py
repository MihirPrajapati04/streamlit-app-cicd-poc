import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="My Snowflake App",
    page_icon="❄️",
    layout="wide"
)

# Title
st.title("❄️ My Snowflake Streamlit App")
st.write("Welcome to my first Streamlit in Snowflake app!")

# Simple metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Sales", value="$10,000", delta="5%")

with col2:
    st.metric(label="Total Users", value="1,200", delta="12%")

with col3:
    st.metric(label="Active Sessions", value="340", delta="-2%")

# Simple dataframe
st.subheader("Sample Data")

data = {
    "Name":     ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age":      [25, 30, 35, 28, 22],
    "City":     ["New York", "London", "Paris", "Tokyo", "Sydney"],
    "Sales":    [5000, 7000, 4500, 8000, 6000]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# Simple chart
st.subheader("Sales Chart")
st.bar_chart(df.set_index("Name")["Sales"])

# Simple input
st.subheader("Search")
search = st.text_input("Search by name")

if search:
    result = df[df["Name"].str.contains(search, case=False)]
    if not result.empty:
        st.success(f"Found {len(result)} result(s)")
        st.dataframe(result, use_container_width=True)
    else:
        st.warning("No results found")