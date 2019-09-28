from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://comic.naver.com/webtoon/weekday.nhn')
# pprint(html.text)

soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'col_inner'})
#pprint(data1)

data2=data1.findAll('a',{'class':'title'})
#pprint(data2)


title_list=[]
for t in data2:
    title_list.append(t.text)

title_list=[t.text for t in data2]

pprint(title_list)
#data1=soup.find('div', {'class':'detail_box'})
#pprint(data1)

#data2=data1.findAll('dd');
#pprint(data2)
#pprint(data2[0])

#find_dust=data2[0].find('span', {'class':'num'})
#pprint(find_dust.text)

html.close()