import sqlite3

def create_table_with_dynamic_columns(db_name="dragon.db"):
    """
    Connects to the specified SQLite database, prompts the user for 
    a table name, and then prompts for column names and types 
    to create a fully dynamic table.
    """
    
    # 1. Get the desired table name from the user
    table_name = input("🐉 Enter the desired name for your new table (e.g., 'Treasures', 'Hunters'): ").strip()
    
    if not table_name:
        print("Table name cannot be empty. Exiting.")
        return

    # 2. Collect column definitions
    columns = []
    print("\n--- Column Definition ---")
    print("Available SQLite Data Types: INTEGER, TEXT, REAL, BLOB, NULL")
    
    # Always include a Primary Key (optional, but good practice)
    columns.append("id INTEGER PRIMARY KEY")
    print("✅ Added 'id INTEGER PRIMARY KEY' as the first column.")

    while True:
        col_name = input("Enter column name (or type 'done' to finish): ").strip()
        
        if col_name.lower() == 'done':
            if len(columns) > 1:
                break
            else:
                print("You must define at least one column besides 'id'.")
                continue

        col_type = input(f"Enter data type for '{col_name}' (e.g., TEXT, INTEGER, REAL): ").strip().upper()

        if not col_name or not col_type:
            print("Both name and type are required. Try again.")
            continue
            
        # Optional: Ask if the column should be NOT NULL
        not_null = input(f"Should '{col_name}' be NOT NULL? (y/n, default is n): ").strip().lower()
        constraint = " NOT NULL" if not_null == 'y' else ""

        # Format the column definition string
        columns.append(f"{col_name} {col_type}{constraint}")

        print(f"Added column: {col_name} {col_type}{constraint}")
        
    # 3. Construct the final SQL command
    # Join all column definitions with a comma and a space
    column_definitions = ",\n    ".join(columns)
    
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {column_definitions}
    );
    """
    
    # 4. Execute the command
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        print(f"\nExecuting SQL:\n{create_table_sql}")
        cursor.execute(create_table_sql)
        conn.commit()
        
        print(f"✅ Success! Table '{table_name}' has been created in '{db_name}'.")
        
    except sqlite3.Error as e:
        print(f"\n❌ A database error occurred. Table was not created: {e}")
        
    finally:
        if conn:
            conn.close()

# ----------------------------------------------------------------------

if __name__ == "__main__":
    # The database file name is explicitly set to "dragon.db"
    create_table_with_dynamic_columns(db_name="dragon.db")