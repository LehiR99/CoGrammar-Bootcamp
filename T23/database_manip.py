import sqlite3

# Function to create the table
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS python_programming
                 (id INT PRIMARY KEY NOT NULL,
                 name TEXT NOT NULL,
                 grade INT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to insert rows
def insert_rows():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    data = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]
    c.executemany('INSERT OR IGNORE INTO python_programming VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

# Function to select records with grade between 60 and 80
def select_records():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Function to update Carl Davis's grade
def update_carl_grade():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis"')
    conn.commit()
    conn.close()

# Function to delete Dennis Fredrickson's row
def delete_dennis_row():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson"')
    conn.commit()
    conn.close()

# Function to update grades for ids greater than 55
def update_grades_above_55():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')
    conn.commit()
    conn.close()

# Function to display all rows for verification
def display_all_rows():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM python_programming')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Main execution
if __name__ == '__main__':
    create_table()
    insert_rows()

    print("Rows with grade between 60 and 80:")
    select_records()

    update_carl_grade()

    delete_dennis_row()

    update_grades_above_55()

    print("\nUpdated rows:")
    display_all_rows()
