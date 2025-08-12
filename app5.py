import requests
from send_email import send_email
import os

api_key= "a75fa1f61988439ca9e3085c7c7ae6f0"
url= "https://newsapi.org/v2/everything?q=tesla&from2025-07-12&sortBy=publishedAt&apiKey=a75fa1f61988439ca9e3085c7c7ae6f0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}
params = {
    "q": "tesla",
    "from": "2025-07-12",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
}

#make a req

request= requests.get(url,params=params,headers=headers)
content = request.json()
body=""
for article in content['articles']:
    if article["title"] is not None:
        body= (body+article["title"] +"\n"+article["description"]+"\n"+article["url"]
               +"\n"+article["url"]+2*"\n")
body=body.encode("utf-8")
send_email(message=body)
#a75fa1f61988439ca9e3085c7c7ae6f0