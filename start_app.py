# -*- coding: UTF-8 -*-
"""
gunicorn的配置文件
"""
import gevent.monkey
import multiprocessing
import os

from config.app_config import ServerConfig

path_of_current_file = os.path.abspath(__file__)
path_of_current_dir = os.path.split(path_of_current_file)[0]

_file_name = os.path.basename(__file__)

# gevent 在有些Linux环境执行报错
#gevent.monkey.patch_all()
debug = False
loglevel = 'info'
bind = '{}:{}'.format(ServerConfig.Host, ServerConfig.Port)
pidfile = '%s/logs/gunicorn.pid' % (path_of_current_dir,)
errorlog = '%s/logs/info.logs' % (path_of_current_dir,)
accesslog = '%s/logs/access.logs' % (path_of_current_dir,)
# 启动进程数
workers = multiprocessing.cpu_count()*2 + 1
timeout = 36000
preload_app = False
daemon = True
x_forwarded_for_head = 'X-FORWARDED_FOR'