# 封装输出日志
import logging

def get_logger(name, filename, debug=False, fmt=None, mode='w', encoding='utf-8'):

    logger = logging.getLogger(name=name)
    logger.setLevel(level=logging.DEBUG)

    if debug:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO

    if fmt is None:
        #fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s'
        fmt = '%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s'

    format = logging.Formatter(fmt)
    file_handle = logging.FileHandler(filename=filename, mode=mode, encoding=encoding)
    file_handle.setLevel(level=file_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=console_level)

    file_handle.setFormatter(format)
    console_handler.setFormatter(format)

    logger.addHandler(file_handle)
    logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    logger = get_logger(name='do', filename='../logs/do.txt', debug=False, mode='a')
    logger.debug(10)
    logger.info(20)
    logger.warning(30)
    logger.error(40)
    logger.critical(50)
