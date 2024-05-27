from requests import get
from bs4 import BeautifulSoup

def get_page_count(keyword):
    response = get(f"https://web3.career/{keyword}-jobs")
    if response.status_code != 200:
        print(f"Error {response.status_code}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("ul", class_="pagination")
        if pagination == None:
            return 1
        pages = pagination.find_all("li", recursive=False)
        count = len(pages)
        if count >= 5:
            return 5
        else:
            return count

def extract_web3_jobs(keyword):
    pages = get_page_count(keyword)
    jobs_db = []
    for page in range(pages):
        print(f"Scrapping page: https://web3.career/{keyword}-jobs?page={page+1}")
        response = get(f"https://web3.career/{keyword}-jobs?page={page+1}")
        if response.status_code != 200:
            print(f"Error {response.status_code}")
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find("tbody", class_="tbody").find_all("tr")
    
            for job in jobs:
                position = job.find("td", scope="row").text.strip()
                link = job.find("td", scope="row").find("a")["href"]
                company = job.find("td", class_="job-location-mobile").text.strip()
                job_data = {
                    'position': position,
                    'company': company,
                    'link': f"https://web3.career{link}",
                    'platform': "Web3"
                }
                jobs_db.append(job_data)

    return jobs_db