from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import UserLog
@receiver(request_finished)
def all_log(sender,**kwargs):
    print(sender,kwargs)
    print("使用信号记日志")
# @receiver(post_save,sender=MailLog)
# def send_mail(sender,instance,**kwargs):
#
@receiver(post_save,sender=UserLog)
def send_mail(sender,instance,**kwargs):
    print(sender,instance,kwargs)
    import time
    time.sleep(20)
    print("发邮件需要20s")


