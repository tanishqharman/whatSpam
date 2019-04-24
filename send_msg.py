from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# path where chrome-webdriver is located
driver = webdriver.Chrome('/home/tan_ishq/Desktop/whatSpam/chromedriver') 

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# contact name or group name whom you want to send message
target = '"W Navneet Rawat"'

# write the message
string = "Unblock kar....BSDK!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

# set the frequency of message in range
for i in range(500):
	message.send_keys(string + Keys.ENTER)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()

driver.close()
