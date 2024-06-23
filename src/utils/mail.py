import yagmail
import traceback
from src.utils.logger import logger


class Mail:
    def __init__(self):
        from src.utils.yamlloader import Yamlloader
        self.__mail_conf = Yamlloader().load(r'conf/mail.yaml')

    def send_mail(self, subject, content, attachments=None):
        """
            发送邮件
        """
        if self.__mail_conf['active']:
            logger.info('开始发送邮件')
            try:
                yag_mail = yagmail.SMTP(**self.__mail_conf['sender'])
                yag_mail.send(to=self.__mail_conf['receiver'],
                              cc=self.__mail_conf['cc'],
                              subject=subject,
                              contents=content,
                              attachments=attachments)
                logger.success('邮件发送成功')
                return True
            except:
                logger.error(f'邮件发送失败!\n{traceback.print_exc()}')
                return False
        else:
            logger.warning('邮箱未启用，放弃执行')
