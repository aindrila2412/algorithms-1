# Print N-bit binary numbers having more 1s than 0s
def get_binary(output_num, num_0, num_1, n):
    if len(output_num) == n:
        final.insert(0, output_num)
        return
    if num_1 > num_0:
        get_binary(output_num + '0', num_0 + 1, num_1, n)
    get_binary(output_num + '1', num_0, num_1 + 1, n)


final = []
get_binary("", 0, 0, 4)
print(final)