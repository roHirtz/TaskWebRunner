# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
import time
import traceback
import urllib.parse
import requests
from jsonpath import jsonpath
from src.utils.config import Config
from src.utils.logger import logger


class PyDingTalk:
    def __init__(self):
        self.dingtalk_conf = Config().get_dingtalk_conf()
        self.__url = self.__get_url(self.dingtalk_conf['secret'], self.dingtalk_conf['access_token'])

    @staticmethod
    def __get_url(secret, access_token):
        """
            获取请求地址
        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return f'https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={timestamp}&sign={sign}'

    def send_text_msg(self, msg):
        """
            发送文字消息
        """
        if self.dingtalk_conf['active']:
            logger.info('钉钉机器人启动，开始推送！')
            try:
                data = {"msgtype": "text", "text": {"content": msg}}
                resp = requests.post(url=self.__url, json=data)
                if jsonpath(resp.json(), '$.errcode')[0] == 0:
                    print("钉钉消息发送成功！")
                else:
                    print(f"钉钉消息发送失败！\n{resp.text}")
            except:
                traceback.print_exc()
        else:
            logger.warning('钉钉机器人未启用，放弃执行')
