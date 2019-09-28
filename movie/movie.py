import requests
from bs4 import BeautifulSoup
from pprint import pprint
from bs4 import BeautifulSoup as bs

html = requests.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date=20190927')
soup = bs(html.text, 'html.parser')
#pprint(soup)
title_list=soup.select('div.info-movie')
#pprint(title_list)
for i in title_list:
    print(i.select_one('a>strong').text.strip())