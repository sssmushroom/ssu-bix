from bs4 import BeautifulSoup
from flask import jsonify
import re

class CSEParser:
    BASE_URL = 'http://cse.ssu.ac.kr/'
    TARG_URL = 'http://cse.ssu.ac.kr/main/index.htm'

    def parse(self, soup):
        target_div = soup.find('div', id='notice_list')
        target_list = target_div.select('ul > li')

        ret = []

        for item in target_list:
            cur_dict = dict()

            a_node = item.find('a')
            onclick_txt = a_node['onclick']
            onclick_split = re.split(',|\(|\)', onclick_txt)
            no = onclick_split[1]
            url = onclick_split[2][4:-1]
            opt = onclick_split[3][1:-1]

            # original format of onclick
            # onclick="viewContents(4224,'../03_sub/01_sub.htm','&bbs_cmd=view&page=1&key=&keyfield=&bbs_code=Ti_BBS_1');return false;"
            
            cur_dict['URL'] = self.BASE_URL + url + '?no=' + no + opt

            cur_dict['title'] = a_node.text
            cur_dict['date'] = item.find('span', class_='list_date').text

            ret.append(cur_dict)
        return ret

PARSER = CSEParser()
