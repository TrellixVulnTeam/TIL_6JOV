#id를 이용한 다양한 데이터 참조 방법

from bs4 import BeautifulSoup

# fp=open("lang.html",mode="r",encoding="utf-8")
# soup=BeautifulSoup(fp,"html.parser")
# print(soup)
# print("="*30)
# print(soup.select_one("ul>li")) #요건을 만족하고 처음에 나오는 데이터만 추
# print("-"*30)
# print(soup.select("ul>li")) #출요건을 만족하는 전체가 리스트로 모든 형태 나옴
#
# print("="*30)
#
# #python부분만 출력하고 싶을 때
#
# print(soup.select_one("ul>li#py")) #id줄때는 # 뒤에 id명
# print(soup.select_one("ul>li#py")) #선택자(selector)
# #ul은 하나밖에 없기때문에 생략해도 무관함!!
# print(soup.select_one("li#py"))
# #심지어는 id도 각각 다르기 때문에 li태그도 빼도 ok
# print(soup.select_one("li#py"))
#
#
# print("="*30)
# #조금 더 어려운 ver or 비효율....
# print(soup.select_one("ul#language")) #ul태그에 id명 줘도 됨
#
# print(soup.select_one("ul#language>li#py"))
#
#
# #another ver...
# print(soup.select_one("#language"))
# print(soup.select_one("#language >#py"))
# print(soup.select_one("#language #py"))
# print(soup.select_one("li[id='py']"))
#
#
# print("="*30)
#
# print(soup.select_one("li:nth-of-type(2)")) #type안에 리스트의 위치 줘서 참조해도 됨
#
# print(soup.select("li")[2])
# print(soup.find_all("li")[2])
# print(soup.find_all("li"))


#네이버 달러 환율 정보 가져오기

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)
from bs4 import BeautifulSoup
fp=open("lang.html", mode="r", encoding="utf-8")
soup=BeautifulSoup(fp, "html.parser")
print(soup)
print("="*50)
print(soup.select_one("ul > li"))
print(soup.select_one("ul > li#py")) #id 가 py인 데이터 추출
print(soup.select_one("li#py")) #선택자 (selector)
print(soup.select_one("#py"))
print("="*50)
print(soup.select_one("ul#language > li#py"))
print(soup.select_one("#language > #py"))
print(soup.select_one("#language #py"))
print(soup.select_one("li[id='py']"))
print("="*50)
print(soup.select_one("li:nth-of-type(3)"))

print(soup.select("li")[2].string)
print(soup.find_all("li")[2])



print("-"*50)
print(soup.select("ul > li")) #리스트

import urllib.request as req

#네이버 달러 환율 정보 가져오기
url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
#res=req.urlopen(url) #한글깨짐
res=req.urlopen(url).read().decode('euc-kr')
print(res)

soup=BeautifulSoup(res, "html.parser")
#print(soup)

print("달러당",soup.select("a.head.usd > div > span.value")[0].string+"원")

print("달러당",soup.select("#exchangeList > li.on > a.head.usd > div > span.value")[0].string)
print("달러당",soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string)

print("금값",soup.select_one("#oilGoldList > li.on > a.head.wti > div > span.value"))
print("기사",soup.select_one("#content > div.section_news > div > ul > li:nth-child(1) > p > a"))



import urllib.request as req
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
# print(soup.select_one("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a").string)


mylist=soup.select("#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul >li")
for li in mylist:
    print(li.string)

print(len(mylist))
#
# fp=open("fruits-vegetables.html", encoding="utf-8")
# soup=BeautifulSoup(fp, "html.parser")
# print(soup.select("div"))
# print("="*50)
# # dic={"data-lo":"us"} #{속성명:속성값,...}
# # print(soup.find("li", dic))
#
# dic={"data-lo":"us", "class":"black"}
# # print(soup.find("li", dic))
#
# print(soup.find(id="ve-list").find("li", dic))
#
#
# print(soup.findAll("li", dic))
# print(soup.findAll("li"))#find함수==select_one함수, findAll==select함수






# print("="*50)
# print(soup.select("#ve-list > li[data-lo='us']")[1])
# print(soup.select("#ve-list > li.black")[1])
# print(soup.select("#ve-list > li:nth-of-type(4)")[0].string)
# print(soup.select("li.black")[1].string)
# print(soup.select("li.black")[1])
# print(soup.select("li.black"))
# print(soup.select("li"))
# print(soup.select("div > ul"))
# print("="*50)
# print(soup.select("div > ul#fr-list"))
# print(soup.select("#fr-list"))
#
# Selenium : 웹 브라우저를 제어하는 프로그램 #pip install selenium
#
# 크롬드라이버를 다운로드 받아서 #c:\scrap\파일복사
#
# chromedriver는 크롬 웹브라우저를 제어하는 프로그램
#
# from selenium import webdriver
# driver=webdriver.Chrome("c:/scrap/chromedriver.exe")
# url="https://www.naver.com"
# driver.get(url)
# html=driver.page_source
# print(html)

# #멜론 실시간 인기 차트 곡 수집
# url="https://www.melon.com/chart/index.htm"
# driver.get(url)
# html=driver.page_source
# #print(html)
# soup=BeautifulSoup(html, "html.parser")
# #print(soup)
# songs=soup.select("tr")[1:]
# #print(len(songs))
# song=songs[2]
#
# title=song.select("a")
# print(title)
#
# print("="*50)
# for song in songs:
#     print("곡 명 :",song.select("div.ellipsis.rank01 > span > a")[0].string)
#     print("가수명 : ",song.select("div.ellipsis.rank02 > span > a")[0].string)
#     print("="*50)


# 내일 : 인스타그램 크롤링(제주도 맛집)
#
#
# 리뉴얼(구현 보류)
# 네이버 -> 강아지 -> 이미지 탭 주소
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80
# 네이버 -> 고양이 -> 이미지 탭 주소
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4
# baseUrl="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# word=input("검색어를 입력하세요 : ")
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# #num=int(input("개수 입력 : "))
# url=baseUrl+quote_plus(word)
# #print(url)
# html=urlopen(url)
# #print(html)
# soup=BeautifulSoup(html, "html.parser")
# print(soup)
#img=soup.find_all(class_="_img")
#main_pack > section > div._contentRoot.image_wrap > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(3) > div > div.thumb > a > img
#print(img)
#print(len(img))