# Sum of two linked list 
def sum_two_lists(self, llist):
	# Method 1 using strings 
    sum_llist = LinkedList()
    p = self.head 
    q = llist.head 
    s1 = ""
    s2 = ""
    if p:
        while p:
            s1 += str(p.data)
            p = p.next 
    else:
        s1 = '0'
    if q:
        while q:
            s2 += str(q.data)
            q = q.next
    else:
        s2 = '0'
    s1 = int(s1[::-1])
    s2 = int(s2[::-1])
    s3 = str(s1+ s2)
    s3 = s3[::-1]
    # print(s3)
    for i in s3:
        sum_llist.append(int(i))
    return sum_llist

    # Method 2 
    sum_llist = LinkedList() 
    p = self.head 
    q = llist.head 
    carry = 0

    while p or q:
    	if not p:
    		a = 0 
    	else:
    		a = p.data 
    	if not q:
    		b = 0
    	else:
    		b = q.data
    	sums = a + b + carry

    	if sums >= 10:
    		carry = 1
    		remainder = sums % 10
    		sum_llist.append(remainder)
    	else: 
    		carry = 0
    		sum_llist.append(sums)

    	if p:
    		p = p.next 
    	if q:
    		q = q.next 
    return sum_llist



