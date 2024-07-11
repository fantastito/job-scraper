from yoto_scraper import yoto_scraper
import send_email

def lambda_handler(event, context):
    
    email_body = []
    
    email_body.append(yoto_scraper())
    # print(email_body)

    send_email(email_body)
    return {"statusCode": 200}