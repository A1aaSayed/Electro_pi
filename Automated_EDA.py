import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Load data
def load_data():
    file_path = input("Enter the path to the data file: ")
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
    return df

# Clean data
def handle_missing(df):
    na_cols = [col for col in df.columns if df[col].isna().any()]
    
    for col in na_cols:
        if df[col].dtype in ['int64', 'float64']:
            mean_value = df[col].mean()
            df[col].fillna(mean_value, inplace=True)
        else:
            mode_value = df[col].mode()
            df[col].fillna(mode_value, inplace=True)
    return df

# Display data info
def data_info(df):
    # Display the shape of the dataset
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
        
    # Display summary for numerical columns
    print("\nData Summary:\n")
    print(df.describe())

# Scale numerical data
def data_scale(df):
    df[df.select_dtypes(include=['number']).columns] = scaler.fit_transform(df[df.select_dtypes(include=['number']).columns])

# Data visualization
def data_visualization(df):
    # set the color palette
    sns.set_palette('pastel')

    # determine the type of each column
    for column in df.columns:
        col_name = df[column]
        col_type = col_name.dtype

        fig, axs = plt.subplots()

        # visualize categorical data with bar chart
        if col_type == 'object':
            value_counts = col_name.value_counts()
            labels = value_counts.index
            sns.barplot(x=labels, y=value_counts, ax=axs)

        # visualize numerical data with histogram
        elif col_type in ['int64', 'float64']:
            sns.histplot(col_name, bins='auto', ax=axs)
            axs.axvline(col_name.mean(), color='red', linewidth=1)
            axs.axvline(col_name.median(), color='green', linewidth=1)
            axs.legend(['Mean', 'Median'])

        axs.set_title(column)
        axs.grid(True)
        plt.show()

def main():
    # Load data
    df = load_data()
    
     # Handle missing values
    df = handle_missing(df)
    
    # Display data information
    data_info(df)
    
    # Scale the data
    data_scale(df)
    
    # Visualize the data
    data_visualization(df)


if __name__ == "__main__":
    main()