# 测试入口
import settings
import unittest
from common.reports_handler import reports

ts = unittest.TestLoader().discover('test_cases')
runner = reports(ts, **settings.REPORTS_CONFIG)

if __name__ == '__main__':
    unittest.main()
