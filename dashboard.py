
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Network Traffic Analyzer",
    layout="wide"
)

st.title("🛡️ Network Traffic Analyzer")
st.write("Cybersecurity Monitoring Dashboard")

df = pd.read_csv("traffic.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Total Packets", len(df))
col2.metric("Unique Source IPs", df["Source IP"].nunique())
col3.metric("Unique Destination IPs", df["Destination IP"].nunique())

st.subheader("Protocol Distribution")
st.bar_chart(df["Protocol"].value_counts())

st.subheader("Top Source IP Addresses")
st.bar_chart(df["Source IP"].value_counts().head(10))

st.subheader("Packet Size Statistics")
st.write(df["Packet Size"].describe())

st.subheader("Captured Network Traffic")
st.dataframe(df, use_container_width=True)
