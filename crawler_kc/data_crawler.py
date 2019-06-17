from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
wait=WebDriverWait(browser,15)

def crawle():
    url='https://www.1688.com/'
    browser.get(url=url)
    #叉掉首页弹出大框
    button=browser.find_element_by_class_name('identity-cancel')
    button.click()
    #定位搜索框
    input=browser.find_element_by_id('alisearch-keywords')
    input.send_keys('女装')
    #定位搜索按钮
    sea_button=browser.find_element_by_id('alisearch-submit')
    sea_button.click()
    #叉掉框图
    button_1=browser.find_element_by_class_name('s-overlay-close-l')
    button_1.click()
    #定位成交量
    button_deal=browser.find_elements_by_css_selector('.sm-widget-sort.fd-clr.s-widget-sortfilt li')[1]
    button_deal.click()
    try:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#offer60')))
    except :
        print('*'*30,'超时加载','*'*30,'\n\n\n')
    get_products()

from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc('.sm-offer .fd-clr .sm-offer-item').items()
    index=0
    for item in items:
        index+=1
        print('*'*50)
        title=item.find('.s-widget-offershopwindowtitle').text().split('\n')
        title=' '.join(title)
        price_a=item.find('.s-widget-offershopwindowprice').text().split('\n')
        price=''.join(price_a[:2])
        deal=''.join(price_a[2:])
        #产品网址
        text=item.find('.s-widget-offershopwindowtitle')
        soup=BeautifulSoup(str(text),'lxml')
        a=soup.select('.s-widget-offershopwindowtitle a')[0]
        url=a['href']
        print(title)
        print(price)
        print(deal)
        print(url)


    print(' (●ˇ∀ˇ●) '*5)
    print('一共%d条数据'%index)


crawle()
