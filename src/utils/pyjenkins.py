# -*- coding: utf-8 -*-

import urllib.parse
import jenkins
from src.utils.config import Config


class Pyjenkins:
    @staticmethod
    def get_msg():
        jenkins_conf = Config().get_jenkins_conf()
        server = jenkins.Jenkins(url=jenkins_conf['url'], username=jenkins_conf['user'],
                                 password=jenkins_conf['password'], timeout=60)
        infos = server.get_job_info(name=jenkins_conf['job_name'], fetch_all_builds=True)
        last_builds_url = urllib.parse.unquote(infos['builds'][0]['url'])
        last_builds_report = last_builds_url + 'allure'

        return last_builds_url, last_builds_report
