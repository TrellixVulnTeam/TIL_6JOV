# # # re.sub("패턴","바꿀문자열",'문자열',바꿀횟수)
# # # import re
# # #
# # # print(re.sub("apple|orange","fruit","apple tree banana orange"))
# # #
# # #
# # # print(re.sub("[0-9]+","num","1 2 apple 3 banana 4 7 9 30 tree"))
# # #
# # # print(re.sub("apple|orange","fruit","apple tree banana orange",1))
# # #
# # # print(re.sub("apple|orange","fruit","apple tree banana orange"))
# # #
# # # pat=re.compile("apple|orage")
# # # pat.sub("fruit","apple tree banana orange")
# #
# #
# #앞부분 강사님 필기

# ## # sub함수
# # #
# # #
# # # 대한민국, 한국, 코리아 ... => 대한민국
# #
# # # import re
# # # if re.match("\d{4}$","12345"):
# # #     print("정상 전화번호")
# # # else :
# # #     print("비정상 전화번호")
# # #
# # #
# # # #re.sub("패턴","바꿀문자열", "문자열",바꿀횟수)
# # # print(re.sub("apple|orange", "fruit","apple tree banana orange"))
# # #
# # # # "1 2 apple 3 banana 4 7 9 30 tree"
# # # # 수치데이터 => "num"으로 변경
# # # print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree",1))
# # #
# # # print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree",3))
# # #
# # #
# # # # print(re.sub("apple|orange", "fruit","apple tree banana orange",1))
# # # # print(re.sub("apple|orange", "fruit","apple tree banana orange",count=1))
# # #
# # #
# # # print(re.sub("apple|orange", "fruit","apple tree banana orange"))
# # # print("="*50)
# # # pat=re.compile("apple|orange")
# # # print(pat.sub("fruit","apple tree banana orange",1))
# #
# # #[0-9]:\d, 공백/탭/엔터문자:\s, 문자/숫자:\w
# #
# # #https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png
# #
# #
# # import urllib.request
# # # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # # urllib.request.urlretrieve(url, "test.png")
# # # print("저장되었습니다")
# #
# # import ssl
# #
# # #context = ssl._create_unverified_context() #mac
# #
# # # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # # mem=urllib.request.urlopen(url).read()
# # # #mem=urllib.request.urlopen(url, context=context).read() #mac
# # #
# # # with open("test2.png", "wb") as f:
# # #     f.write(mem)
# # #     print("저장되었습니다")
# #
# #
# # # http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
# # #
# # # 웹에서 사용하는 언어
# # # -서버와 클라이언트 간에 데이터를 주고 받을 때 사용하는 언어(HTML)
# # # 클라이언트(페이지 요청, 웹브라우저에 www.naver.com) -> 웹서버 -> 메인페이지 제공(index.html)->
# # #
# # # HTML: HyperText Markup Language
# # # XML : Extensible Markup Language
# #
# # # jsp, asp, php 등 : 동적 페이지
# # # 구조화된 문서(xml):정적 페이지
# # # 비구조화된 문서(html):정적 페이지
# # #
# # # 클라이언트(날씨 클릭)-> 웹서버(날씨 페이지(동적,jsp) 생성) -> 생성된 페이지를 html문서로 만들어 제공
# # # -> 웹브라우저 해석 -> 결과를 화면에 출력
# # #
# # # 출력 : 오늘의 날씨는 맑습니다. 기온은 섭씨 영상 2도입니다
# # #
# # # 정적페이지
# #
# # # 검색어 : 노래 제목, 멤버들, ...
# # #
# # # 비구조화된 문서 : 웹페이지 내용에 대해 기계가 해석하지 못하는 문서->검색어를 기반으로 검색
# # # EX) BTS가 서울 강남구에서 공연을 했습니다.
# # #
# # # 구조화된 문서 : 웹페이지 내용에 대해 기계가 해석 가능한 문서->검색어의 의미를 기반으로 검색
# # # =>검색 폭 넓음, 검색 결과에 대한 정확도 높음
# # # <가수>
# # #     <그룹명>BTS</그룹명>
# # #     <도시이름>서울</도시명>
# # #     <구이름>강남구</구이름>
# # #     <멤버이름>.....</멤버이름>
# # # </가수>
# #
# # import urllib.parse as parse
# # import urllib.request as request
# # addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# # values={'stdId':'109'}
# #
# # params=parse.urlencode(values)
# # url=addr+"?"+params
# # print(url)
# #
# # data=request.urlopen(url).read()
# # data=data.decode('utf-8')
# # print(data)
#
# #제주시의 1월16일 자정 온도
#
# #웹스크래핑 :BeautifulSoup패키지
# # # import urllib.request
# # # import ssl
# # # #
# # # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # #
# # # mem=urllib.request.urlopen(url,context=context).read()
# # # with open("test2.png","wb") as f:
# # #     f.write(mem)
# # #     print("저장되었습니")
# #
# #
# #
# # # import urllib.request
# # #
# # # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # # urllib.request.urlretrieve(url,"test.png")
# # # print("저장되었습니다")
# # #
# # #
# # # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # #
# # # mem=urllib.request.urlopen(url).read()
# # # with open("test2.png","wb") as f:
# # #     f.write(mem)
# # #     print("저장되었습니")
# #
# #
# # # http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
# #
# # # XML : Extensible Markup Language
# # # -서버와 클라이언트 간에 데이터를 주고 받을 때 사용하는 언어(HTML)
# #
# #
# #
# #
# # # 구조화된 문서(XML):정적 페이지
# # # 비구조화된 문서 (html):정적 페이지
# #
# # # 클라이언드(날씨 클릭)->웹서버(날씨 페이지(동적)생성)->생성된 페이지를 HTML문서로 만들어 제공
# # # ->웹브라우저 해석->결과를 화면에 출력
# #
# # # 출력 : 오늘의 날씨는 맑습니다. 기온은 섭씨 영상 2도입니다
# # # 정적페이지
# #
# #
# #
# # #검색어: 노래 제목, 멤버들,....
# # # 비구조화된 문서: 웹페이지 내용에 대해 기계가 해석하지 못하는 문서색->검색어를 기반으로 검색을 해준
# # # bts가 서울 강남구에서 공연을 했습니다.
# # # 구조화된 문서: 웹페이지 내용에 대해 기계까 해석 가능한 문서-->의미를 기반으로 검색
# # # ->검색 폭 넓음, 검색 결과에 대한 정확도 높
# #
# # # <가수>
# # # <그룹>/BTS</그룹명>
# # # <도시이름>서울</도시명>
# # # <구이름>강남구</구이름>
# # # <멤버이름>...</멤버이름>
# # # </가수>
# #
# #
# #
# import ssl
# #
# # import urllib.parse as parse
# # import urllib.request as request
# # addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# # values={'stdId':'109'}
# # params=parse.urlencode(values)
# #
# # url=addr+"?"+params
# #
# # print(url)
# # context=ssl._create_unverified_context()
# # data=request.urlopen(url,context=context).read()
# # data=data.decode('utf-8')
# # print(data)
# #
# # # 제주시의 1월 16일 자정 온도
# #
# # # 웹스크래핑:BeautifulSoup패키지
#
# from bs4 import BeautifulSoup
#
# # html="""
# # <html>
# # <body>
# # <h1>스크래핑</h1>
# # <p>웹 페이지 분석</p>
# # <p>원하는 부분 추출</p>
# # </body>
# # </html>
# # """
# # soup=BeautifulSoup(html,"html.parser")
# #
# # print(soup.html.body.h1.string) #.string하면 태그 내용이 빠지고 문자열만 추출
# # p1=soup.html.body.p
# # # p2=p1.next_sibling#줄바꿈 문자(p1다음은 엔터문자가 왔기때문에)
# # # print(p2.next_sibling.string)
# # # print(soup.html.body.p.string)
# # # 위에 두 줄을 한줄로 표현하면
# # p2=p1.next_sibling.next_sibling.string
# # print(p2)
#
#
# html2="""
# <html>
# <body>
# <h1 id='title'>스크래핑</h1>
# <p id='body'>웹 페이지 분석</p>
# <p>원하는 부분 추출</p>
# </body>
# </html>
# """
#
# soup=BeautifulSoup(html2,"html.parser")
# # print(soup.html.body.h1.string)
# print(soup.find(id='title').string)
# print(soup.find(id='body').string)
#
#
# #raw text
# html3="""
# <html><body>
# <ul>
# <li><a href="http://www.naver.com">naver</a><li>
# <li><a href="http://www.daum.net">daum</a><li>
# </ul>
# </body></html>
# """
#
# soup=BeautifulSoup(html3,"html.parser")
# print(soup) #문자열->html파서로 분석할 수 있는 객체로 변
# print(html3) #문자열을 저장하고 있는 변수에 불과
#
# # <태그명 속성명= 속성값 속성명=속성값...>
#
#
# # print(soup.find_all("a")) #리스트로 변환됨
# # print(html3.find_all("a")) #findal은 문자열(html3)에 적용할 수 있는 함수가 아님
#
# links=soup.find_all("a")
# # print(links[0]) #naver
# # print(links[1]) #daum
#
# for i in links:
#     href=i.attrs['href']  #특정 속성 참조
#     na=i.string
#     print(na,"-->",href)
#
#
# print("="*50)
#
# html4="""
# <p><a href="aaa.html" name="kkk">aaa page</a></p>
# """
# soup=BeautifulSoup(html4,"html.parser")
# print(soup.p.a.string)
# print(soup.a) #굳이 차례 p태그부터 접근하지 않아도 됨로 #만약 a태그가 여래개 있는 경우는 명시를 해주어야함
# print(soup.a.attrs) #중요!! 속성과 값이 딕셔너리 형태로 출력됨
# mydict=soup.a.attrs
#
#
# #mydict에서 찾고자하는 이름의 키가 존재하는지 알고싶을 때
# print('href' in mydict)
# # if 'href' in mydict:
# #     ..
# # else:
# #     ..
# # mydict=soup.a.attrs
# # print(mydict.values())
#
#
# # dic=soup.a.attrs
# # print(dic)
# # print(dic.values())
# # print(list(dic.values()))
#
# # 또는
# # soup.a.attrs.get('href')
# # 또
# # for i in soup.find_all("a"):
# #
# #     href=i.attrs["href"]
# #
# #     name=i.attrs["name"]
# #
# # print(i.string,"-->","href:",href,"name:",name)
#
#
# print("="*50)
# #웹스크래핑
#
#
# import ssl
#
# import urllib.request as req
#
# url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# context=ssl._create_unverified_context()
# res=req.urlopen(url,context=context) #페이지 내용이 담겨있는 포장지(봉투)
# print(res)
#
# soup=BeautifulSoup(res,"html.parser") #웹에서 가져온 문서의 경우 문서가 담겨있는 봉투를 통으로
# # print(type(soup))
# print("문서 제목:",soup.title.string) #처음의 title만 찾
# #또는
# print(soup.find("title").string) #처음의 타이틀만 찾
# #또는
# print(soup.find_all("title")) #title에 해당하는 것을 모두 출력해 리스트로 반음
# print(soup.find_all("title")[0].string)
# # 정상응담=>200:ok
# # 문서를 찾지 못한경우=>40으로 시작하는 수로 응답
# # 서버 자체 오류=>50으로 시작되는 오류 응답
# #
# # print(soup.find("wf").string)
# # print(len(soup.find_all("wf"))) #결과가 리스트라서 len함수 쓸 수 있음
#
#
#
# #select함수
#
from bs4 import BeautifulSoup
#
# # html = """
# # <html><body>
# # <div id="lang">
# #     <h1>프로그래밍언어</h1>
# #     <ul class="items">
# #         <li>python</li>
# #         <li>java</li>
# #         <li>cpp</li>
# #     </ul>
# # </div>
# # </body></html>
# # """
# # h1은 주로 제목을 나타낼 때 씀
# #ul -->unordered의 약자로 순서가 없는 목록을 만드는 태그임
# #ol->ordered list 앞에 순서가 붙음
#
html4 = """
<html><body>
<div id="lang">
    <h1>programming</h1>  
    <ul class="items">
        <li>python</li>
        <li>java</li>
        <li>cpp</li>
    </ul>
</div>
</body></html>
"""

#
#
# # #div,class, !!select함수!!
soup=BeautifulSoup(html4,"html.parser")
# # # print(soup.select("div"))  #리스트로 변환됨
# # print(soup.select("div#lang>h1")[0])  #lang이라는 id를 가지고 있는 dic태그만 나옴
# # #리스트로 나오기때문에 [0]주면 []없어지고 문자열만 반환됨
# # #셀렉트는 같은 태그가 여러개 있고 그 여러개의 태그를 추출할 때
# #
# # #select_one
# # print(soup.select_one("div#lang>h1").string)
# # #select one은 리스트가 아니라 문자열 그대로 나와버림
# # #select_one은 한개를 추출함
#
#
# #select함수를 사용할 때 클래스 사용방법
# # print(soup.select("div#lang > ul.items >li")) #리스트로 나오고 li태그로 묶여 있는 것이 다 나
# # print(soup.select_one("div#lang >ul"))옴
# # print(soup.select_one("div#lang > ul.items >li")) #리스트에 있는 값 하나만 나옴
#
#
#

mylist=soup.select("div#lang>ul.items>li")
for i in mylist:
    print(i.string)