def convert_str_int(value):
	# Initialise the final sum 
	value_sum = 0

	# Initialise is negative as False
	is_negative = False

	# Calculate the length of the string 
	str_len = len(value)

	# Loop over and perform chr() and ord() operations 
	for i in value:
		# Check if the value is negative 
		if i == '-':
			is_negative = True
			# Decrement the string length
			str_len -= 1
		else: 
			current = ord(i) - ord('0')
			current = current * pow(10, (str_len - 1))
			value_sum += current 
			str_len -= 1 

	# Update the value_sum if negative is present 
	if is_negative:
		value_sum = value_sum * -1

	return value_sum 


print(convert_str_int('-1234'))
print(type(convert_str_int('-1234')))
