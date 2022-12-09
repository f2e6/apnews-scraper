import requests
import re
import subprocess

url = "https://apnews.com/hub/ap-top-news"

response = requests.get(url)

titles = re.findall(r"<h2 class=\"[^\"]+\">([^<]+)</h2>", response.text)
links = re.findall(r"data-key=\"card-headline\" href=\"([^\"]+)", response.text)

for i, title in enumerate(titles):
    print(f"{i+1}. {title}")

article_num = int(input("Enter the number of the article you want to view: "))

link = links[article_num-1]

link = f"https://apnews.com{link}"

selected_article_link = link
subprocess.run(["rdrview", "-B", "lynx", link])
