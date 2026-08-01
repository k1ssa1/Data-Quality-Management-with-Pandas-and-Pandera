# Data Quality Management with Pandas and Pandera

This exercise showcases how to leverage Python libraries (Pandas and Pandera) for DQM procedures: Data validation and data cleansing.

Discover the full article: 
https://dev.to/kitchen_code/data-quality-management-data-validation-and-data-cleansing-with-pandas-and-pandera-3elp

## Features

- Data cleansing with Pandas
- Data validation with Pandera
- Separation of clean and dirty records
- Type, format, code, consistency, uniqueness and range checks

## Project Structure

```text
.
├── data/
│   └── dirty_cafe_sales.csv
├── workflow/
│   ├── extract.py
│   └── transform.py
├── main.py
└── requirements.txt
```

## Dataset

This project uses the **Cafe Sales - Dirty Data for Cleaning Training** dataset by Ahmed Mohamed.

License: **CC BY-SA 4.0**

Download:
https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the project

Place the downloaded dataset inside the `data/` directory.

Run

python main.py

## Technologies

- Python
- Pandas
- Pandera

## License

The repository and dataset are both licensed under CC BY-SA 4.0. 
https://creativecommons.org/licenses/by-sa/4.0/

**Changes made:** This project renames columns, removes duplicate rows, separates clean and dirty records, converts data types, performs data validation using Pandas and Pandera, and conducts sorts.