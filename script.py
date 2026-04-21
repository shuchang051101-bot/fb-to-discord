import requests
import feedparser
import json
import os

RSS_URL = "https://rss.app/feeds/oTffud10xdTFuH3B.xml"
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

DATA_FILE = "data.json"

# 读取历史记录
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"last": ""}

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    exit()

entry = feed.entries[0]
latest_link = entry.get("link", "")

# 去重逻辑
if latest_link and latest_link != data["last"]:

    data["last"] = latest_link

    requests.post(WEBHOOK_URL, json={
        "content": "📢 逆水寒更新",
        "embeds": [
            {
                "title": entry.get("title", "无标题"),
                "url": latest_link,
                "description": "点击查看详情",
                "color": 5814783
            }
        ]
    })

    # 保存状态
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

        requests.post(WEBHOOK_URL, json={
    "content": "📢 逆水寒更新",
    "embeds": [
        {
            "title": entry.title,
            "url": entry.link,
            "description": "点击查看详情",
            "color": 5814783
        }
    ]
})

        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
