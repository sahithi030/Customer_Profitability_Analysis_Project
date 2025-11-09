import pandas as pd

def test_data_cleaning():
    df = pd.read_csv("data/customer_profitability.csv")
    df.drop_duplicates(inplace=True)
    df.fillna({'Gender': 'Unknown'}, inplace=True)
    df = df[(df['Age'] > 0) & (df['Age'] < 100)]
    df = df[df['Profit'] >= 0]
    assert df['Gender'].isnull().sum() == 0, " Missing Gender values remain."
    assert df['Customer_ID'].duplicated().sum() == 0, "Duplicate Customer_IDs found."
    assert df['Age'].between(1, 99).all(), "Invalid ages found."
    print(" test_data_cleaning passed")

if __name__ == "__main__":
    test_data_cleaning()
