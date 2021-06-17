#동적으로 html 파일을 불러오는 웹 사이트와 \
#정적으로 html 파일을 불러오는 웹 사이트간 \
크롤링 방법의 차이로 인해 겪었던 문제점과 \
그 해결 방법을 기록해 놓기 위한 repository 입니다. 


####################################### \
#정적으로 html 파일을 불러오는 웹 사이트의 경우 # \
#######################################

단순 beautifulSoup 패키지를 사용하여 parsing 하여도 데이터를 모아 오는 것에 문제가 없었음.

######################################## \
#동적으로 html 파일을 불러오는 웹 사이트의 경우 # \
######################################## 

beautifulSoup 패키지만으로는 한계가 생겼음 

#Solution1)---------------------------------------------------- 

time.sleep을 이용해 로딩이 다 될때 까지 기다린 다음 크롤링 시도. 

결과 : 여전히 빈 컨테이너만 로딩 됨.

반응 : 비동기 작업처럼 단순 스케쥴링 타이밍 문제가 아님을 깨달음.



#Solution2)----------------------------------------------------

"크롤링시 빈 컨테이너" 라는 키워드로 구글링을 진행하던 중, Selenium이란 프레임워크를 발견했다.

크롤링이 정보를 습득하는 기술이긴 하지만, 반대로 정보를 주는 것을 막고자 하는 경우들도 있다.

User가 아니면서 정보를 습득하려는 행위 자체를 막으려는 경우를 의미한다.

Selenium은 그런 경우를 위해서 '사용'되는 기술이다.

Selenium이 크롤링을 위한 기술은 아니다.

기본적으로 어느 페이지의 어느 버튼을 누르고, 또 태그를 입력했을 때 원하는 결과가 나오는지,

그런 다양한 웹 페이지와 사용자 간의 상호작용을 하나 씩 해보면서 테스트를 해야 했었다.

이런 비효율을 해결하기 위해서, 원격으로, code를 활용하여 웹 페이지를 테스트하기 위한 기술이 selenium이었다.

결과 : 너무 잦은 재접속와 자동화로 인해 여전히 데이터 접근이 block되는 경우가 생김.

반응 : "너무 잦은" 이 원인이라면 빈도를 줄이기 위해 time.sleep을 이용함. 
       그 이후 원하는 결과를 잘 얻을 수 있었음. 
       
      



