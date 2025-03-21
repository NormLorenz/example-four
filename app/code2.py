input_string = 'How are you 1?  How are you 2?  '

# split a string into multiple parts using a separator
def split_strings(input, separator):
    result = []
    if separator in input:
        parts = input.split(separator)
        if len(parts) == 3:
            parts[0] = (parts[0] + separator).strip()
            parts[1] = (parts[1] + separator).strip()
            result = parts
    return result


output = split_strings(input_string, '?')
print(output)

# output3 = split_strings(input_string, '.')
# print(output3)
# print(len(output3))
# if len(output3) == 3:
#     print(output3[0] + '.')
#     print(output3[1] + '.')
#     print(output3[2] + '.')
# else:
#     print("output3 is empty.")
