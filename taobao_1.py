# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import datetime


class taobao_1:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

    def login(self):

        self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://www.taobao.com/')
        # 窗口最大化
        self.driver.maximize_window()

        login_button = self.wait.until(
            lambda s: s.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'))
        login_button.click()
        print("扫码登录")
        time.sleep(3)

        # 1.到达收藏的具体宝贝页面，
        # 2.等待到时间点击立即抢购并提交订单

        # 到达收藏夹
        self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="J_SiteNavFavor"]/div[1]/a/span[2]')).click()
        # 到达收藏的第一个宝贝页面
        self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="fav-list"]/ul/li[1]/div[1]/div[1]/a/img')).click()

        while True:
            now = datetime.datetime.now()
            if now.hour == 11 and now.minute == 0 and now.second == 0:
                print("开始抢")
                try:
                    # 点立即抢购
                    self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="J_LinkBuy"]')).click()
                    # 点提交订单
                    self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a')).click()
                except TimeoutException:
                    print("很遗憾，没有抢到")
                    break
            time.sleep(0.001)
            print("target is 11:00:00 ；now is " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))


if __name__ == '__main__':
    broeser = taobao_1()
    broeser.login()
