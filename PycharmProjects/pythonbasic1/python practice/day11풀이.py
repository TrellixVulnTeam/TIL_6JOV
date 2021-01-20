from selenium import webdriver

driver=webdriver.Chrome('/Users/junmishin/chromedriver')
url="http://search.danawa.com/dsearch.php?query=무선청소기&tab=main"

#url로 접속
driver.get(url) #해당 url을 브라우저에 띄움

#print(driver.current_url)
#driver.implicitly_wait(3) #웹 페이지의 모든 요소(이미지, 텍스트 등)를 모두 읽을 때까
#3초 대기
#print(driver.current_url)
#driver.implicitly_wait(3) #웹 페이지의 모든 요소(이미지, 텍스트 등)를 모두 읽을때까지 3초 대기

from bs4 import BeautifulSoup
html=driver.page_source
soup=BeautifulSoup(html, "html.parser")

prod_items=soup.select("li.prod_item")
print(prod_items[1])
print("="*50)
print(len(prod_items))





from bs4 import BeautifulSoup
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

prod_items=soup.select("li.prod.item")

print(prod_items)
print("="*50)
print(len(prod_items))




prod_items = soup.select('ul.product_list > li.prod_item')
len(prod_items)





prod_data = []
for prod_item in prod_items:
    try:
        title = prod_item.select('p.prod_name > a')[0].text.strip()
    except:
        title = ''
    try:
        spec_list = prod_item.select('div.spec_list')[0].text.strip()
    except:
        spec_list = ''
    try:
        price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(",", "")
    except:
        price = 0
    prod_data.append([title, spec_list, price])

print(len(prod_data))
print(prod_data)



from selenium import webdriver

driver=webdriver.Chrome('/Users/junmishin/chromedriver')

