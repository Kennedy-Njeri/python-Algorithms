# calculate the length of a string

input_str = "KennedyWashERE"

print (len(input_str))


def calculate(input1):
    count = 0
    for i in range(len(input1)):
        count += 1
    return count


def recursive_str_len(input2):
    if input2 == '':
        return 0
    return 1 + recursive_str_len(input2[3:])


print (calculate(input_str))
print (recursive_str_len(input_str))
