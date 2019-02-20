# -*- coding: utf-8 -*-
'''
Created on Tue Mar  6 16:49:25 2018
'''
'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个
以后每天早上都吃了前一天剩下的一半零一个
到第10天早上想再吃时，见只剩下一个桃子了
求第一天共摘了多少。
程序分析：采取逆向思维的方法，从后往前推断
'''
#解法0：Tn=(Tn+1) *2，第9天吃完桃子就剩1个了，吃之前=（1+1）*2=4个
x =1
for day in range(0,9):
    x = (x+1)*2
print(x)
#解法1：正序的递归排序
def fun(x):
    if x ==10:
        return 1
    else:
        return (fun(x+1)+1)*2
print(fun(1))