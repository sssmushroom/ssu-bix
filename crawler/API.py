from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from crawler import Crawler

from fun_parser import PARSER_DATE as FUN_DATE_PARSER
from fun_parser import PARSER_APPROACH as FUN_APPROACH_PARSER
from fun_parser import PARSER_APPLICANT as FUN_APPLICANT_PARSER

from cse_parser import PARSER as CSE_PARSER

app = Flask(__name__)
api = Api(app)

class FunDateGET(Resource):
    def get(self):
        it = Crawler(FUN_DATE_PARSER)
        return it.parse()

class FunApproachGET(Resource):
    def get(self):
        it = Crawler(FUN_APPROACH_PARSER)
        return it.parse()

class FunApplicantGET(Resource):
    def get(self):
        it = Crawler(FUN_APPLICANT_PARSER)
        return it.parse()

class CSENoticeGET(Resource):
    def get(self):
        it = Crawler(CSE_PARSER)
        return it.parse()

api.add_resource(FunApproachGET, '/fun/approach')
api.add_resource(FunApplicantGET, '/fun/applicant')
api.add_resource(FunDateGET, '/fun/date')
api.add_resource(CSENoticeGET, '/cse/notice')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)
