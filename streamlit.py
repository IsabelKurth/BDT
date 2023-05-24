import pandas as pd
import streamlit as st

# Read the CSV file
df = pd.read_csv('clothing.csv')
print(df.head())

# Set up Streamlit
st.title("Customer Review Analysis")
st.subheader("CSV Data")
st.dataframe(df)

# Additional visualizations or analysis can be added here using Streamlit's features
st.subheader('Ratings by age')
st.bar_chart(df['Age'])