from yoto_scraper import yoto_scraper
from send_email import send_email

def lambda_handler(event, context):
    
    scraping_results = []
    
    # Append the result of scrapers to scraping_results
    scraping_results.append(yoto_scraper())
    
    # List compresension to flatten format into string
    flattened_results = [item for sublist in scraping_results for item in sublist]
    
    # Convert list of strings into a single string with HTML formatting
    email_body = '<br>'.join(flattened_results)

    send_email(email_body)
    return {"statusCode": 200}