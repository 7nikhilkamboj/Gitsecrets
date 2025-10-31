import os
from datetime import datetime

api_key = os.getenv("API_KEY")
#db_password = os.getenv("DB_PASSWORD")

print(f"API Key: {api_key}")
#print(f"DB Password: {db_password}")
print("Running scheduled Python job...")
print("Current UTC time:", datetime.utcnow())
