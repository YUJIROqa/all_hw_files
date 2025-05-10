import psycopg2
import psycopg2.extras
import creds
import os
import dotenv

dotenv.load_dotenv()

w = '='*50

db = psycopg2.connect(
    host = os.getenv('DB_HOST'),
    database = os.getenv('DB_NAME'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    port = os.getenv('DB_PORT')
)

print(w)

cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor) 
cursor.execute("SELECT * FROM students")
data = cursor.fetchall()
print(data)
