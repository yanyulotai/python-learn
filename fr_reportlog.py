# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class fr_reportlog:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

    def login(self):

        self.driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('http://bi.wancaitong.com')
        self.switch_which_frame('reportFrame')
        # 显式获取用户名输入框并输入用户名
        username = self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/input'))
        username.send_keys('test')
        # username.send_keys('admin')

        password = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="bi-absolute-layout"]//input[@type="password"]'))
        password.send_keys('778899a!')
        # password.send_keys('admin')

        # 单击登录
        login_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="bi-card-layout"]//div[1]//div[1]//div[6]//div[1]'))
        login_button.click()
        time.sleep(5)
        print("登录成功")

        duijiang = self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div/div[4]/div'))
        duijiang.click()

        # 点击摇一摇
        # shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="zzza_tixing"]//a[@class="zzza_hall_bottom_right_yjan_btn"]'))
        # shake_button.click()
        # time.sleep(3)
        #
        # # 重新定位标签页
        # self.driver.switch_to.window(self.driver.window_handles[1])
        #
        # # 点击开始摇奖
        # shake_button = self.wait.until(lambda s: s.find_element_by_xpath('//div[@class="zzza_button_1"]//a[@onclick="go_yj();"]'))
        # shake_button.click()
        # time.sleep(10)
        #
        # # 关闭浏览器
        # self.driver.quit()

    def switch_which_frame(self, frame_name):
        """
        切换Frame
        """
        i = 0
        while True:
            try:
                # self.browser.switch_to.frame(frame_name)
                WebDriverWait(self.driver,15).until(EC.frame_to_be_available_and_switch_to_it(frame_name))
            except TimeoutException:
                time.sleep(1)
                print(str(i))
                i = i + 1
                if i > 3:
                    raise TimeoutException
            else:
                print("Find this "+frame_name)
                break


if __name__ == '__main__':
    broeser = fr_reportlog()
    while True:
        data_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_time = int(data_time[11:13])
        print('当前小时：'+str(current_time))
        print('当前时间：'+str(data_time))
        if current_time == 11:
            broeser.login()
            # print('签到完成')
            # time.sleep(3580)
        else:
            print('不在签到时间：sleep3600')
            time.sleep(3600)