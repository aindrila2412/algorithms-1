'''
	Return Pairs from a doubly linked list which sums to a specified number.
	
	Input: (1->2->3->4->5, sum_key = 5)
	Output: ['(1,4)', '(2,3)']
'''
def get_pairs_sum(self, sum_key):
	first = self.heaf 
	second = None 
	final_list = list()
	while first:
		second = first.next 
		while second:
			if first.data + second.data == sum_key:
				# final_list.append(str(tuple([first.data, second.data])))
				final_list.append("(" + str(first.data) + "," + str(second.data) + ")")
			second = second.next 
		first = first.next 
	return final_list
