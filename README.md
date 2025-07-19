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
