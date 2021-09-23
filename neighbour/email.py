from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_abdi_email(title, content, reciever):
    # creating message subject and sender 
    subject = 'Alert'
    sender = 'Neigbourhood'
    
    # passing in the context variable
    text_content = render_to_string('email/abdiemail.txt', {"title": title, "content": content})
    html_content = render_to_string('email/abdimail.html', {"title": title, "content": content})

    message = EmailMultiAlternatives(subject, text_content, sender, [reciever])
    message.attach_alternative(html_content, 'text/html')
