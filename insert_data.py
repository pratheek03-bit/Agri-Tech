import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO crop_disease_data
(image_path, city, state, crop_type, disease_type, confidence_percentage, recommendations, cost, fertilizer_use, fungicide, crop_rotation, water_management)

VALUES
('leaf001.jpg','Bangalore','Karnataka','Tomato','Leaf Spot',92.5,'Apply copper fungicide',150,'NPK','Copper Fungicide','Rotate with legumes','Avoid overwatering')
""")

conn.commit()
conn.close()

print("Data inserted successfully!")