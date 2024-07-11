# job-scraper

job-scraper is an evolution of [new_rosti_scraper](https://github.com/fantastito/new_rosti_scraper), applying web scraping to looking for jobs.

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![AWS Lambda Badge](https://img.shields.io/badge/AWS%20Lambda-F90?logo=awslambda&logoColor=fff&style=flat) ![Amazon Simple Email Service Badge](https://img.shields.io/badge/Amazon%20Simple%20Email%20Service-DD344C?logo=amazonsimpleemailservice&logoColor=fff&style=flat) ![Docker Badge](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=flat)

Using AWS Lambda, BeautifulSoup and AWS Simple Email Service, a cron expression triggers a daily check on the careers pages for a number of companies and returns links to all current open positions.