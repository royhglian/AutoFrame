import os
import time
import logging

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.realpath(cur_path),'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

class logs():
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log'% time.strftime('%Y_%m_%d'))
        self.logname = os.path.join(log_path, '{}.log'.format(time.strftime('%Y_%m_%d')))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 日志输出格式
        self.fromatter = logging.Formatter('[%(asctime)s-%(filename)s]-%(levelname)s:%(message)s')

    def _console(self, level, message):
        # 输出到本地文件夹
        fh = logging.FileHandler(self.logname, 'a', encoding='UTF-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.fromatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.fromatter)
        self.logger.addHandler(ch)

        # 区分日志等级
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'warning':
            self.logger.warning(message)

        # 去重日志
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)