# -*- coding: UTF-8 -*-
from api.base import create_app

from config import app_config

app = create_app()

if __name__ == "__main__":
    app.run(host=app_config.ServerConfig.Host, port=app_config.ServerConfig.Port, threaded=True, debug=True)