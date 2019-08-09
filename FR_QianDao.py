# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class SigninFanRuan:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

    def login(self):

        self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('http://id.fanruan.com/login/login.php?clue=bbs&referrer=http%3A%2F%2Fbbs.fanruan.com%2F')
        # 显式获取用户名输入框并输入用户名
        username = self.wait.until(lambda s: s.find_element_by_xpath('//aside[@class="typeArea"]//input[@type="text"]'))
        username.send_keys('17686512179')

        password = self.wait.until(lambda s: s.find_element_by_xpath('//aside[@class="typeArea"]//input[@type="password"]'))
        password.send_keys('g17686512179')

        # 单击登录
        login_button = self.wait.until(lambda s: s.find_element_by_xpath('//aside[@class="typeArea"]//input[@id="submitButton"]'))
        login_button.click()
        time.sleep(5)

        # 点击摇一摇
        shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="zzza_tixing"]//a[@class="zzza_hall_bottom_right_yjan_btn"]'))
        shake_button.click()
        time.sleep(3)

        # 重新定位标签页
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 点击开始摇奖
        shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="zzza_button_1"]//a[@onclick="go_yj();"]'))
        shake_button.click()
        time.sleep(10)

        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    broeser = SigninFanRuan()
    while True:
        data_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_time = int(data_time[11:13])
        print('当前小时：'+str(current_time))
        print('当前时间：'+str(data_time))
        if current_time == 8:
            broeser.login()
            print('签到完成')
            time.sleep(3580)
        else:
            print('不在签到时间：sleep3600')
            time.sleep(3600)
