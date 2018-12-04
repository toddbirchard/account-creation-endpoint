# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
from python_http_client import exceptions
import datetime
import json


def welcome_email(email_address):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    mail = Mail()
    mail.from_email = Email('toddbirchard@gmail.com')
    mail.to_email = Email(email_address)
    mail.subject = "Welcome to Hackers and Slackers"
    mail.template_id = 'd-79888eacf2a74def8d2b673891b2f75a'


    response = sg.client.mail.send.post(request_body=mail.get())
    status = b"{}".decode('utf-8').format(response.status_code)
    body = b"{}".decode('utf-8').format(response.body)
    headers = b"{}".decode('utf-8').format(response.headers)
    content = Content("text/html", '<p>You\'re so close to becoming a member of <strong>Hackers and Slackers!</strong> The only thing left is to click that button down there.</p></div><div>&nbsp;</div><div><p>But let\'s pump the breaks for a second: I feel like I need to tell you something before we take this relationship any further. By joining our community, you\'re joining our family. That means we love you. Unconditionally. We will be there when times are hard. We will be be attending your wedding with tears in our eyes as we watch you grow into the epitome of success we always knew you\'d be. <p></div><div>&nbsp;</div><div><p style="margin-bottom:20px;">We will have good times. We will have bad times. But at the end of it all, we will always have each other - as well as a blog about data science or whatever. </p>')
    data = {
        'status': status,
        'body': body,
        'headers': headers.splitlines(),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
