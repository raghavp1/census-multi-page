import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(census_df):
    st.set_option("deprecation.showPyplotGlobalUse", False)
    st.subheader("Visualization Selector")
    plot_list = st.multiselect("Select the Charts/Plots:", ("income-group", "gender", "hours-per-week by income group", "hours-per-week by gender", "workclass"))

    if 'income-group' in plot_list:
        st.subheader("distribution of records for the income-group feature.")
        plt.figure(figsize=(10,10))
        plt.pie(census_df["income"].value_counts(), labels=census_df["income"].value_counts().index, autopct="%1.2f%%")
        st.pyplot()
    if 'gender' in plot_list:
        st.subheader("distribution of records for the gender feature.")
        plt.figure(figsize=(10,10))
        plt.pie(census_df["gender"].value_counts(), labels=census_df["gender"].value_counts().index, autopct="%1.2f%%")
        st.pyplot()
    if 'hours-per-week by income group' in plot_list:
        st.subheader("Box plot for the hours-per-week feature for different income groups.")
        plt.figure(figsize=(10,10))
        sns.boxplot(census_df["hours-per-week"], census_df["income"])
        st.pyplot()
    if 'hours-per-week by gender' in plot_list:
        st.subheader("Box plot for the hours-per-week feature for different genders.")
        plt.figure(figsize=(10,10))
        sns.boxplot(census_df["hours-per-week"], census_df["gender"])
        st.pyplot()
    if "workclass" in plot_list:
        st.subheader("Count Plot for unique workclass feature values for different income groups.")
        plt.figure(figsize=(10,10))
        sns.countplot(x = "workclass", data=census_df)
        st.pyplot()