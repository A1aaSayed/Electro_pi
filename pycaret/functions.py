import pandas as pd
import streamlit as st

def data_isna(df):
    res = pd.DataFrame(df.isnull().sum()).reset_index()
    res['Persentage'] = round(res[0] / df.shape[0] * 100, 2)
    res['Percentage'] = res['Percentage'].astype(str) + '%'
    return res.rename(columns = {'index':'Column', 0:'Number of null values'})

def data_info(df):
    # Display the shape of the dataset
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
        
    # Display summary for numerical columns
    print("\nData Summary:\n")
    print(df.describe())

def count_outliers(df):
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=['number'])
    
    # Calculate Q1 and Q3 for each column
    Q1 = numerical_cols.quantile(0.25)
    Q3 = numerical_cols.quantile(0.75)
    
    # Calculate IQR for each column
    IQR = Q3 - Q1
    
    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Find outliers using the bounds
    outliers = (numerical_cols < lower_bound) | (numerical_cols > upper_bound)
    
    # Count outliers for each column
    outlier_counts = outliers.sum()
    
    return outlier_counts

def space(num_lines=1):
    for _ in range(num_lines):
        st.write("")

def sidebar_space(num_lines=1):
    for _ in range(num_lines):
        st.sidebar.write("")

def sidebar_space(num_lines=1):
    for _ in range(num_lines):
        st.sidebar.write("")