import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEST_DATA = os.path.join(BASE_DIR, 'test_data/test_cases.xlsx')

PROJECT_URL = 'http://10.00.5.74:00000'

INTERFACE = {
    'login': '/api/v1/login',
    'query': '/api/v1/approve/query?page=1&size=4294967295'
}

# 数据库配置
DB_CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'mysql',
    'port': 3306,
    'autocommit': False
}

# 输出日志
LOG_CONFIG = {
    'name': 'DPO',
    'filename': os.path.join(BASE_DIR, 'logs/dpo.txt'),
    'debug': True,
    'mode': 'w',
    'fmt': None,
    'encoding': 'utf-8'
}

# 报告
REPORTS_CONFIG = {
    'filename': 'do接口自动化',
    'report_dir': os.path.join(BASE_DIR, 'reports'),
    'theme': 'theme_default',
    'description': 'DO',
    'title': 'DO1期',
    '_type': 'br'
}

USER_LOGIN = {
    'username': 'username',
    'password': 'password'
}
