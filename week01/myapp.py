import os
import logging
import mylib
from datetime import datetime


logger = logging.getLogger(__name__)


class LoggerConfig:
    """ 初始化日志配置 """
    def __init__(self):
        self.log_fname = 'example.log'
        self.base_dir = os.path.join(os.getcwd(), 'var', 'log')
        self.init_config()

    def init_config(self):
        logging.basicConfig(
            filename=self.get_log_fp(),
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def get_log_fp(self):
        """ 获取日志文件路径 """
        current_day = datetime.now().strftime('%Y-%m-%d')
        log_dir = os.path.join(self.base_dir, f'python-{current_day}')

        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)

        return os.path.join(log_dir, self.log_fname)


def main():
    """ 主函数 """
    logger.info('do something start ...')
    try:
        0 / 0
    except Exception as e:
        logger.error(f'got error: {e}')

    mylib.do_something()
    logger.info('do something end ...')


if __name__ == '__main__':
    LoggerConfig()  # 初始化日志配置
    main()
