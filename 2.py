try:
	#s=0
	s=3/0
	print(s)
	raise ZeroDivisionError
except ZeroDivisionError:
	print("error")