import pandas as pd

from sqlalchemy import create_engine

data = pd.read_csv('CSV/clean_csv/students_performance_clean.csv')

engine = create_engine("mysql+pymysql://root:@localhost:3307/students_db")
data.to_sql(
    name="student_performance",  # table name in MySQL
    con=engine,                  # connection to use
    if_exists="replace",         # if table exists, replace it
    index=False                  # don't write dataframe index as a column
)

print("Data loaded successfully!")