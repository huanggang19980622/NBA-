from django.shortcuts import HttpResponse
import logging


# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')


def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')