import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create a cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS crop_disease_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    district TEXT,
    crop_type TEXT,
    disease_type TEXT,
    confidence_percentage REAL,
    recommendations TEXT,
    cost INTEGER,
    fertilizer_use TEXT,
    fungicide TEXT,
    crop_rotation TEXT,
    water_management TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

print("Database and table created successfully!")

# Save changes
conn.commit()

# Close connection
conn.close()