# -*- coding: utf-8 -*-

from src.utils.environment import Environment


class Report:

    @staticmethod
    def get_report_summary(terminalreporter):
        """
            获取pytest的结果
        """
        passed, failed, skipped = [], [], []
        for status, reports in terminalreporter.stats.items():
            if status == "passed":
                for report in reports:
                    nodeid = report.nodeid
                    passed.append({nodeid: ""})
            elif status == 'failed':
                for report in reports:
                    nodeid = report.nodeid
                    reason = report.longreprtext
                    failed.append({nodeid: reason})
            elif status == 'skipped':
                for report in reports:
                    nodeid = report.nodeid
                    reason = report.longreprtext
                    skipped.append({nodeid: reason})

        return passed, failed, skipped

    @staticmethod
    def get_report_subject():
        return f'自动化API测试报告{Environment.get_environment("start_time")}'

    @staticmethod
    def get_report_content(passed, skipped, failed):
        """
            获取测试报告结果内容
        """
        content = f'测试结果如下:\n测试通过用例：【{len(passed)}】个用例通过\n'
        for item in passed:
            for k, v in item.items():
                content = content + k + '   -   ' + '\n'

        content = content + f'\n测试跳过用例：【{len(skipped)}】个用例跳过\n'
        for item in skipped:
            for k, v in item.items():
                content = content + k + '   -   ' + v + '\n\n ************************************************** \n\n'

        content = content + f'\n测试失败用例：【{len(failed)}】个用例失败\n'
        for item in failed:
            for k, v in item.items():
                content = content + k + '   -   ' + v + '\n\n ************************************************** \n\n'

        return content
