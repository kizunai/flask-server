import flask
from flask_restful import Resource

from utils import decoraters
from logic.test.checkalive_logic import CheckaliveLogic

class CheckaliveApi(Resource):
    """CheckaliveApi
    /api/checkalive
    """

    def __init__(self):
        self.log_id = 1 #todo 暂时用1代替

    @decoraters.response_format
    def get(self):
        """
        """
        checkalive_logic = CheckaliveLogic()
        res, err = checkalive_logic.checkalive()
        if err:
            return 1, err, self.log_id
        return 0, res, self.log_id
