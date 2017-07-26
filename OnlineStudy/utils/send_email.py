from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailVerifyRecord
import string
import random


def get_random_string():
    random_string = string.ascii_letters + string.digits
    code_string = ''
    for i in range(16):
        code_string += random_string[random.randint(0, len(random_string) - 1)]
    return code_string


def send_email(email, type):
    code = get_random_string()
    from_email = settings.EMAIL_FROM
    email_verify = EmailVerifyRecord()
    subject = ''
    message = ''
    html_message = ''
    if type == "register":
        base_url = 'http://127.0.0.1:8000/users/register_active?{}={}'.format(type, code)
        subject = "欢迎注册.."
        message = "请点击下面的链接进行激活注册"
        html_message = '<h3><a href={0}>{1}</a></h3>'.format(base_url, message + base_url)
        type = '0'
    elif type == 'forget':
        base_url = 'http://127.0.0.1:8000/users/forget_active?{}={}'.format(type, code)
        subject = "点击链接修改确认修改密码.."
        message = "请点击下面的链接进行确认修改密码"
        html_message = '<h3><a href={0}>{1}</a></h3>'.format(base_url, message + base_url)
        type = '1'
    email_verify.email = email
    email_verify.code = code
    email_verify.send_type = type
    email_verify.save()
    return send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[email],
                     html_message=html_message)
