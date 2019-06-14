from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json



with open('text.json', 'r') as text:
    text_dict = json.load(text)

for text in text_dict:
	# Getting msg in json
    msg1 = 	text["text8"]

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.get('https://web.whatsapp.com/send?phone=')
											#  ^ Number goes here 


#Scan the code before proceeding further
input('Enter anything after scanning QR code to send messages')

# Get the class from msg box
msg_box = driver.find_element_by_class_name('_1PRhq')
# chat_bubble = driver.find_element_by_class_name('-N6Gq')

# print("reading chat",chat_bubble)
def chooseMsg(choice):
	switcher = {
		1: msg1
	}
	return switcher.get(choice, "Invalid choice")

while True:
	inp = int(input('Input type of msg: '))
	print('sendig this msg: ',chooseMsg(inp))
	# for i in range(count):
	print('sendig this msg: ',chooseMsg(inp))
	msg_box.send_keys(chooseMsg(inp))
	# driver.find_element_by_class_name('_3M-N-').click()
	
	q = input("Again ? y/n: ")
	if q=='N' or q=='n':
		break
