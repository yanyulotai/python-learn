import datetime
import time


class test_dingshi:

    def main(self):
        """h表示设定的小时，m为设定的分钟"""
        while True:
            now = datetime.datetime.now()
            if now.hour == 11 and now.minute == 0 and now.second == 0:
                print("开始抢")
                # 点立即抢购
                # self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="J_LinkBuy"]')).click()
                # 点提交订单
                # self.wait.until(lambda s: s.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a')).click()
            time.sleep(0.001)
            print("target is 11:00 ；now is " + str(now.hour) + ":" + str(now.second))


if __name__ == '__main__':
    a = test_dingshi()
    a.main()
