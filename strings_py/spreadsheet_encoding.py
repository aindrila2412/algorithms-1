"""
Provide a solution to the problem of implementing a function that converts a spreadsheet 
column ID (i.e., “A”, “B”, “C”, …, “Z”, “AA”, etc.) to the corresponding integer. 
For example, “A” equals 1 because it represents the first column, while “AA” equals 27 because 
it represents the 27th column.
"""
def spreadsheet_encoding(val_str):
	count = len(val_str) - 1
	value = 0
	for i in val_str:
		value += 26 ** count * (ord(i) - ord('A') + 1)
		count -= 1
	return value 

print(spreadsheet_encoding('AZZZ'))