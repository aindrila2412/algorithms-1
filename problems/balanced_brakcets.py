# Program to check if the string parenthesis are balanced
def isValid(s):
    stack = []
    parenthesis_dict = {"(" : ")", "{": "}", "[": "]"}
    parent_list = ["(", "{", "["]

    for i in s:
        if i in parent_list:
            stack.append(i)
        elif len(satck) > 0 and parenthesis_dict[stack[-1]] == i:
            stack.pop()
        else:
            return False
    return stack == []

print(isValid("(])"))
# Returns False