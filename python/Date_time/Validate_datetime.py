from datetime import *

def validateCard(expDate):
	if expDate>datetime.now().date():
		print("valid")
	else:
		print("expired")

validateCard(date(2020,2,8))
validateCard(date(2020,12,8))