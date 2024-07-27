# Database Setup Guide

## 1. Schema Definition

The database schema is defined in `database_schema.sql`:

- **`equipment` Table**: Stores details about film equipment.
  - `id`: Unique identifier for each item.
  - `name`: Name of the equipment.
  - `availability`: Availability status (1 for available, 0 for not available).
  - `price`: Price of the equipment.

- **`reviews` Table** (Optional): Stores customer reviews.
  - `id`: Unique identifier for each review.
  - `email`: Email of the reviewer.
  - `review`: The review text.
  - `sentiment`: Sentiment of the review ('positive' or 'negative').
  - `created_at`: Timestamp of the review creation.

## 2. Setting Up the Database

1. **Create the Database**:
   - Run the `create_db.py` script to create the database and apply the schema:
     ```bash
     python database/create_db.py
     ```

2. **Insert Sample Data** (Optional):
   - Run the `insert_data.py` script to insert sample data into the database:
     ```bash
     python database/insert_data.py
     ```

## 3. Verification

Ensure that the database file `equipment.db` is created in the `database` directory. You can use SQLite tools or scripts to verify the schema and data.
