import sqlite3
from faker import Faker

fake = Faker()

# Connect to SQLite database (this simulates the data store)
conn = sqlite3.connect('healthcare_data_store.db')
cursor = conn.cursor()

# Create a table for storing healthcare patient data
cursor.execute('''
CREATE TABLE IF NOT EXISTS patient_data (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    ssn TEXT NOT NULL,
    medical_record_number TEXT NOT NULL,
    insurance_id TEXT NOT NULL
)
''')

# Insert fake data into the store (simulating healthcare patient information)
def insert_fake_data():
    for _ in range(10):  # Insert 10 fake entries for this example
        name = fake.name()  # Fake patient name
        age = fake.random_int(min=18, max=90)  # Fake age
        ssn = fake.ssn()  # Fake SSN
        medical_record_number = fake.uuid4()  # Fake medical record number
        insurance_id = fake.uuid4()  # Fake insurance ID
        
        cursor.execute('''
        INSERT INTO patient_data (name, age, ssn, medical_record_number, insurance_id) 
        VALUES (?, ?, ?, ?, ?)
        ''', (name, age, ssn, medical_record_number, insurance_id))

    conn.commit()

# Insert the fake data
insert_fake_data()

# Function to search the fake data store (vector store simulation)
def search_fake_data(query: str):
    cursor.execute('''
    SELECT * FROM patient_data WHERE name LIKE ? OR ssn LIKE ? OR medical_record_number LIKE ? OR insurance_id LIKE ?
    ''', ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))
    return cursor.fetchall()

# Close the connection
conn.close()
