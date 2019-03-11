try:
	a=int(input("enter no."))
	if a<=3:
		b=int((a/3-a))
	elif a==3:
		raise ZeroDivisionError
	elif a>3:
		raise NameError
except ZeroDivisionError:
	print("error")
except NameError:
	print("you've chosen a no. greater than 3")
else:
	print(b)