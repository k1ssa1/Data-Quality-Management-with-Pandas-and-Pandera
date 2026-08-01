import pandas as pd

#read the file and return a dataframe
def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df