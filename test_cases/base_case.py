# 测试基类
import unittest
from common import logger
import requests

class Basic_test_case(unittest.TestCase):

    name = '基类'
    logger = logger
    requests = requests
    session = requests.session()
