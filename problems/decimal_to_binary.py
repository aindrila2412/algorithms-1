# Function to convert decimal to bianry (not using stack)
def convert_int_to_bin(dec_num):
	check = ""
	while dec_num > 0:
		val = dec_num % 2
		# print(val)
		check += str(val)
		dec_num //= 2
		if dec_num == 0:
			return (check[::-1])

print(convert_int_to_bin(220))
