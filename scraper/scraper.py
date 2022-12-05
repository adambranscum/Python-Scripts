import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/jobs?q=&l=North+Little+Rock%2C+AR&from=searchOnHP&vjk=c424e9c2a5e60b51"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

job_element = soup.find_all("div", class_="title")


for job_element in job_element:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("span", class_="location")
    location_element = job_element.find("span", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()