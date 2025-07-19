import requests
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables (API key, Snowflake credentials)
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION_CODE = "DE"

# --- Step 1: Fetch Category Metadata from YouTube API ---
CATEGORY_URL = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode={REGION_CODE}&key={API_KEY}"
response = requests.get(CATEGORY_URL)
data = response.json()

# --- Step 2: Extract category_id and category_name ---
records = []
for item in data['items']:
    category_id = int(item['id'])
    category_name = item['snippet']['title']
    records.append({"category_id": category_id, "category_name": category_name})

df = pd.DataFrame(records)

# --- Step 3: Connect to Snowflake ---
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse="YOUTUBE_WH",
    database="YOUTUBE_DB",
    schema="PUBLIC"
)
cursor = conn.cursor()

# --- Step 4: Create the CATEGORY_MAPPING table (if not exists) ---
cursor.execute("""
    CREATE OR REPLACE TABLE YOUTUBE_DB.DIM.CATEGORY_MAPPING (
        category_id INT,
        category_name STRING
    );
""")

# --- Step 5: Insert rows into CATEGORY_MAPPING ---
# Optional: clear existing rows if needed
cursor.execute("TRUNCATE TABLE YOUTUBE_DB.DIM.CATEGORY_MAPPING")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO YOUTUBE_DB.DIM.CATEGORY_MAPPING (category_id, category_name)
        VALUES (%s, %s)
    """, (row['category_id'], row['category_name']))

# --- Cleanup ---
cursor.close()
conn.close()

print("✅ YouTube category mapping loaded into Snowflake!")
