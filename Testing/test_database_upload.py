import mysql.connector

def test_database_upload():
    conn = mysql.connector.connect(
        user="root",
        password="Nithin@2003",
        host="localhost",
        database="customer_profitability_db"
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES LIKE 'customer_profitability_cleaned'")
    result = cursor.fetchone()
    assert result is not None, " Cleaned table not found in database."
    cursor.execute("SELECT COUNT(*) FROM customer_profitability_cleaned")
    count = cursor.fetchone()[0]
    assert count > 0, " Cleaned table is empty."
    print(" test_database_upload passed")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    test_database_upload()
