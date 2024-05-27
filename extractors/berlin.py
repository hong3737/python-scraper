from requests import get
from bs4 import BeautifulSoup

url = "https://berlinstartupjobs.com/skill-areas/"

def extract_berlin_jobs(keyword):
  response = get(f"{url}{keyword}", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"})
  
  jobs_db = []
  
  if response.status_code != 200:
      print(f"Error {response.status_code}")
  else:
      soup = BeautifulSoup(response.text, "html.parser")
      jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
      for job in jobs:
          position = job.find("h4", class_="bjs-jlid__h").text
          link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
          company = job.find("a",class_="bjs-jlid__b").text
          job_data = {
              'position': position,
              'company': company,
              'link': link,
              'platform': "Berlin"
          }
          jobs_db.append(job_data)
  
  return jobs_db