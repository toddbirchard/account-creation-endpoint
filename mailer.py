# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import Email, Substitution, Mail, Personalization
from python_http_client import exceptions
import datetime
import json


def welcome_email(email_address):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    sg = SendGridAPIClient()
    from_email = Email('toddbirchard@gmail.com')
    to_email = Email(email_address)
    subject = "Welcome to Hackers and Slackers"
    template_id = 'd-79888eacf2a74def8d2b673891b2f75a'

    mail = Mail(from_email, subject, to_email, template_id)
    response = sg.client.mail.send.post(request_body=mail.get())
    status = b"{}".decode('utf-8').format(response.status_code)
    body = b"{}".decode('utf-8').format(response.body)
    headers = b"{}".decode('utf-8').format(response.headers)
    data = {
        'status': status,
        'body': body,
        'headers': headers.splitlines(),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
