# YouTube Trending Data Pipeline & Dashboard

## Overview
This project builds an end-to-end data pipeline that extracts YouTube trending video data from the YouTube Data API, enriches it with category metadata, stores it in Snowflake, and visualizes key insights using Power BI.

---

## Features
- **Data Ingestion:** Fetches trending videos and category metadata from YouTube API.
- **Data Storage:** Raw and dimension data stored in Snowflake tables.
- **Data Transformation:** Enriches raw video data by joining with category mappings.
- **Visualization:** Interactive Power BI dashboard showcasing video trends, engagement metrics, and category insights.
- **Automation Ready:** Modular Python scripts enable easy scheduling and automation.

---

## Architecture

YouTube API → Raw Data (Snowflake RAW schema)
→ Category Data (Snowflake DIM schema)
→ Enriched Data (Snowflake TRANSFORMED schema)
→ Power BI Dashboard

---

## Prerequisites
- Python 3.x
- Snowflake account with proper access and warehouse
- YouTube Data API key
- Power BI Desktop
- `.env` file with the following variables:

YOUTUBE_API_KEY=your_youtube_api_key
SNOWFLAKE_USER=your_snowflake_user
SNOWFLAKE_PASSWORD=your_snowflake_password
SNOWFLAKE_ACCOUNT=your_snowflake_account


---

## Installation & Setup

1. Clone this repo:
git clone https://github.com/yourusername/youtube-trending-pipeline.git
cd youtube-trending-pipeline

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt




