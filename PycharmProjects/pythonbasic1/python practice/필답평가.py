# # 1. "test.txt"라는 파일에 "big data" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램을 작성하시오.
# #
#
# f=open("text.txt","w")
#
# f.write('big data')
# f.close()
#
#
# with open("text.txt", "r") as f:
#     s=f.read()
#     print(s)
#
# # 2. 다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.
#
#
#
# import re
#
# data="""
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
# """
#
# p=re.compile("(\d{3}[-]\d{4})[-]\d{4}")
#
# result=p.sub("\g<1>-####", data)
#
# print(result)
#
#
# # 3. utf-8로 인코딩하기 위한 meta 태그를 적으시오.
#
# # <meta charset="UTF-8">
#
# # 4. 네이버 또는 다음에 실린 신문기사를 스크래핑하는 코드를 작성하시오. (신문사 및 카테고리는 자유롭게 선택 가능, 1page만)

from selenium import webdriver
from bs4 import BeautifulSoup
driver=webdriver.Chrome('/Users/junmishin/chromedriver')


url="https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&oid=092&aid=0002211790"
driver.get(url)
from bs4 import BeautifulSoup
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

content = soup.find(id="articleBodyContents")
print(content)


# # import requests
# # from bs4 import BeautifulSoup
# # from urllib.parse import urljoin
# # url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=009&aid=0004738856'
# # req_header = {
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# # }
# # res = requests.get(url, headers=req_header)
# # print(res.status_code)
# # html = res.text
# # soup = BeautifulSoup(html, 'html.parser')
# #
# # content = soup.find(id="articleBodyContents")
# # print(content)
#


