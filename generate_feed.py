#!/usr/bin/env python3
import csv
import html
from datetime import datetime, timezone

SITE_URL = "https://nhranitzky.github.io"
SITE_TITLE = "Norbert Hranitzky"
SITE_DESCRIPTION = "Notes, essays, and experiments"

with open("_data/toc.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

rows.sort(key=lambda r: r["date"], reverse=True)

items = []
for row in rows:
    link = f"{SITE_URL}/{row['url']}"
    pub_date = datetime.strptime(row["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    items.append(f"""    <item>
      <title>{html.escape(row['title'])}</title>
      <link>{html.escape(link)}</link>
      <guid>{html.escape(link)}</guid>
      <description>{html.escape(row['summary'])}</description>
      <pubDate>{pub_date.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
    </item>""")

now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S %z")

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{html.escape(SITE_TITLE)}</title>
    <link>{html.escape(SITE_URL)}</link>
    <description>{html.escape(SITE_DESCRIPTION)}</description>
    <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(feed)
