from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json



with open('new.json', 'r') as text:
    text_dict = json.load(text)

# Getting msg
def getMsg(msgs):
	for text in text_dict:
		if text['id'] == msgs:
			msgs = text["text"]
			# print (text["text"])

	return msgs


driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get('https://web.whatsapp.com/send?phone=')
# Config the browser driver, and link to target							


#Scan the code before proceeding further
input('Enter anything after scanning QR code to send messages')
# Input the number

count = 1

msg_box = driver.find_element_by_class_name('_1PRhq')
# Getting the msg box from whatsapp

while True:
	inp = int(input('Input type of msg: '))
	print('sendig this msg: ',getMsg(inp))
	msg_box.send_keys(getMsg(inp))
	# driver.find_element_by_class_name('_3M-N-').click()
	
	q = input("Again ?: ")
	if q=='N' or q=='n':
		break
