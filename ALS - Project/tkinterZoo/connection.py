import pyodbc
 
# Database credentials
SERVER = 'laptop-n0755o44\\sqlexpress01'  # Or 'localhost\\SQLEXPRESS' if using a named instance
DATABASE = 'zooDB'
USERNAME = 'LAPTOP-N0755O44\\CRISTIAN'
DRIVER = 'ODBC Driver 18 for SQL Server'
 
def get_db_connection():
    """Establish a connection to SQL Server using ODBC."""
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'UID={USERNAME};'
            f'Encrypt=yes;'
            f'TrustServerCertificate=yes;'
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
 
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
                print("No records found in Tasks table.")
        except Exception as e:
            print(f"Error during query execution: {e}")
        finally:
            conn.close()
    else:
        print("Failed to establish a connection.")

test_connection()