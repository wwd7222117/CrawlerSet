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
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)

def crawl():
    while True:
        items = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView' )))
        swipeUp(1500)
        for item in items:
            try:
                nickname = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderCompany').get_attribute('text')
                content = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderStartTime').get_attribute('text')
                list_time = content.split("至", 1)
                start_time = list_time[0]
                deadline = list_time[1]
                send = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderDetailStartAdd').get_attribute('text')
                receive = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderDetailEndAdd').get_attribute('text')
                type = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderDetailGoodsType1').get_attribute('text')
                raw_price= item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_orderDetailFreight1').get_attribute('text')
                price = re.findall(r"\d+\.?\d*", raw_price)[0]
                raw_distance = item.find_element_by_id('com.kuaichengwuliu.driver:id/tv_search_goods_distance').get_attribute('text')
                list_raw = re.findall(r"\d+\.?\d*",raw_distance)
                distance = list_raw[1]
                data = {'nickname': nickname, 'start_time':start_time, 'deadline':deadline,'send':send,'receive':receive,'type':type,'price':price,'distance':distance}
                #self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                print(data)

                collection.update_one({'nickname': nickname,'start_time':start_time,'deadline':deadline,'send':send,'receive':receive,'type':type,'price':price,'distance':distance}, {'$set': data},upsert=True)

            except BaseException as e:
                print(e)



client=pymongo.MongoClient("127.0.0.1",27017)
db=client.kc_data
collection=db.data_detail
desired_caps = {}
desired_caps['platformName'] ='Android'
desired_caps['deviceName']='f866d421'
desired_caps['appPackage']='com.kuaichengwuliu.driver'
desired_caps['appActivity']='.guide.GuideActivity'#'.guide.GuideActivity'
driver_server='http://localhost:4723/wd/hub'
desired_caps['autoAcceptAlerts']="true"
desired_caps['platformVersion'] = '6.0.1'
driver = webdriver.Remote(driver_server,desired_caps)
wait = WebDriverWait(driver, 300)

#WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_id("com.kuyu:id/tv_login").is_displayed())
#time.sleep(30)
WebDriverWait(driver, 7).until(lambda the_driver: driver.find_element_by_id("android:id/content").is_displayed())
TouchAction(driver).tap(x=545, y=181).release().perform()
time.sleep(1)
TouchAction(driver).tap(x=161, y=706).release().perform()
time.sleep(1)
TouchAction(driver).tap(x=534, y=1029).release().perform()
time.sleep(1)
TouchAction(driver).tap(x=183, y=1029).release().perform()
time.sleep(1)
TouchAction(driver).tap(x=528, y=701).release().perform()
time.sleep(1)
TouchAction(driver).tap(x=183, y=684).release().perform()
time.sleep(4)
TouchAction(driver).tap(x=161, y=306).release().perform()
time.sleep(4)
TouchAction(driver).tap(x=128, y=303).release().perform()
time.sleep(5)
crawl()


# 输入用户名
#driver.find_element_by_id("com.kuyu:id/et_email").send_keys("******")
# 输入密码
#driver.find_element_by_id("com.kuyu:id/et_pwd").send_keys("******")
# 点击登录
#driver.find_element_by_id("com.kuyu:id/tv_login").click()
# 这里加了一个等待,判断指定的元素出现则为登录成功(等待方法不懂没有关系，以后会再讲解如何设置等待)
#WebDriverWait(driver, 20).until(
#    lambda the_driver: the_driver.find_element_by_id("com.kuyu:id/include_study_iv_add").is_displayed())
print(u"登录成功")
#driver.quit()
#TouchAction(driver).press(x=297, y=1073).move_to(x=309, y=459).release().perform()
