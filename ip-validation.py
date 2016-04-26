
def ip_validate(string):
	fields = string.split('.')
	try:
		validator = lambda x: len(x) == len(str(int(x))) and 0 <= int(x) <= 255
		return True if all(map(validator, fields)) and len(fields) == 4 else False
	except:
		return False