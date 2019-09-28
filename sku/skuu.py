from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://cs.skuniv.ac.kr/cs_notice')
# pprint(html.text)

soup = bs(html.text, 'html.parser')

#1페이지 전체 추출
data1_list = soup.findAll('td', {'class':'title'})
#pprint(data1_list[0])
#pprint(data1_list[1])


#1 페이지의 제목만 추출
title_list=[]
for data1 in data1_list:
    title=data1.find('a', {'class':'title'})
    title_list.append(title.text)
    #pprint(title.text)

#pprint(title_list)
#1 페이지의 글쓴이 만 추출
writer_list=[]
for data1 in data1_list:
    title=data1.find('li', {'class':'author'})
    writer_list.append(title.text)
    #pprint(title.text)
#pprint(writer_list)

#1 페이지의 내용 만 추출
content_list=[] 
for data1 in data1_list:
    title=data1.find('p', {'class':'summary'})
    content_list.append(title.text)
    #pprint(title.text)
pprint(content_list)

#pprint(title_list)
#data2=data1.findAll('p', {'class':'title'})
#pprint(data2)
#안에 내용만 추출
#data1=soup.find('div', {'class':'detail_box'})
#pprint(data1)

#data2=data1.findAll('dd');
#pprint(data2)
#pprint(data2[0])

#find_dust=data2[0].find('span', {'class':'num'})
#pprint(find_dust.text)