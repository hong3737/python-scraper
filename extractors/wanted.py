from extractors.job import Job
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
# import time 

PLATFORM="Wanted"

class Wanted(Job):

    def get_pages(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

        # 개체 하나씩 선택해서 url 이동하기 
        # page.click("button.Aside_searchButton__Xhqq3")
        # # == page.locator("button.Aside_searchButton__Xhqq3").click()
        # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
        # time.sleep(5)
        # page.keyboard.down("Enter")
        # time.sleep(4)
        # page.click("a#search_tab_position")

        # 스크린샷 저장
        # self.save_to_screen(page, keyword)

        for x in range(5):
            page.keyboard.down("End")

        content = page.content()
        p.stop()

        return content

    def save_to_screen(self, page, keyword):
        page.screenshot(path=f"{PLATFORM}_{keyword}_screenshot.png")

    def scrape_page(self, content):
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")

        jobs_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            position = job.find("strong", class_="JobCard_title__ddkwM").text
            company = job.find("span", class_="JobCard_companyName__vZMqJ").text

            job = super().save_data(position, company, link, PLATFORM)
            jobs_db.append(job)

        # print(len(jobs_db))
        return jobs_db
