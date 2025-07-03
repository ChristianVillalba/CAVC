# displays all the elements from the table admin if connection si successful
def test_connection():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            sqlquery = "SELECT * FROM admins"
            cursor.execute(sqlquery)
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(row)  # Prints each row as a tuple
            else:
                print("No records found in Admin table.")
        except Exception as e:
            print(f"Error during query execution: {e}")
        finally:
            conn.close()
    else:
        print("Failed to establish a connection.")
# call the test function
test_connection()