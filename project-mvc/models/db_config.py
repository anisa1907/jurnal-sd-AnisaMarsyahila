from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DB_PASSWORD")

print("DB Password:", db_password)