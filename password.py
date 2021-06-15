password = 'a123456'
x = 2 
while True:
	n = input('請輸入密碼: ')
	n = str(n)
	if x < 1:
		print('居居，3次機會沒囉')
		break
	else:
		if n == password:
			print('登入成功')
			break
		else:
			print('密碼錯誤! 還有', x,'次機會')
			x = x - 1
