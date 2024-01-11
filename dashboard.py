import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('forestfires.csv')

# Sidebar
st.sidebar.title("Dashboard Options")
selected_month = st.sidebar.selectbox("Select Month", df['month'].unique())
selected_day = st.sidebar.selectbox("Select Day", df['day'].unique())

# Filter Data
filtered_data = df[(df['month'] == selected_month) & (df['day'] == selected_day)]

# Main content
st.title("Fire Data Dashboard")

st.write(f"Displaying data for {selected_month}, {selected_day}")

# Display DataFrame
st.dataframe(filtered_data)

# Plot
st.subheader("Temperature Distribution")
st.hist(filtered_data['temp'], bins=20, edgecolor='black')
st.pyplot()

# Add more visualizations or analysis based on your needs


