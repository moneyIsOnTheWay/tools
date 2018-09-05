from selenium import webdriver
import time


# 分析页面答案下面自定义填写答案


def start():
    nums = int(input("输入答题次数:"))
    for n in range(nums):
        answers = {
            '1': 0,# 1 2
            '2': 2, # 3 4 5 6
            '3': 6, # 7 8
            '4': 8 , # 9 10 11
            '5': 0, # 1  2  3  4  5
            '6': 12, # 12  13 14
            '13': 25,
            '14': 20,
            '15': 28,
            '16': 31,
            '22': 41,
            '23': 45,
            '24': 46,
            '25': 50,
            '26': 56,
            '27': 63,
            '28': 65,
            '29': 69,
            '30': 73,
            '31': 36,
        }
        driver = webdriver.Chrome()
        url = "https://www.wjx.cn/m/20360287.aspx"
        driver.get(url)
        driver.find_element_by_id('slideChunkArrow').click()
        for i in answers:
            if i != '5' and i != '14' and i != '31':
                js = 'document.getElementsByClassName("jqradio")[' + str(answers[i]) + '].click();'
                driver.execute_script(js)
                time.sleep(2)  # 延时2秒
            elif i == '5' or i == '14' or i == '31':
                js = 'document.getElementsByClassName("jqcheck")[' + str(answers[i]) + '].click();'
                driver.execute_script(js)
                time.sleep(2)  # 延时2秒
        answers.clear()
        print('第'+ str(n+1)+'次题目填写完毕!')
        driver.find_element_by_id('ctlNext').click()
        print('第'+ str(n+1)+'次提交!')
        answers.clear()
        time.sleep(5)
        driver.close()
        # 防止问卷星要验证码这里提交一次后休眠一段时间
        time.sleep(20)


start()
