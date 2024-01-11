# Import necessary libraries
import streamlit as st
import pandas as pd

# Load the forest fires data
df = pd.read_csv("forestfires.csv")

# Drop unnecessary columns
df.drop(["FFMC", "DMC", "DC", "ISI", "RH"], axis=1, inplace=True)

# Set the page title
st.title("Forest Fires Data Dashboard")

# Display the first few rows of the dataset
st.subheader("Dataset Overview")
st.dataframe(df.head())

# Display basic statistics of the dataset
st.subheader("Dataset Statistics")
st.write(df.describe())

# Display the shape of the dataset
st.subheader("Dataset Shape")
st.write(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")

# Display missing values information
st.subheader("Missing Values")
st.write(df.isna().sum())

# Display data types
st.subheader("Data Types")
st.write(df.dtypes)


# Add a sidebar for user interaction
st.sidebar.header("User Input")
selected_month = st.sidebar.selectbox("Select a month:", df['month'].unique())
selected_day = st.sidebar.selectbox("Select a day:", df['day'].unique())

# Filter the data based on user input
filtered_data = df[(df['month'] == selected_month) & (df['day'] == selected_day)]

# Display the filtered data
st.sidebar.subheader("Filtered Data")
st.sidebar.write(filtered_data)

# Run the app
st.sidebar.text("App by Your Name")