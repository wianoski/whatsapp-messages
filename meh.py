import webbrowser 
import json

with open('text.json', 'r') as text:
    text_dict = json.load(text)

for text in text_dict:
    msg = text["text1"]
    
    # print(text["text2"])
print(msg)
# url = "https://web.whatsapp.com/send?phone=6281270227879"

# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# webbrowser.get(chrome_path).open(url)

# print ("OK")


