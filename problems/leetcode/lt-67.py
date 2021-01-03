# 67. Add Binary
"""
    Given two binary strings a and b, return their sum as a binary string.
    Input: a = "111", b = "1010101"
    Output: "1011100"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Single liner answer could be the following:
        # return bin(int(a, 2) + int(b, 2))[2:]
        # Using XOR truth table 
        # T or T -> F (1+1 = 0, carry 1)
        # T or F -> T (1+0 = 1)
        # F or T -> T (0+1 = 1)
        # F or F -> F (0+0 = 0)

        # Approach A using extra space (using stacks )
        # Takes less time but more space
        aList = list()
        bList = list()
        
        for i in a:
            aList.append(i)
        for i in b:
            bList.append(i)
            
        listA = []
        listB = []
        final = ""
        
        if len(aList) > len(bList):
            listA = aList 
            listB = bList
        else:
            listA = bList 
            listB = aList 

        carry = 0
        
        while listA != [] or listB != []:
            sums = carry 
            if listA != []:
                sums += int(listA.pop())
            if listB != []:
                sums += int(listB.pop())


            final = final + str(sums % 2)
            carry = sums // 2

            # Using conditional statements
            # if sums == 3:
            #     final = final + str(1)
            #     carry = 1 
            # elif sums == 2:
            #     final = final + str(0)
            #     carry = 1 
            # else:
            #     final = final + str(sums)
            #     carry = 0
                
        if carry == 1:
            final = final + str(1)
        
        return final[::-1]


        # Approach B not using extra space 
        # Takes more time but less space 
        lenA = len(a) - 1
        lenB = len(b) - 1
        sums = 0
        final = ""
        while lenA >= 0 or lenB >= 0 or sums > 0:
            if lenA >= 0:
                sums += int(a[lenA])
                lenA -= 1
            if lenB >= 0:
                sums += int(b[lenB])
                lenB -= 1 
            final = final + str(sums % 2)
            sums = sums // 2
        return final 