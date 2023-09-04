import streamlit as st
import pandas as pd
import plotly.express as px
from pycaret.classification import *
from pycaret.regression import *
import functions

st.set_page_config(layout = "wide", page_title='EDA')
st.header("Exploratory Data Analysis")
functions.space()
st.write('Import Dataset', unsafe_allow_html=True)

file_format = st.radio('Select file format:', ('csv', 'excel'), key='file_format')
dataset = st.file_uploader(label = '')
if dataset:
    if file_format == 'csv' or use_defo:
        df = pd.read_csv(dataset)
    else:
        df = pd.read_excel(dataset)
        
st.subheader('Dataset:')
n, m = df.shape
st.write(f'Dataset contains {n} rows and {m} columns', unsafe_allow_html=True)   
st.dataframe(df)
    
visualizations = ['Info', 'NA', 'Descriptive Analysis', 'Distribution of Numerical Columns',
                   'Box Plots', 'Outlier Analysis']

vizualis = st.sidebar.multiselect("Choose which visualizations you want to see", visualizations)

if 'Info' in vizualis:
        st.subheader('Data Info:')
        c1, c2, c3 = st.columns([1, 2, 1])
        c2.dataframe(functions.df_info(df))
        
if 'NA' in vizualis:
        st.subheader('NA Value Information:')
        if df.isnull().sum().sum() == 0:
            st.write('There is not any NA value in your dataset')
        else:
            c1, c2, c3 = st.columns([0.5, 2, 0.5])
            c2.dataframe(functions.data_isna(df), width=1500)
            functions.space(2)
            
if 'Descriptive Analysis' in vizualis:
        st.subheader('Descriptive Analysis:')
        st.dataframe(df.describe())
        
        
num_columns = df.select_dtypes(exclude = 'object').columns
catego_columns = df.select_dtypes(include = 'object').columns        
if 'Distribution of Numerical Columns' in vizualis:

        if len(num_columns) == 0:
            st.write('There is no numerical columns in the data')
        else:
            selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Distribution plots:', num_columns, 'Distribution')
            st.subheader('Distribution of numerical columns')
            i = 0
            while (i < len(selected_num_cols)):
                c1, c2 = st.columns(2)
                for j in [c1, c2]:
                    if (i >= len(selected_num_cols)):
                        break
                    fig = px.histogram(df, x = selected_num_cols[i])
                    j.plotly_chart(fig, use_container_width = True)
                    i += 1
                    
                    
if 'Box Plots' in vizualis:
        if len(num_columns) == 0:
            st.write('There is no numerical columns in the data.')
        else:
            selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Box plots:', num_columns, 'Box')
            st.subheader('Box plots')
            i = 0
            while (i < len(selected_num_cols)):
                c1, c2 = st.columns(2)
                for j in [c1, c2]:
                    
                    if (i >= len(selected_num_cols)):
                        break
                    
                    fig = px.box(df, y = selected_num_cols[i])
                    j.plotly_chart(fig, use_container_width = True)
                    i += 1
                    
if 'Outlier Analysis' in vizuals:
        st.subheader('Outlier Analysis')
        c1, c2, c3 = st.columns([1, 2, 1])
        c2.dataframe(functions.number_of_outliers(df))
        
        
# Machine learning models
# Sidebar: Select target variable
st.sidebar.header("Select Target Variable")
target_variable = st.sidebar.selectbox("Select the target variable", df.columns)

# Determine problem type (classification or regression)
problem_type = st.sidebar.radio("Select the problem type", ["Classification", "Regression"])

# Sidebar: Select models to train
st.sidebar.header("Select Models to Train")
available_models = get_config("available_models")
selected_models = st.sidebar.multiselect("Select models to train", available_models)

# Train models based on the problem type
if problem_type == "Classification":
    setup_data = setup(data, target=target_variable, silent=True, session_id=42)
    models = compare_models(include=selected_models, sort="AUC")
else:
    setup_data = setup(data, target=target_variable, silent=True, session_id=42)
    models = compare_models(include=selected_models, sort="RMSE")

# Train and evaluate the selected models
st.header("Training and Evaluating Models")
for model_name in selected_models:
    if problem_type == "Classification":
        model = create_model(model_name)
        plot_model(model, plot="confusion_matrix")
    else:
        model = create_model(model_name)
        plot_model(model, plot="residuals")

# Show model evaluation results
st.header("Model Evaluation Results")
evaluate_models()

# Display model performance metrics
if problem_type == "Classification":
    st.write(get_metrics())
else:
    st.write(get_metrics(type="regression"))