from selenium import webdriver
#selenium을 구동하기 위한 webdriver를 가져옴.
#webdriver는 사용하는 것들이 다르지만 주로 chrome을 사용한다고 함.
#따로 다운로드를 받아 줘야 하는 외부 프로그램임.
from bs4 import BeautifulSoup
##server에서 받은 html file을 우리가 아는 html 태그 형태로 보여주기 위한 패키지.

import time



pageNum = 0
searchPagenum = 10
################################
#       File Save Field        #
outputFileName = "Output_file_Name"
textFile = open(f'{outputFileName}.txt','w',encoding='UTF-8')
################################

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#그냥 드라이버만 사용시, runtime error가 발생하여 추가한 options.
driver = webdriver.Chrome("Input chrome driver's absolute location",options=options)
count = 0


#페이지를 넘겨가기 위한 부분
while(pageNum != searchPagenum+1) :
    driver.get('https://website/biz?page='+str(pageNum))
    time.sleep(3)
    print(pageNum)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    tank = soup.select("Input tag inheritance stack")
    #select는 연관된 모든 tag를 parsing

    for data in tank:
        #select된 데이터들은 list의 형태로 저장되기에 for문을 사용하여 간편히 parsing
        temp = data.select_one("Input target tag inheritance stack")

        #file에 저장
        textFile.write(temp)
    pageNum +=1



driver.close()
textFile.close()
