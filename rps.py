import random
l=['r','p','s']

i=input("enter your choice")
c=random.choice(l)
if i==c:
	print("tie")
elif i=='r' and c=='p':
	print("computer wins")
elif i=='r' and c=='s':
	print("you win")
elif i=='s' and c=='r':
	print("computer wins")
elif i=='s' and c=='p':
	print("you win")
elif i=='p' and c=='s':
	print("computer wins")
elif i=='p' and c=='r':
	print("you win")