import random
l=['r','p','s']
d={'r':'rock','p':'paper','s':'scissor'}
us=0
cs=0
while True:


	i=input("enter your choice")
	if i=='q':
	   print("game is over")
	   print("comp score and user score",cs,us)
	   if us>cs:
	   	print("user won")
	   if cs>us:
	   	print("comp won")
	   if cs==us:
	   	 print("tie")

	i=input("enter your choice")
	c=random.choice(l)
	print("comp",d[c],"user",d[i])
	if i==c:
		print("tie")
	elif i=='r' and c=='p':
		print("computer wins")
		cs=cs+1
	elif i=='r' and c=='s':
		print("you win")
		us=us+1
	elif i=='s' and c=='r':
		print("computer wins")
		cs=cs+1
	elif i=='s' and c=='p':
		print("you win")
		us=us+1
	elif i=='p' and c=='s':
		print("computer wins")
		cs=cs+1
	elif i=='p' and c=='r':
		print("you win")
		us=us+1