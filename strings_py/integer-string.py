"""
Given some integer as input, (i.e. … -3, -2, -1, 0, 1, 2, 3 …) and you have to convert the integer 
you are given to a string.
"""

def convert_int_string(value):
	# Getting the absolute value of the integers 
	if value < 0:
		is_negative = True 
		value = -1 * value 
	else: 
		is_negative = False 

	# transit array 
	transit_arr = []

	# Loop over and add the ord() values 
	while value > 0:
		current = value % 10 
		current = chr(ord('0') + current)
		transit_arr.append(current)
		value = value // 10

	# Reverse the array
	transit_arr = transit_arr[::-1]

	# Add each value to an empty string 
	final_string = "".join(transit_arr)

	# Add the negative sign if there any
	if is_negative == True:
		final_string = '-' + transit_arr

	return final_string

print(convert_int_string(1234))
print(type(convert_int_string(1234)))





