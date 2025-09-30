from threading import Thread

def dispalynumber():
	i = 0
	while (i<=10):
		print(i)
		i+=1

t = Thread(target=dispalynumber)
t.start()
