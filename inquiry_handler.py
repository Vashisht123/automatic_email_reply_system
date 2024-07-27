# src/inquiry_handler.py
import sqlite3
import os

def handle_inquiry(email_text):
    # Use an absolute path for the database
    db_path = os.path.join(os.path.dirname(__file__), '../database/equipment.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    item_name = email_text.split()[-1]  # assuming the last word is the item name
    cursor.execute("SELECT availability, price FROM equipment WHERE name=?", (item_name,))
    result = cursor.fetchone()
    if result:
        availability, price = result
        if availability:
            return f"The {item_name} is available at ${price}."
        else:
            cursor.execute("SELECT name FROM equipment WHERE availability=1")
            alternatives = cursor.fetchall()
            return f"The {item_name} is not available. Similar items: {', '.join([alt[0] for alt in alternatives])}."
    else:
        return "Item not found."
