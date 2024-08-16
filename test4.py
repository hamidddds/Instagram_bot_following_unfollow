import os
import pandas as pd


def read_inputs():
    file_path = os.path.join('data', 'inputs.xlsx')

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    # Read the Excel file
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        raise RuntimeError(
            f"An error occurred while reading the Excel file: {e}")

    # Check if required columns exist
    required_columns = ['Target Name', 'Type Name', 'Number Of follow']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(
                f"The column '{col}' is missing from the Excel file.")

    # Read values
    TargetName = df.loc[0, 'Target Name']
    TargetType = df.loc[0, 'Type Name']
    Number_of_following = df.loc[0, 'Number Of follow']

    return TargetName, TargetType, Number_of_following


print(read_inputs())
