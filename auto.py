from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

with open('text.json', 'r') as text:
    text_dict = json.load(text)

for text in text_dict:
    msg = text["text5"]

# Call executable app for chrome	
driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
# Enter the number here
driver.get('https://web.whatsapp.com/send?phone=')

#Scan the code before proceeding further
input('Enter anything after scanning QR code to send messages')


print("Sending message(s) ") 
count = 5

# Each box's class has different name, make sure that you check it first
msg_box = driver.find_element_by_class_name('_1PRhq')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()