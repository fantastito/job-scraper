from bs4 import BeautifulSoup
import requests

def yoto_scraper():
    #Get jobs page and handle errors
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
    
    # Parse the page content
    soup = BeautifulSoup(response.content, "lxml")

    #Extract only the current jobs section
    jobs = soup.find(class_="jobs-container")
    
    #Find all the links
    links = jobs.find_all('a')
    
    #Extract links and append to list
    job_links = []

    for link in links:
        job_links.append(link.get('href'))
        # print(link.get('href'))

    return job_links

# yoto_scraper()