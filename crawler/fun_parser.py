from bs4 import BeautifulSoup
from flask import jsonify

class FunParser:
    BASE_URL = 'https://fun.ssu.ac.kr'
    TARG_URL = 'https://fun.ssu.ac.kr/ko/program/all/list/all/1'

    SORT_BASE = {
                'date' : '?sort=date',
                'approach' : '?sort=approach',
                'applicant' : '?sort=applicant'
            }

    def __init__(self, sort_base = 'date'):
        self.TARG_URL += self.SORT_BASE[sort_base]

    def parse(self, soup):
        target_form = soup.find('form', id='ModuleEcoProgramListForm').find('ul', recursive=False)
        target_list = target_form.select('li > div > a')

        ret = []

        for item in target_list:
            cur_dict = dict()
            cur_dict['URL'] = self.BASE_URL + item['href'] # URL
            cur_dict['thumbnailImage'] = self.BASE_URL + item.find('div', class_='cover', recursive=False)['style'][21:-2]
            # hardcored string split
            # Original format : "background-image:url(/attachment/view/18748/cover.png);"

            cur_dict['depart'] = item.find('div', class_='department').text.strip()

            content_node = item.find('div', class_='content', recursive=False)
            cur_dict['title'] = content_node.find('b').text

            periods = content_node.find_all('time')
            cur_dict['date'] = periods[0].text + ' ~ ' + periods[1].text

            cur_dict['apply'] = item.find('div', class_='bottom').find('label').text

            ret.append(cur_dict)
        return ret

        #return jsonify(ret)

PARSER_DATE = FunParser('date')
PARSER_APPLICANT = FunParser('applicant')
PARSER_APPROACH = FunParser('approach')
