from celery import shared_task
from templated_mail.mail import BaseEmailMessage

@shared_task
def MailSending(email):
    message=BaseEmailMessage(
        template_name='email.html',
        context={'email':email}
    )
    message.send([email])
    
    return "mail send successfully"