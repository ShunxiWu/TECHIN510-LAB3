import sqlite3
import psycopg2
import os

import streamlit as st
from pydantic import BaseModel
import streamlit_pydantic as sp

PG_USER = "shunxiwu"
PG_PASSWORD = "123ZhaiXia**SongGeiNi"
PG_HOST = "shunxiwu.postgres.database.azure.com"
PG_PORT = 5432  # Replace with your actual port

# Connect to our database
DB_CONFIG = os.getenv("DB_TYPE")
if DB_CONFIG == 'PG':
    PG_USER = os.getenv("PG_USER")
    con = psycopg2.connect(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/burnbook?connect_timeout=10&application_name=burnbook")
else:
    con = sqlite3.connect("burn_book.sqlite", isolation_level=None)
cur = con.cursor()

# Create the table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        Gossip TEXT,
        is_confirmed BOOLEAN
    )
    """
)

# Define our Form
class Task(BaseModel):
    name: str
    gossip: str
    is_confirmed: bool

# This function will be called when the check mark is toggled, this is called a callback function
def toggle_is_confirmed(is_confirmed, row, cur):
    cur.execute(
        """
        UPDATE tasks SET is_confirmed = ? WHERE id = ?
        """,
        (is_confirmed, row[0]),
    )

# Function to delete a gossip
def delete_gossip(gossip_id, cur):
    cur.execute(
        """
        DELETE FROM tasks WHERE id = ?
        """,
        (gossip_id,),
    )

def main():
    st.header("🔥 The Burnt Book 🔥")
    st.subheader("Anonymously Share Your Friends' Gossips")


    # Connect to our database inside the main function
    DB_CONFIG = os.getenv("DB_TYPE")
    if DB_CONFIG == 'PG':
        PG_USER = os.getenv("PG_USER")
        con = psycopg2.connect(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/burnbook?connect_timeout=10&application_name=burnbook")
    else:
        con = sqlite3.connect("burn_book.sqlite", isolation_level=None, check_same_thread=False)
    cur = con.cursor()

    # Create the table
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            Gossip TEXT,
            is_confirmed BOOLEAN
        )
        """
    )

    # Create a Form using the streamlit-pydantic package, just pass it the Task Class
    data = sp.pydantic_form(key="task_form", model=Task)
    if data:
        cur.execute(
            """
            INSERT INTO tasks (name, gossip, is_confirmed) VALUES (?, ?, ?)
            """,
            (data.name, data.gossip, data.is_confirmed),
        )

    data = cur.execute(
        """
        SELECT * FROM tasks
        """
    ).fetchall()

    # HINT: how to implement an Edit button?
    cols = st.columns(3)
    cols[0].write("Confirmed?")
    cols[1].write("Name")
    cols[2].write("Gossip")

    for row in data:
        cols = st.columns(3)
        cols[0].checkbox('is_confirmed', row[3], label_visibility='hidden', key=row[0], on_change=toggle_is_confirmed, args=(not row[3], row, cur))
        cols[1].write(row[1])
        cols[2].write(row[2])

        if st.button(f"Delete {row[1]}", key=f"delete_button_{row[0]}"):
            delete_gossip(row[0], cur)

if __name__ == "__main__":
    main()