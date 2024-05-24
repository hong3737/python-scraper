from job import Job
import requests
from bs4 import BeautifulSoup

PLATFORM="Wwr"


class Wwr(Job):
  base_url = ""
  def scrape_page(self, keyword):
    print(f"Scraping page {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    all_jobs = []

    for job in jobs:
      title = job.find("span", class_="title").text
      company, position, region = job.find_all("span", class_="company")[0:3]
      url = job.find_all("a")[1]["href"]
      job_data = {
          "title": title,
          "company": company.text,
          "position": position.text,
          "region": region.text,
          "url": f"https://weworkremotely.com/{url}"
      }
      all_jobs.append(job_data)


  def get_pages(self, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(
        soup.find("div", class_="pagination").find_all("span", class_="page"))


  # url = "https://weworkremotely.com/remote-full-time-jobs?page=1"
  # total_pages = get_pages(url)

  # for x in range(total_pages):
  #   url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  #   scrape_page(url)

  # print(len(all_jobs))

  # User-Agent 차단 사이트
  # r = requests.get(
  #     "https://remoteok.com/remote-flutter-jobs",
  #     headers={
  #         "User-Agent":
  #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
  #     })
  # print(r.status_code)
