import streamlit as st
import psycopg2

# Define function to establish database connection
def create_conn():
    conn = psycopg2.connect(
        host="localhost",
        database="database_name",
        # database="streamlitdb",
        user="postgres",
        password="linux"
    )
    return conn

# Connect to database
conn = create_conn()

# Define SQL query
query = "SELECT * FROM users;"
# query = "SELECT * FROM streamlitTable;"

# Execute query
cur = conn.cursor()
cur.execute(query)

# Fetch and display results
results = cur.fetchall()
for row in results:
    st.write(row)

# Close cursor and connection
cur.close()
conn.close()
