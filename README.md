本接口自动化框架采用 Python + unittest + request + openpyxl + myddt + pymysql 来实现接口自动化。

测试报告生成模块：BeautifulReport
网络请求模块：requests
数据库模块：
    mysql：pymysql

使用环境需要下载的 Python 库：
    pip install BeautifulReport
        执行 main.py 后，如果出现 ModuleNotFoundError: No module named 'distutils'
        (由于 Python 3.12 之后废弃了 distutils)
        请安装：pip install setuptools
    pip install requests
    pip install pymysql


启动方法：控制台进去根目录输入 python main.py
