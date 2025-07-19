import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def enrich_youtube_data():
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse="YOUTUBE_WH",
            database="YOUTUBE_DB",
            schema="TRANSFORMED"
        )
        cursor = conn.cursor()

        # Enrichment SQL joining raw with category mapping
        enrichment_sql = """
        CREATE OR REPLACE TABLE YOUTUBE_DB.TRANSFORMED.YOUTUBE_TRENDING_ENRICHED AS
        SELECT
          yt.video_id,
          yt.title,
          yt.published_at,
          yt.category AS category_id,
          cat.category_name,
          yt.views,
          yt.likes,
          yt.comments,
          yt.data_loaded_at
        FROM
          YOUTUBE_DB.RAW.YOUTUBE_TRENDING_RAW yt
        LEFT JOIN
          YOUTUBE_DB.DIM.CATEGORY_MAPPING cat
        ON
          yt.category = cat.category_id;
        """

        print("Starting enrichment transformation...")
        cursor.execute(enrichment_sql)
        print("Enriched table created or replaced successfully.")

    except Exception as e:
        print("Error during enrichment transformation:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    enrich_youtube_data()
