# -*- coding: UTF-8 -*-
import time
import hashlib
import functools

import flask

def response_format(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        """
        格式化处理接口返回数据，code为0判断为成功
        """
        res = f(*args, **kwargs)
        if len(res) < 3:
            return res
        
        log_id = 0
        status_code = 200
        if len(res) == 3:
            code, info, data_code = res
            if data_code >= 1000:
                log_id = data_code
            else:
                status_code = data_code
        elif len(res) == 4:
            code, info, status_code, log_id = res
        else:
            return res
        if code == 0:
            msg = 'success'
            data = info
        elif code == 200:
            msg = str(info)
            data = info
            code = 0
        else:
            msg = info
            data = None
        response = {
            'status': code,
            'msg': msg,
            'data': data,
            'log_id': str(log_id)
        }
        return response, status_code
    return decorated