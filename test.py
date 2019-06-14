import json



with open('new.json', 'r') as text:
    text_dict = json.load(text)

def getMsg(inp):
	for text in text_dict:
		if text['id'] == inp:
			msg=text["text"]
			print (msg)

	return msg

while True:

	inputs = int(input('which msg do u looking for ?: '))
	getMsg(inputs)

	q = input('y/n ?: ')
	if q=='n':
		break