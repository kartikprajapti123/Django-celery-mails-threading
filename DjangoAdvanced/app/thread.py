import threading
from templated_mail.mail import BaseEmailMessage


def run():
        try:
            print("threading is started")
            
            message=BaseEmailMessage(
                template_name='email.html',
                context={
                    'name':'my name is kartik'
                }
            )
            message.send(['mysterious.stories1234@gmail.com'])
            
        except Exception as e:
            print(e)