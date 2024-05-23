from playwright.sync_api import sync_playwright
import time 
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# time.sleep(5)

# page.click("button.Aside_searchButton__Xhqq3")
# # == page.locator("button.Aside_searchButton__Xhqq3").click()

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(4)

# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    job = {
        "title":title,
        "conpany_name":company_name,
        "link":link,
    }
    jobs_db.append(job)

#csv : comma separated values
file = open("jobs.csv", mode="w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow([
        "Title",
        "Company",
        "Link"
    ])

for job in jobs_db:
    writer.writerow(job.values())
file.close()

# print(jobs_db)
# print(len(jobs_db))

# page.screenshot(path="screenshot.png")

#url challenge, keyword.csv, OOP
keywords = [
    "flutter",
    "nextjs",
    "kotlin"
]