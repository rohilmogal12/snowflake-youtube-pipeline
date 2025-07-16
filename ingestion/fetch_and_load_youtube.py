import requests
import pandas as pd
import snowflake.connector
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Get API key from env
API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION_CODE = "DE"
URL = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={REGION_CODE}&maxResults=20&key={API_KEY}"

response = requests.get(URL)
data = response.json()

# Extract relevant data
records = []
for item in data['items']:
    records.append({
        "video_id": item["id"],
        "title": item["snippet"]["title"],
        "published_at": item["snippet"]["publishedAt"],
        "category": item["snippet"]["categoryId"],
        "views": int(item["statistics"].get("viewCount", 0)),
        "likes": int(item["statistics"].get("likeCount", 0)),
        "comments": int(item["statistics"].get("commentCount", 0))
    })

df = pd.DataFrame(records)

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse="YOUTUBE_WH",
    database="YOUTUBE_DB",
    schema="RAW"
)
cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO YOUTUBE_TRENDING_RAW (video_id, title, published_at, category, views, likes, comments)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (row.video_id, row.title, row.published_at, row.category, row.views, row.likes, row.comments))

cursor.close()
conn.close()
