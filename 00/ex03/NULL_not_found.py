def NULL_not_found(object: any) -> int:
	if (isinstance(object, type(None))):
		print("Nothing: None <class 'NoneType'>")
	if (isinstance(object, float)):
		print("Cheese: NaN <class 'float'>")
	elif (isinstance(object, bool)) and object is False:
		print("False: <class 'bool'>")
	elif (isinstance(object, int)) and object == 0:
		print("Zero: <class 'int'>")
	elif (isinstance(object, str)) and object == '':
		print("Empty: <class 'str'>")
	else:
		print("Type not Found")
		return 1
	return 0