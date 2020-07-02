from selenium import webdriver
import time

try:
    #使用chrome浏览器模拟点击登录
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    browser.get('https://shimo.im/login?from=home')

    #输入注册手机号或邮箱、密码，点击立即登录
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18010095180')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('lb1234')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

except Exception as e:
    print(e)
# finally:    
#     browser.close()