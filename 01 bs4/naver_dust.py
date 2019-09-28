from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'detail_box'})
#pprint(data1)

data1=soup.find('div', {'class':'detail_box'})
#pprint(data1)

data2=data1.findAll('dd');
#pprint(data2)
#pprint(data2[0])

find_dust=data2[0].find('span', {'class':'num'})
pprint(find_dust.text)