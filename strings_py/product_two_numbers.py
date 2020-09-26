"""
Given two numbers as strings, find their product.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
def product_string(nums1, nums2):
	checkDict = {"0": 0,"1":1 ,"2":2 ,"3": 3,"4": 4,"5":5 ,"6": 6,"7": 7,"8":8,"9":9 }
	def convert_str_to_int(numString):
		value = 0
		for i, val in enumerate(numString):
			value += 10 ** (len(numString) - (i + 1)) * checkDict[val]
		return value 

	def convert_int_to_str(numInt):
		newDict = { value:key for key, value in checkDict.items() }
		# Returns: {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
		finalString = ""
		if numInt == 0:
			return '0'
		while numInt > 0:
			finalString = newDict[numInt % 10] + finalString
			numInt = numInt // 10
		return finalString
	# Multiplication could be donw using Karatsuba multiplication for the most optimised solution
	return convert_int_to_str(convert_str_to_int(nums1) * convert_str_to_int(nums2))

nums1 = '3'
nums2 = '2'
print(product_string(nums1, nums2))

