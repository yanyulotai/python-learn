# coding:utf-8

import urllib.request
import datetime
import os
import time
import random


class get_renminrb:

    def getNews(self, url, file_path):
        url_status = False
        file_name = file_path + url.split('/')[-1]
        try:
            u = urllib.request.urlopen(url)
            url_code = u.status
            # print(url_status)
            # print(url_code)
            if url_code == 200:
                f = open(file_name, 'wb')
                block_sz = 8192
                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break
                    f.write(buffer)
                f.close()
                print("Sucessful to download" + " " + file_name)
                url_status = True
            # print("url_status : " + str(url_status))
            return url_status
        except Exception as e:
            # print(e)
            # print("友情提示：检查是否有该文件夹")
            return False

    def request_url(self, search_date, i):
        file_path = "F:/rmrb2019/"
        year = str(search_date[0: 4])
        month = str(search_date[5: 7])
        day = str(search_date[-2:])
        if i < 10:
            i = "0" + str(i)
        url = str("http://paper.people.com.cn/rmrb/page/" + year + "-" + month + "/" + day + "/" + str(
            i) + "/rmrb" + year + "" + month + "" + day + str(i) + ".pdf")
        # print(str(url))
        url_status = self.getNews(url, file_path)
        # print(str(i) + ":" + str(url_status))
        if url_status:
            # seq = range(5)
            # sleep_time = random.choice(seq)
            # # print("sleep_time: " + str(sleep_time))
            # time.sleep(sleep_time)
            i = int(i) + 1
            # print(i)
            self.request_url(search_date, i)
        else:
            print(str(search_date) + " 内容已抓取完成！ 共" + str(int(i) - 1) + "页")
        # exit(1)


if __name__ == '__main__':
    rmrb = get_renminrb()
    search_date = "2019-09-17"
    rmrb.request_url(search_date, 1)
    # begin = datetime.date(2019, 8, 15)
    # end = datetime.date(2019, 8, 15)
    # for i in range((end - begin).days + 1):
    #     day = begin + datetime.timedelta(days=i)
    #    search_date = str(day)
    #    rmrb.request_url(search_date, 1)
