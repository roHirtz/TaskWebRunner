# -*- coding: utf-8 -*-

import pytest
import os
import sys
sys.path.append(os.getcwd())


def pytest_configure(config):
    """
        最先调用，用于配置环境
    """
    from datetime import datetime
    from src.utils.environment import Environment
    Environment.set_environemt('start_time', datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
        每次执行收集结果
    """
    from src.utils.pyselenium import PySelenium
    from src.utils.mail import Mail
    report = yield
    report = report.get_result()
    if report.when == 'call':
        if report.outcome == 'failed':
            PySelenium().save_screenshot('./report/failed.png')
            Mail().send_mail('自动化测试失败截图',
                             f'{report.nodeid} - 执行失败截图',
                             './report/failed.png')


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
        执行完成后生成测试报告摘要
    """
    from src.utils.report import Report
    from src.utils.mail import Mail
    from src.utils.pyjenkins import Pyjenkins
    from src.utils.pydingtalk import PyDingTalk

    passed, failed, skipped = Report.get_report_summary(terminalreporter)
    url, report = Pyjenkins().get_msg()
    subject = Report.get_report_subject()
    content = Report.get_report_content(passed, skipped, failed, url, report)

    Mail().send_mail(subject, content)
    PyDingTalk().send_text_msg(content)


@pytest.fixture(params=[['hotshot0', '123456', 'A1B2']])
def login(request):
    from src.utils.tagFunc import login
    return login(request)
