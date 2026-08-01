from workflow.extract import extract_data
from workflow.transform import transform_data

def main():
    df = extract_data("data/dirty_cafe_sales.csv")
    transform_data(df)
main()