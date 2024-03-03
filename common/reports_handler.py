import os
from datetime import datetime
from BeautifulReport import BeautifulReport
from common.HTMLTestRunnerNew import HTMLTestRunner

def reports(ts, filename, report_dir, theme='theme_default', title=None, description=None, tester=None, _type='br'):

    time_prefix = datetime.now().strftime('%Y-%m-%d_%H:%M')
    filename = '{}_{}'.format(time_prefix, filename)

    if _type == 'br':
        br = BeautifulReport(ts)
        br.report(description=description, filename=filename, report_dir=report_dir, theme=theme)
    else:
        with open(os.path.join(report_dir, filename), 'wb') as f:
            runner = HTMLTestRunner(f, title=title, description=description, tester=tester)
            runner.run(ts)
