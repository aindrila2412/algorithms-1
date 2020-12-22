# Implementation of Knuth Morris Pratt Algorithm 

# Method to get array for the pattern to match based on the failure function 
def getArray(substring):
    substring_len = len(substring)
    i = 0 
    j = 1 

    # No proper prefix for string of length 1 
    global test_array 
    test_array[0] = 0

    # Loop over till the second pointer reaches the end of the array 
    while j < substring_len:
        if substring[i] == substring[j]:
            i = i + 1 
            test_array[j] = i 
            j = j + 1 

        # If the first character didn't matched 
        elif i == 0:
            test_array[j] = 0 
            j = j + 1 
        
        # Mismatch after at least one matching character 
        else:
            i = test_array[i - 1]

# Implementation of KMP algorithm 
def kmp(substring, text):
    # Initialise variables:
    i = 0
    j = 0

    # Loop over and search
    while i < len(substring) and j < len(text):
        # Last character matches -> Substring found:
        if substring[i] == text[j] and i == len(substring) - 1:
            return True

        # Character matches:
        elif substring[i] == text[j]:
            i += 1
            j += 1

        # Character didn't match -> Backtrack:
        else:
            if i != 0:
                i = test_array[i-1] 
            else:
                j += 1

    # Return false if substring not found
    return False

text = "abxabcabcaby"
substring = "abcaby"
test_array = [None] * len(substring) 
getArray(substring)
print(kmp(substring, text))
print(test_array)
