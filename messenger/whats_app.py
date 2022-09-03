import os
from twilio.rest import Client
from decouple import config
from db.file_provider import get_file_content_as_list

account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
phone_numbers = get_file_content_as_list("phone_numbers.txt")
client = Client(account_sid, auth_token)


def send_notification(body: str, media_urls: list):
    for number in phone_numbers:
        client.messages.create(
            body=body,
            from_='whatsapp:+14155238886',
            to=f'whatsapp:+{number}',
            media_url=media_urls
        )
