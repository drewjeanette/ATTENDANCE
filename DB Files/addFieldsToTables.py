import sqlite3

DATABASE_NAME = 'dragon.db'
TABLE_NAME = 'CUSTOMER'

# --- 1. Setup: Connect and ensure the table exists (for demonstration) ---
def setup_database():
    """Connects and ensures the 'dragons' table exists with some data."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                color TEXT,
                fire_power INTEGER
            );
        """)

        # Insert some dummy data if the table is empty
        cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME};")
        if cursor.fetchone()[0] == 0:
            cursor.execute(f"INSERT INTO {TABLE_NAME} (name, color, fire_power) VALUES ('Smaug', 'Red', 90);")
            cursor.execute(f"INSERT INTO {TABLE_NAME} (name, color, fire_power) VALUES ('Trogdor', 'Brown', 85);")
            conn.commit()
            print(f"Setup complete: Created '{TABLE_NAME}' table and added initial data.")

    except sqlite3.Error as e:
        print(f"Database setup error: {e}")
    finally:
        if conn:
            conn.close()

# --- 2. Function to Read Data ---
def read_dragons():
    """Reads and prints all records from the table."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Select all records
        cursor.execute(f"SELECT id, name, color, fire_power FROM {TABLE_NAME};")
        
        # Fetch column names
        column_names = [description[0] for description in cursor.description]
        print(f"\n--- Current {TABLE_NAME.capitalize()} Data ---")
        print(f"Columns: {', '.join(column_names)}")
        
        # Fetch and print all rows
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Color: {row[2]}, Fire Power: {row[3]}")
        
        return rows
    
    except sqlite3.Error as e:
        print(f"Database read error: {e}")
        return []
    finally:
        if conn:
            conn.close()

# --- 3. Function to Edit/Update a Field ---
def edit_dragon_field(dragon_id, field_name, new_value):
    """Updates a specific field for a given dragon ID."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Ensure the field name is a column name (simple validation)
        # Note: For production, use a whitelist or check against schema
        if field_name not in ['name', 'color', 'fire_power']:
             print(f"Error: Field '{field_name}' is not editable or doesn't exist.")
             return

        # Prepare the SQL UPDATE statement. We use '?' placeholders for safety.
        # This prevents SQL Injection attacks.
        sql_update = f"UPDATE {TABLE_NAME} SET {field_name} = ? WHERE id = ?;"
        
        cursor.execute(sql_update, (new_value, dragon_id))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"\n✅ Success: Updated Dragon ID {dragon_id}'s {field_name} to '{new_value}'.")
        else:
            print(f"\n⚠️ Warning: No dragon found with ID {dragon_id} or no change was made.")

    except sqlite3.Error as e:
        print(f"Database edit error: {e}")
    finally:
        if conn:
            conn.close()

# --- Main Execution ---

# 1. Setup the database (creates table/data if needed)
setup_database()

# 2. Read the current data
read_dragons()

# 3. Prompt user for input and edit (Example interactive part)
try:
    print("\n--- Interactive Edit ---")
    
    # Get the ID of the dragon to edit
    id_to_edit = int(input("Enter the ID of the dragon you want to edit (e.g., 1): "))
    
    # Get the field name to change
    field_to_change = input("Enter the field name to change (name, color, fire_power): ").lower()
    
    # Get the new value
    new_data = input(f"Enter the new value for {field_to_change}: ")
    
    # Attempt to convert fire_power to integer if that's the field
    if field_to_change == 'fire_power':
        new_data = int(new_data)
        
    # Execute the edit
    edit_dragon_field(id_to_edit, field_to_change, new_data)

except ValueError:
    print("\nInvalid input. Please ensure ID and fire_power (if editing) are numbers.")
except Exception as e:
    print(f"\nAn unexpected error occurred during input: {e}")

# 4. Read the data again to verify the edit
read_dragons()