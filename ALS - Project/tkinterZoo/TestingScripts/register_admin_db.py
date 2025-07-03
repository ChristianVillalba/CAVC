# try to register a new admin into the database, 
# will dispalys successful or error messages to guide the users
def register_admin_db(first_name, last_name, username, password, email):
    print(f'Attempting to register user: {username}')
    conn = get_db_connection()
    if not conn: 
        return False 
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM Admins WHERE username = ?", (username,))
        if cursor.fetchone():
            print(f"User {username} already exists")
            return False
        cursor.execute("INSERT INTO Admins(first_name, last_name, username, password, email) VALUES(?,?,?,?,?)",(first_name, last_name, username, password, email))
        conn.commit()
        print(f"user {username} registered successfully")
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()
register_admin_db()