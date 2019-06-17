from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymongo

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

'''
解释：int start x－开始滑动的x坐标，

  int start y －开始滑动的y坐标。

   int end x －结束点x坐标，

   int end y －结束点y坐标。

   duration 滑动时间（默认5毫秒）；
'''

def swipeUp(y1,y2,t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    factor1 = y1/1280
    #y1 = int(l[1] * factor1)   #起始y坐标
    y1 = int(l[1] * factor1)
    #factor2 = y2/1280
    y2 = int(l[1] * 0.175)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

def crawl(driver):
    i = 1
    while True:
        i+=1
        try:
            #start_end = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[1]').get_attribute('text')
            loc_start = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').get_attribute('text')
            loc_end = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[3]').get_attribute('text')

            car_info = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView').get_attribute('text')
            driver_name = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView').get_attribute('text')
        except BaseException as e:
            print(e)
        #driver_name = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView').get_attribute('text')
        data = {'loc_start': loc_start, 'loc_end':loc_end, 'car_info':car_info,'name':driver_name}
        #self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
        print(data)
        collection.update_one({'loc_start': loc_start, 'loc_end':loc_end, 'car_info':car_info,'name':driver_name},{'$set': data},upsert=True)
        driver.swipe(500,442,500,265,500)
        if i%8 == 0:
            time.sleep(0.5)
        #time.sleep(1)

client=pymongo.MongoClient("127.0.0.1",27017)
db=client.lujing
collection=db.car_market
desired_caps = {}
desired_caps['platformName'] ='Android'
desired_caps['deviceName']='f866d421'
desired_caps['appPackage']='com.transfar56.project.uc'
desired_caps['appActivity']='com.transfar.tradedriver.ui.module.main.StartupActivity'#'.guide.GuideActivity'
driver_server='http://localhost:4723/wd/hub'
desired_caps['autoAcceptAlerts']="true"
desired_caps['platformVersion'] = '6.0.1'
driver = webdriver.Remote(driver_server,desired_caps)
wait = WebDriverWait(driver, 300)

#WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_id("com.kuyu:id/tv_login").is_displayed())
#time.sleep(30)
login = wait.until(EC.presence_of_element_located((By.ID, 'com.transfar56.project.uc:id/mAgreeProtocolBtn')))
login.click()
time.sleep(2)
TouchAction(driver).press(x=600, y=1013).move_to(x=300, y=1030).release().perform() #左翻页
time.sleep(2)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
tap_x = x*0.5
tap_y = y*0.85
TouchAction(driver).tap(x=tap_x, y=tap_y).release().perform()
time.sleep(2)
crawl(driver)
driver.quit()
#TouchAction(driver).tap(x=167, y=461).release().perform()
# com.transfar56.project.uc:id/mAgreeProtocolBtn 同意按钮
# TouchAction(driver).press(x=813, y=1013).move_to(x=254, y=1030).release().perform() 左翻页
'''   用来点击立即体验：
x = self.driver.get_window_size()['width']
y = self.driver.get_window_size()['height']
tap_x = x*0.5
tap_y = y*0.85
TouchAction(driver).tap(x=tap_x, y=tap_y).release().perform()
'''

