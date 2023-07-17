from celery import shared_task, current_task
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template, render_to_string

from House24.celery import app


@app.task(bind=True)
def send_invitation(self, to='somebody@gmail.com', ):
    html_template = 'admin_panel/invitation_email.html'
    html_message = render_to_string(html_template)
    message = EmailMessage('Приглашение в House24', html_message, 'dhushchyn@gmail.com', [to])
    message.content_subtype = 'html'  # this is required because there is no plain text email message
    message.send()


@app.task(bind=True)
def send_receipt(self, id, to='somebody@gmail.com'):
    html_template = 'admin_panel/receipt_email.html'
    html_message = render_to_string(html_template, {'id': id})
    message = EmailMessage('Электронная квитанция House24', html_message, 'dhushchyn@gmail.com', [to])
    message.content_subtype = 'html'  # this is required because there is no plain text email message
    message.send()
