from threading import Thread

from flask_mail import Message

from app import current_app
from app import mail

from typing import List


def send_async_email(app: current_app, msg: Message) -> None:
    """
    Асинхронная обёртка для отправки email сообщения
    :param app: Экземпляр приложения
    :param msg:
    :return:
    """
    with app.app_context():
        mail.send(msg)


def send_email(subject: str, sender: str, recipients: List[str], text_body: str, html_body: str,
               attachments=None, sync=False) -> None:
    """
    Отправка email сообщения
    :param subject: тема письма
    :param sender: адрес почты отправителя
    :param recipients: адрес почты получателя
    :param text_body:
    :param html_body:
    :return:
    """
    with current_app.app_context():
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body

        if attachments:
            for attachment in attachments:
                msg.attach(*attachment)
        if sync:
            mail.send(msg)
        else:
            # Запуск потока
            Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
