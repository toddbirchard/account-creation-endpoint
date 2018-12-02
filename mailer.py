# using SendGrid's Python Library - https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import Email, Substitution, Mail, Personalization
from python_http_client import exceptions


def welcome_email(email):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    personalization = Personalization()
    personalization.add_to(Email("sendgridtesting@gmail.com"))

    sg = SendGridAPIClient()
    mail = Mail()
    mail.from_email = Email('todd@hackersandslackers.com')
    mail.template_id = 'd-79888eacf2a74def8d2b673891b2f75a'
    p = Personalization()
    p.add_to(Email(email))
    mail.add_personalization(personalization)

    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except exceptions.BadRequestsError as e:
        print(e.body)
        exit()
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
