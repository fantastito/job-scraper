from bs4 import BeautifulSoup
import requests

def yoto_scraper():
    url = "https://careers.yotoplay.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        # General request exception
        return {"statusCode": 500}
    except Exception as e:
        # Any unexpected exceptions
        return {"statusCode": 500}
    
    soup = BeautifulSoup(response.content, "lxml")
    # for link in soup.find(id="jobs_list_container"):
    #     print(link.get('href'))
    # return "that worked?"
    print(soup.find(class_="jobs-container"))

yoto_scraper()