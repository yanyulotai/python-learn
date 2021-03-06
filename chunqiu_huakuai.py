# 图像处理标准库
from PIL import Image
# web测试
from selenium import webdriver
# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
# 等待时间 产生随机数
import time, random

# 打开页面至屏幕最大尺寸
driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.get('https://account.ch.com/NonRegistrations-Regist')
driver.maximize_window()
# 获取输入手机号码的表单
input1 = driver.find_element_by_name('phoneNumberInput')
# 输入注册号码
input1.send_keys(17686512179)
time.sleep(0.2)
# 获取打开滑块验证码页面的元素
getcheck = driver.find_element_by_id('getDynamicPwd')
# 点击进入滑块验证码页面
getcheck.click()
time.sleep(5)
# 获取拖拽的圆球
slideblock = driver.find_element_by_class_name('geetest_slider_button')
# 鼠标点击圆球不松开
ActionChains(driver).click_and_hold(slideblock).perform()
# 将圆球滑至相对起点位置的最右边
ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
time.sleep(0.4)
# 保存包含滑块及缺口的页面截图
driver.save_screenshot('d://quekou.png')
# 放开圆球
ActionChains(driver).release(slideblock).perform()
# 打开保存至本地的缺口页面截图
quekouimg = Image.open('d://quekou.png')


def match_source(image):
    imagea = Image.open('d://source1.png')
    imageb = Image.open('d://source2.png')
    imagec = Image.open('d://source3.png')
    imaged = Image.open('d://source4.png')
    list = [imagea, imageb, imagec, imaged]
    # 通过像素差遍历匹配本地原图
    for i in list:
        # 本人电脑原图与缺口图对应滑块图片横坐标相同，纵坐标原图比缺口图大88px，可根据实际情况修改
        pixel1 = image.getpixel((868, 340))
        pixel2 = i.getpixel((868, 428))
        # pixel[0]代表R值，pixel[1]代表G值，pixel[2]代表B值
        if abs(pixel1[0] - pixel2[0]) < 5:
            return i
    return image

# 匹配本地对应原图
sourceimg = match_source(quekouimg)




# 计算滑块位移距离
def get_diff_location(image1, image2):
    # （825,1082）（335,463）为滑块图片区域，可根据实际情况修改
    for i in range(825, 1082):
        for j in range(335, 463):
            # 遍历原图与缺口图像素值寻找缺口位置
            if is_similar(image1, image2, i, j) == False:
                return i
    return -1


# 获取缺口位置
visualstack = get_diff_location(sourceimg, quekouimg)
# 获取移动距离loc，827为滑块起点位置
loc = visualstack - 827


# 对比RGB值得到缺口位置
def is_similar(image1, image2, x, y):
    pixel1 = image1.getpixel((x, y + 88))
    pixel2 = image2.getpixel((x, y))
    # 截图像素也许存在误差，50作为容差范围
    if abs(pixel1[0] - pixel2[0]) >= 50 and abs(pixel1[1] - pixel2[1]) >= 50 and abs(pixel1[2] - pixel2[2]) >= 50:
        return False
    return True


# 滑块移动轨迹
def get_track(self, distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = random.randint(2, 3) / 10
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


# 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
track_list = get_track(loc + 3)
time.sleep(2)
ActionChains(driver).click_and_hold(slideblock).perform()
time.sleep(0.2)
# 根据轨迹拖拽圆球
for track in track_list:
    ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()
# 模拟人工滑动超过缺口位置返回至缺口的情况，数据来源于人工滑动轨迹，同时还加入了随机数，都是为了更贴近人工滑动轨迹
imitate = ActionChains(driver).move_by_offset(xoffset=-1, yoffset=0)
time.sleep(0.015)
imitate.perform()
time.sleep(random.randint(6, 10) / 10)
imitate.perform()
time.sleep(0.04)
imitate.perform()
time.sleep(0.012)
imitate.perform()
time.sleep(0.019)
imitate.perform()
time.sleep(0.033)
ActionChains(driver).move_by_offset(xoffset=1, yoffset=0).perform()
# 放开圆球
ActionChains(driver).pause(random.randint(6, 14) / 10).release(slideblock).perform()
time.sleep(2)
# 务必记得加入quit()或close()结束进程，不断测试电脑只会卡卡西
driver.close()
