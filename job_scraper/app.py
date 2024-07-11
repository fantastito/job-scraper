from yoto_scraper import yoto_scraper
from send_email import send_email

def lambda_handler(event, context):
    
    scraping_results = []
    
    scraping_results.append(yoto_scraper())
    # print(email_body)

    #Convert list of strings into single string
    email_body = '\n'.join(scraping_results)

    send_email(email_body)
    return {"statusCode": 200}