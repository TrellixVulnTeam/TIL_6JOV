
# 1. 다나와 -> 노트북 검색 결과
from urllib.request import urlopen

import re

# from selenium import webdriver
#
# driver = webdriver.Chrome('/Users/junmishin/chromedriver')
# #
# url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
#
# driver.get(url)
#
# from bs4 import BeautifulSoup
#
# html = driver.page_source
#
# soup = BeautifulSoup(html, 'html.parser')
# # 1) 노트북 모델명(굵은 글씨)
# # print(soup)
# name = soup.select('#productItem9781572 > div > div.prod_info > p > a')
# for i in name:
#     print(i.string)



#
# 2. 1번 문제를 다 해결했다면,
# 1~10페이지까지 노트북에 대한 정보를 추출
#
# for i in range(10000):
# "http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page="+i+"&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77818&defaultVaTab=9995915&tab=goods"
# http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page=2&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77818&defaultVaTab=9995915&tab=goods
# http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page=3&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77818&defaultVaTab=9995915&tab=goods
#
#
# 3. 보배드림 -> 차량정보추출
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K
# 1)연식
# 2)연료
# 3)가격
#
# 4. https://www.rottentomatoes.com/ => popular streaming movies
# 순위와 함께 영화 제목 추출(밑에 테이블 popular straming movie)




print("="*50)

#다른 분 풀이
#
#
#
# #1. 다나와 사이트 노트북 검색결과
# ###공통 작업###
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('/Users/junmishin/chromedriver')
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
url = "https://search.danawa.com/dsearch.php?k1=%EB%85%B8%ED%8A%B8%EB%B6%81&module=goods&act=dispMain"
driver.get(url)
time.sleep(5)       #로딩 되기 전에 페이지 소스 긁어오지 않게 하기 위함
#
html=driver.page_source
soup = BeautifulSoup(html, "html.parser")
driver.close()
#
# #1-1. 노트북 모델명 (굵은 글씨) 출력
# item_containers = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item')
# for i in item_containers:
#     if i.has_attr('id'):                              # 이상한 애(class="prod_item product-pot")가 하나 껴있어서 그것 제외하려고 함
#                                                       # 그런데 li.prod_item만 불렀는데 왜 얘도 같이 불러와지는지?
#         name = i.select_one(".prod_name > a").text
#         print(name)
#
#1-2. 인치
item_containers = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item')
for i in item_containers:
    if i.has_attr('id'):
        inch = i.select_one(".spec_list > a:nth-child(1)").string
        print(inch)
#
# #1-3. 등록월
# item_containers = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item')
# for i in item_containers:
#     if i.has_attr('id'):
#         mor = i.select_one(".meta_item.mt_date > dd").string
#         print(mor)
#
# #1-4. 평점, 평점을 매긴 건수
# item_containers = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item')
# for i in item_containers:
#     if i.has_attr('id'):
#         point = i.select_one(".point_num > strong").string
#         cnt_opinion = i.select_one(".cnt_opinion > a").string
#         print(point, cnt_opinion)
#
#
# #2. 1-10 페이지까지 1-1~4 정보 추출
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
# item_list = []
# for i in range(1,11):
#     driver.get("http://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page="+str(i)+"&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10586%7C0&defaultVmTab=77818&defaultVaTab=9995915&tab=goods")
#     time.sleep(10)
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
#     item_containers = soup.select('#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item')
#     for j in item_containers:
#         if j.has_attr('id'):
#             if j.select_one(".point_num > strong"):
#                 name = j.select_one(".prod_name > a").text
#                 inch = j.select_one(".spec_list > a:nth-child(1)").string
#                 mor = j.select_one(".meta_item.mt_date > dd").string
#                 point = j.select_one(".point_num > strong").string
#                 cnt_opinion = j.select_one(".cnt_opinion > a").string
#             else:
#                 name = j.select_one(".prod_name > a").text
#                 inch = j.select_one(".spec_list > a:nth-child(1)").string
#                 mor = j.select_one(".meta_item.mt_date > dd").string
#                 point = "없음"
#                 cnt_opinion = "NA"
#         item_list.append(("제품명:"+name, "화면 크기:"+inch, "등록월:"+mor, "평점:"+point, cnt_opinion+"건"))
# print(item_list)
#
# #3. 보배드림 차량 정보 추출
# #연식, 연료, 가격
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
# url = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
# driver.get(url)
#
# html=driver.page_source
# soup = BeautifulSoup(html, "html.parser")
#
# item_containers = soup.select('#listCont > div.wrap-thumb-list > ul > li.product-item')
# item_list=[]
# for i in item_containers:
#     name = i.select_one("p.tit > a").string
#     year = i.select_one(".mode-cell.year > .text").text
#     fuel = i.select_one(".mode-cell.fuel > .text").text
#     price = i.select_one(".mode-cell.price > b").text
#     item_list.append((name, year, fuel, price))
# print(item_list)
#
# #4. rotten tomatoes - popular streaming movies 순위와 함께 영화 제목 추철
# # 순위 --> 리스트 순서대로 매김
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
# url = "https://www.rottentomatoes.com/"
# driver.get(url)
#
# html=driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# driver.close()
#
# rank = 0
# item_containers = soup.select("#media-lists > div.layout.media-lists > div > div.js-scores-lists-wrapper.ordered-layout__scores-wrap > div:nth-child(1) > section > text-list > ul > li")
# for i in item_containers:
#     title = i.find("span", {"class":"dynamic-text-list__item-title clamp clamp-1"}).string
#     tomatometer = i.find("span", {"slot":"tomatometer-value"}).string.strip()
#     rank += 1
#     print((rank, title, tomatometer))


print("="*50)


# # # 1. 다나와 -> 노트북 검색 결과
#
# from urllib.request import urlopen
#
# import re
#
# from selenium import webdriver
#
# driver = webdriver.Chrome('c:/scrap/chromedriver.exe')
#
# url = "http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"
#
# driver.get(url)
#
# from bs4 import BeautifulSoup
#
#
#
# html = driver.page_source
#
# soup = BeautifulSoup(html, 'html.parser')
#
#
# #
#
# # # # # 1) 노트북 모델명(굵은 글씨)
#
# name = soup.select('p.prod_name > a')
#
# for i in name:
#
# print(i.string)
#
# # # 2) 인치
#
spec_list = soup.select('div.spec_list')

for i in spec_list:

    print(i.text.strip())
#
# # # 3) 등록월
#
# date = soup.select('dl.meta_item.mt_date > dd')[:42]
#
# for i in date:
#
# print(i.string)
#
# #
#
# # # 4) 평점, 평점을 매긴 건수
#
score = soup.select('div.cnt_star > div.point_num')

num = soup.select(' div.cnt_opinion')


for i,j in zip(score, num):

    print(i.text.strip(), j.text.strip())
#
#
#
# # 2. 1번 문제를 다 해결했다면,
#
# # 1~10페이지까지 노트북에 대한 정보를 추출
#from selenium import webdriver

driver = webdriver.Chrome('/Users/junmishin/chromedriver')
for i in range(1,10):

    url ='http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page={0}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=103740&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2389&defaultVaTab=120926&tab=goods'.format(i)

driver.get(url)

from bs4 import BeautifulSoup

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
# #

spec = soup.select('div.spec_list')

name = soup.select('p.prod_name > a')

for j,k in zip(name,spec):

    print(j.text.strip(),k.text.strip())
#
#
#
# #
#
# # 3. 보배드림 -> 차량정보추출
#
url ='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'

driver.get(url)

html = driver.page_source

# print(html)

soup = BeautifulSoup(html,'html.parser')
#
#
#
# # # 1)연식
#
#
#
# year = soup.select('div.mode-cell.year > span')
#
# # year = soup.select('#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.year > span')
#
# for i in year:
#
# print(re.findall(('[\d]+[/]+[\d]+'),str(i)))
#
# # # 2)연료
#
# fuel = soup.select('div.mode-cell.fuel > span')
#
# for i in fuel:
#
# print(i.string)
#
# #
#
# # # 3)가격
#
# price = soup.select('div.mode-cell.price > b')
#
# for i in price:
#
# print([re.search('[\d|,]+',str(i)).group()],'만원')
#
#
#
# # 4. https://www.rottentomatoes.com/ => popular streaming movies
#
# # 순위와 함께 영화 제목 추출
#
# from bs4 import BeautifulSoup
#
# from selenium import webdriver
#
# url='https://www.rottentomatoes.com/'
#
# driver=webdriver.Chrome('c:/scrap/chromedriver.exe')
#
# driver.get(url)
#
# html = driver.page_source
#
# soup = BeautifulSoup(html,'html.parser')
#
# # print(soup.select('#media-lists > div.layout.media-lists > div > div.js-scores-lists-wrapper.ordered-layout__scores-wrap > div > section > text-list > ul > li'))
#
# title = (soup.select('text-list > ul > li > a:nth-child(1) > span'))
#
#
#
# for i, v in enumerate(title):
#
# print("순위 : {}, 제목: {}".format(i+1,v.text.strip()))


print("="*50)

# 1. 다나와 -> 청소기 검색 결과

# 1) 청소기 모델명(굵은 글씨)

# 3) 등록월

# 4) 평점, 평점을 매긴 건수

# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
#
# danawaUrl = "http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&tab=main"
#
# driver.get(danawaUrl)
#
# danawa = driver.page_source
#
#
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(danawa, "html.parser")
#
# cleaners = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul")
#
#
# for cleaner in cleaners:
#
#     for i in range(40):
#
#         print("모델명 :", cleaner.select("div.prod_info > p > a")[i].string)
#
#         print("등록월 :", cleaner.select("dl.meta_item.mt_date > dd")[i].string)
#
#         print("평점 :", cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_star > div.point_num > strong")[i].string, "(", cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_opinion > a")[i].string, "건)")
#
#
#
# # 2. 1번 문제를 다 해결했다면,
#
# # 1~10페이지까지 노트북에 대한 정보를 추출
#
# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
#
# from bs4 import BeautifulSoup
#
#
#
# for i in range(1, 10):
#
#     url = "http://search.danawa.com/dsearch.php?query=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&originalQuery=%EB%AC%B4%EC%84%A0%EC%B2%AD%EC%86%8C%EA%B8%B0&previousKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page="+"i"+"&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=103740&defaultPhysicsCategoryCode=72%7C80%7C81%7C0&defaultVmTab=2389&defaultVaTab=120766&tab=goods"
#
#     driver.get(url)
#
#     cleanerSource = driver.page_source
#
#     soup = BeautifulSoup(cleanerSource, "html.parser")
#
#     cleaners = soup.select("#productListArea > div.main_prodlist.main_prodlist_list > ul")
#
#     for cleaner in cleaners:
#
#         print("{0}페이지 모델명 :".format(i), cleaner.select("div.prod_info > p > a"))
#
#         print("{0}페이지 등록월 :".format(i), cleaner.select("dl.meta_item.mt_date > dd"))
#
#         print("{0}페이지 평점 :".format(i), cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_star > div.point_num > strong"))
#
#         print("{0}페이지 평점 건수 :".format(i), cleaner.select("dl.meta_item.mt_comment > dd > div.cnt_opinion > a"), "건")
#
#
#
# # 3. 보배드림 -> 차량정보추출
#
# # 1)연식
#
# # 2)연료
#
# # 3)가격
#
# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
#
# bobaeUrl = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K"
#
# driver.get(bobaeUrl)
#
# bobae = driver.page_source
#
#
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(bobae, "html.parser")
#
# import re
#
#
#
# carName = soup.select("div.mode-cell.title > p > a")
#
# carYear = soup.select("div.mode-cell.year > span.text")
#
# carFuel = soup.select("div.mode-cell.fuel > span")
#
# carPrice = soup.select("div.mode-cell.price > b > em")
#
#
#
# for i in range(3):
#
#    print("-" * 10)
#
#    print(carName[i].string)
#
#    print("연식 :", re.findall("\d+[/]\d+", str(carYear[i]))[0])
#
#    print("연료 :", carFuel[i].string)
#
#    print("가격 :", carPrice[i].string, "만원")
#
#
#
#
#
# # 4. 순위와 함께 영화 제목 추출 => popular streaming movies
#
# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/scrap/chromedriver.exe")
#
# moviesUrl = "https://www.rottentomatoes.com/"
#
# driver.get(moviesUrl)
#
# movies = driver.page_source
#
#
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(movies, "html.parser")
#
# moviesName = soup.select("div:nth-child(1) > section > text-list > ul > li")
#
#
#
# i = 0
#
# for name in moviesName:
#
#     i += 1
#
#     print("{0}위".format(i), name.select("a:nth-child(1) > span")[0].string)
#
#
