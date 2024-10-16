import os
from dotenv import load_dotenv

# Load environment variables from the specified .env file
load_dotenv(r'C:\Users\MMM\Documents\10 Academy File\KAIM-Week-7\notebooks\.env')

# Access the environment variables using os.getenv
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('PHONE')

# Debugging: Print the loaded values
print(f"API ID: {api_id}, API Hash: {api_hash}, Phone: {phone}")
