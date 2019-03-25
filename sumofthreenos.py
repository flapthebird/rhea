x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))
def sum(x, y, z):
    if(x == y or y == z):
    	return(0)
    elif(x==z):
    	return(0)
    else:
    	return(x + y + z)
a=sum(x,y,z) 
print(a)