from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
for j in range(1,3):
	url = "https://codeforces.com/problemset/status/page/{j}?order=BY_ARRIVED_DESC"
	driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
	driver.get(url)

	for i in range(2,50):
		driver.find_element_by_xpath(f'//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr[{i}]/td[1]/a').click()
		WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="facebox"]/div/div/div/span/a'))).click()
		code = driver.find_element_by_xpath('//*[@id="program-source-text"]').text
		file = open(f'code{j}-{i-1}.txt','w')
		file.write(f'{code}')
		file.close()
		driver.back()


		
