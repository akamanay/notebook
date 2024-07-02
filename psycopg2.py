import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost",  # or your server IP
    port="5432"  # default PostgreSQL port
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM your_table_name")

# Fetch all rows from the last executed statement
rows = cur.fetchall()

for row in rows:
    print(row)

# Close communication with the database
cur.close()
conn.close()

import os

# Accessing an environment variable
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']

print(f"Database User: {db_user}")
print(f"Database Password: {db_pass}")

