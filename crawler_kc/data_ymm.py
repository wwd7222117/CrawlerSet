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
    factor2 = y2/1280
    #y2 = int(l[1] * 0.175)   #终点y坐标
    y2 = int(l[1]*factor2)
    driver.swipe(x1, y1, x1, y2,t)

'''def swipeUp_ymmad(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    #y1 = int(l[1] * 0.440625)   #起始y坐标
    y1 = int(l[1] * 0.341640625)
    #y2 = int(l[1] * 0.175)   #终点y坐标
    y2 = int(l[1] * 0.2028125)
    driver.swipe(x1, y1, x1, y2,t)

'''
def findads(driver):
    try:
        driver.find_element_by_id('com.wlqq.phantom.plugin.ymm.cargo:id/image')
        swipeUp(394,234,1400)
        #TouchAction(driver).press(x=100,y=399).wait(300).move_to(x=100, y=224).release().perform()
        return True
    except:
        return False

def crawl(driver):
    while True:
        flag = 0
        if findads(driver):
            continue
        try:
            start_end = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[1]').get_attribute('text')
            list_loc = start_end.split(" → ", 1)
            loc_start = list_loc[0]
            loc_end = list_loc[1]
            car_info = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[3]').get_attribute('text')
            if car_info == '   最高2万货损保障':
                car_info = content = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[4]').get_attribute('text')
                content = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[5]').get_attribute('text')
                trade = ''
                try:
                    trade = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[6]').get_attribute('text')
                except:
                    pass
                if trade == '':
                    flag = 4
                else :
                    flag = 1
            else :
                try :
                    trade = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[5]').get_attribute('text')
                except:
                        pass
                if '交易' in trade:
                    content = driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[4]').get_attribute(
                        'text')
                    flag = 2
                else :
                    content = driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView[4]').get_attribute(
                    'text')
                    flag = 3
        except BaseException as e:
            print(e)
        driver_name = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView').get_attribute('text')
        data = {'loc_start': loc_start, 'loc_end':loc_end, 'car_info':car_info,'content':content,'name':driver_name}
        #self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
        print(data)
        collection.update_one({'loc_start': loc_start, 'loc_end':loc_end, 'car_info':car_info,'content':content,'name':driver_name},{'$set': data},upsert=True)

        if flag == 2:
            driver.swipe(360,550,360,257,1000)
            #swipeUp(520,240,1600)
            #TouchAction(driver).long_press(100,521,1000).wait(300).move_to(x=100, y=224).release().perform()
        elif flag == 1:
            driver.swipe(360, 589, 360, 254,1000)
            #TouchAction(driver).long_press(100,564,1000).wait(300).move_to(x=100, y=224).release().perform()
            #swipeUp(564,240,1600)
        elif flag == 3:
            driver.swipe(360, 546, 360, 257,1000)
            #swipeUp(515,240,1600)
        elif flag == 4:
            driver.swipe(360, 584, 360, 254,1000)
            #swipeUp(559,240,1600)
        else:
            pass

        time.sleep(1)

client=pymongo.MongoClient("127.0.0.1",27017)
db=client.ymm
collection=db.ymm_driver
desired_caps = {}
desired_caps['platformName'] ='Android'
desired_caps['deviceName']='f866d421'
desired_caps['appPackage']='com.xiwei.logistics.consignor'
desired_caps['appActivity']='com.xiwei.logistics.consignor.splash.SplashActivity'#'.guide.GuideActivity'
driver_server='http://localhost:4723/wd/hub'
desired_caps['autoAcceptAlerts']="true"
desired_caps['platformVersion'] = '6.0.1'
driver = webdriver.Remote(driver_server,desired_caps)
wait = WebDriverWait(driver, 300)

#WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_id("com.kuyu:id/tv_login").is_displayed())
#time.sleep(30)
login = wait.until(EC.presence_of_element_located((By.ID, 'com.xiwei.logistics.consignor:id/dialog_btn_right')))
login.click()
phone_number = wait.until(EC.presence_of_element_located((By.ID,'com.xiwei.logistics.consignor:id/mobile')))
phone_num = input("输入手机号哦ヽ(✿ﾟ▽ﾟ)ノ:")
phone_number.send_keys(phone_num)
confirm = wait.until(EC.presence_of_element_located((By.ID,'com.xiwei.logistics.consignor:id/btn_send_verify_code')))
confirm.click()
time.sleep(5)
verify_num = input('要输入四位啊(๑•̀ㅂ•́)و✧:')
split_num = list(verify_num)
time.sleep(2)
verify1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.view.View[1]").send_keys(verify_num)
#TouchAction(driver).tap(x=167, y=461).release().perform()
cancel_ntf = wait.until(EC.presence_of_element_located((By.ID,'com.xiwei.logistics.consignor:id/iv_cancel')))
cancel_ntf.click()
time.sleep(2)
#cancel_ads = wait.until(EC.presence_of_element_located((By.ID,'com.xiwei.logistics.consignor:id/exit')))
#cancel_ads.click()

#send_loc = wait.until(EC.presence_of_element_located((By.ID,'com.wlqq.phantom.plugin.ymm.cargo:id/tv_start')))
#send_loc.click()
#选取山西全省的状况
TouchAction(driver).tap(x=72, y=1218).release().perform()
time.sleep(2)
TouchAction(driver).tap(x=89, y=183).release().perform()
time.sleep(2)
TouchAction(driver).tap(x=612, y=272).release().perform()
time.sleep(2)
TouchAction(driver).tap(x=606, y=350).release().perform()
time.sleep(2)
TouchAction(driver).tap(x=106, y=350).release().perform()
time.sleep(2)
crawl(driver)
