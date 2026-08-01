import pandas as pd
import pandera.pandas as pa
from pandera import DateTime

def transform_data(df):
    df = pd.DataFrame(df)

    # data cleaning: rename columns
    df.rename(columns={'Transaction ID': 'transaction_id', 'Item': 'item', 'Quantity': 'quantity', 'Price Per Unit': 'price_per_unit', 'Total Spent': 'total_spent', 'Payment Method': 'payment_method', 'Location': 'location', 'Transaction Date': 'transaction_date'}, inplace=True)

    # data cleaning: remove duplicates
    df = df.drop_duplicates()

    # data cleaning: extract dirty data from cells for each row
    def data_extraction():
        dirty_values = ["UNKNOWN", "ERROR"]
        dirty_rows = []
        rows_to_drop = []

        for index, row in df.iterrows():
            for value in row:
                if value in dirty_values or pd.isna(value):
                    dirty_rows.append(row)
                    rows_to_drop.append(index)
                    break

        dirty_dataframe = pd.DataFrame(dirty_rows)
        clean_dataframe = df.drop(index=rows_to_drop)

        clean_dataframe = clean_dataframe.reset_index(drop=True)

        return clean_dataframe, dirty_dataframe

    cd, dd = data_extraction()

    # data cleaning: data type conversion
    cd["quantity"] = cd["quantity"].astype(int)
    cd["price_per_unit"] = cd["price_per_unit"].astype(float)
    cd["total_spent"] = cd["total_spent"].astype(float)
    cd["transaction_date"] = pd.to_datetime(cd["transaction_date"], errors="coerce")

    # data validation: type check
    data_type_check = pa.DataFrameSchema(
        {
            "transaction_id": pa.Column(str),
            "item": pa.Column(str),
            "quantity": pa.Column(int),
            "price_per_unit": pa.Column(float),
            "total_spent": pa.Column(float),
            "payment_method": pa.Column(str),
            "location": pa.Column(str),
            "transaction_date": pa.Column(DateTime)
        }
    )

    data_type_check.validate(cd)

    # data validation: uniqueness check
    uniqueness_check = pa.DataFrameSchema(
        {
        "transaction_id": pa.Column(unique=True),
        }
    )

    uniqueness_check.validate(cd)

    # data format check
    format_check = pa.DataFrameSchema(
        {
            "transaction_id": pa.Column(
                str,
                checks=pa.Check(lambda s: s.str.startswith("TXN_"))
            )
        }
    )

    format_check.validate(cd)

    # data validation: code check on transaction method
    transaction_methods = [
        "Credit Card",
        "Digital Wallet",
        "Cash",
        "Other",
        "Cheque",
        "Bank Transfers"
    ]
    code_check = pa.DataFrameSchema(
        {
            "payment_method": pa.Column(
                str,
                checks=pa.Check.isin(transaction_methods)
            )
        }
    )

    code_check.validate(cd)

    # data validation: consistency check
    consistency_check = pa.DataFrameSchema(
        checks=[
            pa.Check(lambda df: (
                    df["total_spent"] == df["quantity"] * df["price_per_unit"]
                )
            )
        ]
    )

    consistency_check.validate(cd)

    # data validation: range check
    range_check = pa.DataFrameSchema(
        {
            "transaction_date": pa.Column(
                DateTime,
                checks=pa.Check(
                    lambda s: (
                        (s >= pd.Timestamp("2023-01-01")) &
                        (s < pd.Timestamp("2024-01-01"))
                    )
                )
            ),
            "quantity": pa.Column(
                int,
                checks=pa.Check.ge(0)
            ),
            "price_per_unit": pa.Column(
                float,
                checks=pa.Check.ge(0)
            ),
            "total_spent": pa.Column(
                float,
                checks=pa.Check.ge(0)
            )
        }
    )
    range_check.validate(cd)

    # sort the clean DataFrame by transaction_date in descending order
    cd_sorted = cd.sort_values(by='transaction_date', ascending=False)

    # return both the clean sorted DataFrame and the dirty DataFrame
    # you can load this data into the destination of choice
    return cd_sorted, dd