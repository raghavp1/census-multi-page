
import streamlit as st
import numpy as np
import pandas as pd

def app(census_df):
    st.title("Census Visualisation Web App")
    st.subheader("This web app allows the user to explore and visualise the census data")

    with st.expander("View Data"):
        st.dataframe(census_df)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.checkbox("Display column names"):
            st.write(census_df.columns)
    with c2:
        if st.checkbox("Display column data types"):
            st.write(list(census_df.dtypes))
    with c3:
        if st.checkbox("Display data for column:"):
            choice = st.selectbox("Choose column:", tuple(census_df.columns))
            st.write(census_df[choice])


    if st.checkbox("Display summary"):
        st.write(census_df.describe())
