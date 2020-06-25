# Program to reverse a string, could be done using str[::-1] though
def ReverseString(List):
	new_list = []
	for i in List:
	    new_list.append(i)
	for i in range(0, len(new_list), 1):
	    List[i] = new_list.pop()
	print(List)

ReverseString(["h","e","l","l","o"])