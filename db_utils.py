# db_utils.py

import mysql.connector
import streamlit as st
from db import get_db_connection

def save_file_details(user_id, file_name, ipfs_link, encryption_key):
    conn = mysql.connector.connect(
        host="localhost",
            user="root",
            password="",
            database="project"
    )
    cursor = conn.cursor()
    
    # Insert into the files table
    sql = "INSERT INTO files (user_id, file_name, ipfs_link, encryption_key) VALUES (%s, %s, %s, %s)"
    values = (user_id, file_name, ipfs_link, encryption_key)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12727620",
        password="XAA48qmmxS",
        database="sql12727620"
    )

def save_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_user_files(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT file_name, ipfs_link, encryption_key FROM files WHERE user_id = %s", (user_id,))
        files = cursor.fetchall()
        return files
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        cursor.close()
        conn.close()
