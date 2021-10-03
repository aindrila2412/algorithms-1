# Generate all the powersets of a given string 
def generate_powerset(ip, op, final):
    # Base condition to get a final output once the input string is empty
    if ip == "":
        final.append(op)
        return
    # Store the first element of the string and make decisions on it 
    temp = ip[0] 
    # Recursively calling the fnc without including the temp in the output
    generate_powerset(ip[1:], op, final)
    # Recursively calling the fnc including the temp with the output string as output
    generate_powerset(ip[1:], op + temp, final)

s = "abcd"
final = []
generate_powerset(s, "", final)
print(sorted(final))