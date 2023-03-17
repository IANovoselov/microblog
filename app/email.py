from flask_mail import Message
from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user):
    msg = Message('test subject', sender=['your-email1@example.com'], recipients=['your-email@example.com'])
    msg.body = 'text_body'
    msg.html = '<h1>HTML body</h1>'
    mail.send(msg)