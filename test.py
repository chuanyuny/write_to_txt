#-*- coding:utf-8 -*-
from selenium import webdriver

def write_txt(content):
	fo=open('read.txt','a+')
	fo.writelines(content)
	fo.close()

driver=webdriver.Chrome()
driver.get('http://localhost:8000/index/')

driver.find_element_by_name("username").send_keys('admin')
driver.find_element_by_name("password").send_keys('123456')
driver.find_element_by_id("btn").click()
listtemp=[]
for i in range(7):
	n=str(i+1)
	inputs=driver.find_elements_by_xpath('/html/body/div[3]/div/table/tbody/tr['+n+']')
	for i in inputs:
		write_txt((i.text).encode('utf-8'))
	write_txt('\n')

driver.quit()
