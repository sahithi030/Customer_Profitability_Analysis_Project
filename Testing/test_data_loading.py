import pandas as pd
from sqlalchemy import create_engine

def test_data_loading():
    engine = create_engine("mysql+mysqlconnector://root:Nithin@2003@localhost/customer_profitability_db")
    df = pd.read_sql("SELECT * FROM customer_profitability", engine)
    assert not df.empty, " DataFrame is empty after loading."
    required_columns = ['Customer_ID', 'Customer_Name', 'Age', 'Gender', 'City', 'Plan_Type', 'Revenue', 'Cost', 'Profit']
    for col in required_columns:
        assert col in df.columns, f" Missing column: {col}"
    print(" test_data_loading passed")

if __name__ == "__main__":
    test_data_loading()
