# 初始化 日志，数据库（单例模式：确保只有一个实例存在）
import settings
from common.logs_handler import get_logger

# 日志
logger = get_logger(**settings.LOG_CONFIG)

# 数据库

