# 大学生网络游戏调查问卷模板自动刷问卷脚本工具
from selenium import webdriver
import random
import time


# 分析页面答案1-4单选，5多选，6-11单选，12多选，下面自定义填写答案
answer_5 = []
answer_12 = []


def start():
    nums = int(input("输入答题次数:"))
    for n in range(nums):
        for i in range(0, random.randint(1, 8)):
            answer_5.append(i)

        for i in range(8, random.randint(8, 16)):
            answer_12.append(i)

        for i in answer_5:
            print(i)

        answers = {
            '1': random.randint(0, 1),
            '2': random.randint(2, 5),
            '3': random.randint(6, 8),
            '4': random.randint(9, 12),
            '5': answer_5,
            '6': random.randint(13, 15),
            '7': random.randint(16, 18),
            '8': random.randint(19, 21),
            '9': random.randint(22, 24),
            '10': random.randint(25, 27),
            '11': random.randint(28, 30),
            '12': answer_12,
        }
        driver = webdriver.Chrome()
        url = "https://www.wjx.cn/jq/21544695.aspx"
        driver.get(url)
        for i in answers:
            if i != '5' and i != '12':
                js = 'document.getElementsByClassName("jqRadio")[' + str(answers[i]) + '].click();'
                driver.execute_script(js)
                time.sleep(2)  # 延时2秒
            elif i == '5':
                for k in answer_5:
                    js = 'document.getElementsByClassName("jqCheckbox")[' + str(k) + '].click();'
                    driver.execute_script(js)
                    print(js)
                    time.sleep(2)  # 延时2秒
            elif i == '12':
                for k in answer_12:
                    js = 'document.getElementsByClassName("jqCheckbox")[' + str(k) + '].click();'
                    driver.execute_script(js)
                    time.sleep(2)  # 延时2秒
        answers.clear()
        answer_5.clear()
        answer_12.clear()
        print('第'+ str(n+1)+'次题目填写完毕!')
        driver.find_element_by_id('submit_button').click()
        print('第'+ str(n+1)+'次提交!')
        answers.clear()
        answer_5.clear()
        answer_12.clear()
        time.sleep(5)
        driver.close()
        # 防止问卷星要验证码这里提交一次后休眠一段时间
        time.sleep(20)


start()
