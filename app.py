import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv(r'churn.csv')

# Set page configuration
st.set_page_config(page_title="Analytics Dashboard", layout="centered")

# Title
st.title("Analytics Dashboard")

# Sidebar for feature selection and tenure range selection
st.sidebar.header("Filter Options")

# Dropdown for selecting a feature
selected_feature = st.sidebar.selectbox(
    "Select Feature", 
    options=['Contract', 'InternetService', 'PaymentMethod']
)

# Slider for selecting the tenure range
min_tenure = int(df["tenure"].min())
max_tenure = int(df["tenure"].max())
tenure_range = st.sidebar.slider(
    "Select Tenure Range",
    min_value=min_tenure,
    max_value=max_tenure,
    value=(min_tenure, max_tenure),
    step=1
)

# Filter the data based on tenure range
filtered_df = df[(df["tenure"] >= tenure_range[0]) & (df["tenure"] <= tenure_range[1])]

# Create and display the chart
fig = px.histogram(
    filtered_df,
    x=selected_feature,
    color="Churn",
    barmode="group",
    title=f"{selected_feature} vs Churn"
)
st.plotly_chart(fig)
