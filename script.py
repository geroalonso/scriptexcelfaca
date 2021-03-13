import pyperclip
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver)
url = ''
driver.get(url)

element = driver.find_element_by_xpath("").click()
element.send_keys("some text")



df = pd.read_excel(r'',  engine = 'openpyxl', sheet_name=0,  usecols='A:J')



def pegardato(xpathcelda,  info):
	#clickeacelda usando xpathcelda 
	#send keys info


for numerofila in range(len(df.index)):
	row = df.iloc[numerofila].tolist()
	row.pop(2) #saco el timestamp
	for dato in row:
		pegardato(xpathcelda= "", info = dato)




