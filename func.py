#creating a function without parameters
def func():
	print("hi")
	print("hello")
func()

#with parameters
def func2(a): #a=1
	print("hii\t",a)
func2("abs")

#with 2|3 parameters
def func3(a,b,c): #a=2,b=5,c=6
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)

#with default parameter
def func4(university="CMR"):
	print("I am in"+"\t"+university)
func4("IIM")
func4("IIT")
func4()

#return statement
def func7(a,b,c): #a=2,b=5,c=6
	d=a+b+c
	return d
e=func7(2,5,6)
print(e)

#calling one function from other and return statement

def func5(a,b):
	print("hey other function")
	c=a+b
	return c
def func6():
	print("hello calling another function")
	s=func5(2,7)
	print("addition is",s)
func6()