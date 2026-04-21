import requests
import feedparser
import json
import os

RSS_URL = "https://rsshub.app/facebook/page/你的页面"
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

DATA_FILE = "data.json"

# 读取历史记录
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"last": ""}

feed = feedparser.parse(RSS_URL)

if feed.entries:
    entry = feed.entries[0]

    # 防止重复发送
    if entry.link != data["last"]:
        data["last"] = entry.link

        requests.post(WEBHOOK_URL, json={
            "content": f"📢 逆水寒更新：\n{entry.title}\n{entry.link}"
        })

        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
