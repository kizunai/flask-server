# -*- coding: UTF-8 -*-
"""
创建flask app， 注册api信息
"""

import os
import atexit
import threading

import flask
from flask import Flask
from flask import app
from flask_restful import Api
from flask_cors import CORS

from config.app_config import AppName

from api.test.checkalive_api import CheckaliveApi


base_path = os.path.dirname(os.path.abspath(__file__))

def create_app():
    """创建app

    :return:
    """
    init_log_folder()
    app = Flask(AppName)
    #app.config.from_object()
    apis = Api(app=app)
    register_api(apis)
    
    @app.before_request
    def setup():
        """
        flask前置操作
        """
        path = flask.request.path
        method = flask.request.method

    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        """
        pass

    # app退出时操作
    atexit.register(teardown)

    return app
        

def init_log_folder():
    """
    初始化日志
    """
    log_path = os.path.join(base_path, 'logs')
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    return

def register_extensions(app):
    pass

def register_api(apis):
    """
    注册接口
    """
    apis.add_resource(CheckaliveApi, "/api/checkalive")
    
def register_celery():
    """注册celery消息队列
    """
    pass

def teardown():
    """app退出时断开连接
    """
    pass