import requests
#html file을 server에서 request하기 위한 패키지.
from bs4 import BeautifulSoup
#server에서 받은 html file을 우리가 아는 html 태그 형태로 보여주기 위한 패키지.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#html header
data = requests.get('https://imnews.imbc.com/news/2021/politics/',headers=headers)
#website의 html data field.

soup = BeautifulSoup(data.text, 'html.parser')
#html file을 우리가 아는 html 태그 형태로 parsing.



################################
#       File Save Field        #
outputFileName = "Output_file_Name"
textFile = open(f'{outputFileName}.txt','w',encoding='UTF-8')
################################



tank = soup.select("Input tag inheritance stack")
#select는 연관된 모든 tag를 parsing

for data in tank:
    #select된 데이터들은 list의 형태로 저장되기에 for문을 사용하여 간편히 parsing
    temp = data.select_one("Input target tag inheritance stack")

    #file에 저장
    textFile.write(temp)

#페이지 넘기면서 크롤링 하기

pageNum = 0
searchPagenum = 10

while(pageNum != searchPagenum+1) :
    url = f'https://news.joins.com/money?page={pageNum}'
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    tank = soup.select("Input tag inheritance stack")
    for data in tank:
        #select된 데이터들은 list의 형태로 저장되기에 for문을 사용하여 간편히 parsing
        temp = data.select_one("Input target tag inheritance stack")

        #file에 저장
        textFile.write(temp)
        
    pageNum += 1




textFile.close()

