def isEven(integer_value):
	result = integer_value % 2
	if result == 0:
		return True
	return False

def three_options(integer_value):
	modvalue = integer_value % 3
	if modvalue == 0:
		print("cool")
	elif modvalue == 1:
		print("not cool")
	elif modvalue == 2:
		print("very not cool")
	
	
check_value = int(input("Enter an integer: "))
if isEven(check_value) is True:
	print("yay an even number.")
else:
	print("o noes it's odd.")