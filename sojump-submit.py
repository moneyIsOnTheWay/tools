from selenium import webdriver
import random
import time

driver = webdriver.Firefox()  # 使用火狐浏览器
url = 'https://www.wjx.cn/m/20834858.aspx?from=singlemessage#'
driver.get(url)  # 打开浏览器并访问URL地址

# 0:A   1:B    2:C    3:D
# # q1 = 'q1_' + str(random.randint(1 ,2))
q1 = random.randint(0, 1)
# # q2 = 'q2_' + str(random.randint(1 ,2))
q2 = random.randint(2, 3)
# # q3 = 'q3_' + str(random.randint(1 ,4))
q3 = random.randint(4, 7)
# # q4 = 'q4_1'
q4 = 9
# # q5 = 'q5_1'
q5 = 11
# # q6 = 'q6_1'
q6 = 14
# # q7 = 'q7_3'
q7 = 19
# # q8 = 'q8_3'
q8 = 23
# # q9 = 'q9_' + str(random.randint(2 ,3))
q9 = random.randint(26, 27)
# # q10 = 'q10_3'
q10 = 31
#
# # q11 = 'q11_' + str(random.randint(2 ,3))
q11 = random.randint(34, 35)
#
# # q12 = 'q12_' + str(random.randint(2 ,3))
q12 = random.randint(37, 38)
#
# # q13 = 'q13_3'
q13 = 43
#
# # q14 = 'q14_' + str(random.randint(2 ,3))
q14 = random.randint(45, 46)
#
# # q15 = 'q15_3'
q15 = 50
#
# # q16 = 'q16_' + str(random.randint(2 ,3))
q16 = random.randint(53, 54)
#
# # q17 = 'q17_' + str(random.randint(3 ,4))
q17 = random.randint(58, 59)
#
# # q18 = 'q18_' + str(random.randint(2 ,4))
q18 = random.randint(61, 63)
# # q19 = 'q19_' + str(random.randint(2 ,4))
q19 = random.randint(65, 67)
# # q20 = 'q20_' + str(random.randint(2 ,3))
q20 = random.randint(69, 70)
answer = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
# # js = 'obj = document.getElementsByTagName("input");' \
# #      ' for(var i=0;i<obj.length;i++){ obj[i].style.display="block";}'
# # driver.execute_script(js)
# time.sleep(1)  # 延时2秒
# #
# 20道题
for i in answer:
    js = 'document.getElementsByClassName("jqradio")['+str(i)+'].click();'
    driver.execute_script(js)
    time.sleep(2)  # 延时2秒
#     # js = 'document.getElementsByTagName("input").style.display="block";'
#     # driver.find_element_by_xpath('//input[@type="radio" and @id='+'"'+ i + '"' ' ]').click()
#     # driver.find_element_by_xpath('//input[@type="radio" and @id=' + '"' + i + '"' ' ]').send_keys(Keys.SPACE)
#
#
print('答题完毕!')
driver.find_element_by_id('ctlNext').click()
print("一次问卷调查填写完毕")
