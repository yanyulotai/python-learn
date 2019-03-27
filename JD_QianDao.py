# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class SigninJingDong:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

    def login(self):

        self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('https://passport.jd.com/uc/login?ltype=logout')

        # 单击账号登录
        login_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="login-tab login-tab-r"]'))
        login_button.click()
        time.sleep(5)
        # 显式获取用户名输入框并输入用户名
        username = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="item item-fore1"]//input[@type="text"]'))
        username.send_keys('17686512179')

        password = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="item item-fore2"]//input[@type="password"]'))
        password.send_keys('g17686512179')

        # 单击登录
        login_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="login-btn"]//a[@id="loginsubmit"]'))
        login_button.click()
        time.sleep(5)

        # 点击用户名
        shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="dt cw-icon"]//a[@class="nickname"]'))
        shake_button.click()
        time.sleep(3)

        # 重新定位标签页
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 点击京豆
        shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="num"]//a[@href="//bean.jd.com/myJingBean/list"]'))
        shake_button.click()
        time.sleep(2)

        # 重新定位标签页
        self.driver.switch_to.window(self.driver.window_handles[2])

        # 点击赚京豆
        shake_button = self.wait.until(
            lambda s: s.find_element_by_xpath('//div[@class="bi-btnbox"]//a[@href="#earnBean"]'))
        shake_button.click()
        time.sleep(5)

        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    broeser = SigninJingDong()
    while True:
        data_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_time = int(data_time[11:13])
        print('当前小时：'+str(current_time))
        print('当前时间：'+str(data_time))
        if current_time == 11:
            broeser.login()
            print('签到完成')
            time.sleep(3580)
        else:
            print('不在签到时间：sleep3600')
            time.sleep(3600)