import requests

class CheckaliveLogic(object):
    """
    CheckaliveLogic
    """
    def __init__(self, logger = None):
        self.logger = logger
    
    def checkalive(self):
        return "it's ok!", None