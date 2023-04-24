import streamlit as st
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="database_name",
    user="postgres",
    password="linux"
)

# Define a function to create a new user
def create_user(name, email, age):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s);", (name, email, age))
    conn.commit()
    st.success("User created successfully!")

# Define a function to retrieve all users
def get_users():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
    return rows

# Define a function to update a user's information
def update_user(id, name, email, age):
    with conn.cursor() as cur:
        cur.execute("UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s;", (name, email, age, id))
    conn.commit()
    st.success("User information updated successfully!")

# Define a function to delete a user
def delete_user(id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id=%s;", (id,))
    conn.commit()
    st.success("User deleted successfully!")

# Display a form for creating a new user
st.subheader("Create new user")
name = st.text_input("Name")
email = st.text_input("Email")
age = st.number_input("Age", min_value=0)
if st.button("Create", key= "Create"):
    create_user(name, email, age)

# Display a list of all users
st.subheader("All users")
users = get_users()
for user in users:
    st.write(f"Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
    if st.button("Delete", key=f"delete_btn_{user[0]}"):
        delete_user(user[0])

# Display a form for updating a user's information
st.subheader("Update user information")
id = st.number_input("ID", min_value=1)
name = st.text_input("Name", key="Name")
email = st.text_input("Email", key="Email")
age = st.number_input("Age", min_value=0, key="Age")
if st.button("Update User"):
    update_user(id, name, email, age)
