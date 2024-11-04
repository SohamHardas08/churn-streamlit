import requests 
import pandas as pd
import streamlit as st


import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics Dashboard", layout="centered")

api_url = "http://127.0.0.1:8000/records/" 

try:
    response = requests.get(api_url)
    response.raise_for_status()  
    data = response.json()
    
    df = pd.DataFrame(data)
    df = df.drop('notes', axis=1)
    st.dataframe(df) 
    
    st.title("Analytics Dashboard")

    st.sidebar.header("Filter Options")

    
    selected_feature = st.sidebar.selectbox(
        "Select Feature", 
        options=['contract', 'internet_service', 'payment_method']
    )

    
    min_tenure = int(df["tenure"].min())
    max_tenure = int(df["tenure"].max())
    tenure_range = st.sidebar.slider(
        "Select Tenure Range",
        min_value=min_tenure,
        max_value=max_tenure,
        value=(min_tenure, max_tenure),
        step=1
    )

    
    filtered_df = df[(df["tenure"] >= tenure_range[0]) & (df["tenure"] <= tenure_range[1])]

    fig = px.histogram(
        filtered_df,
        x=selected_feature,
        color="Churn",
        barmode="group",
        title=f"{selected_feature} vs Churn"
    )
    st.plotly_chart(fig)

    st.markdown("""
    These visualizations are based on the Telco customer dataset,  the same dataset on which the 
    predictive model was trained on.
    """)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")
