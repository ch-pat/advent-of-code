input_file = "2021/03/input"

with open(input_file, "r") as f:
    data = f.read().splitlines()
data = [x for x in data]

def binary_arr_to_int(arr):
    integer_value = 0
    for i, value in enumerate(arr):
        integer_value += value * 2**i
    return integer_value


def get_least_most_common_bits(data, least=False):
    bit = 0 if least else 1
    length = len(data[0])
    frequencies = [0 for x in data[0]]
    for line in data:
        for i, char in enumerate(line):
            if char == "1":
                frequencies[i] += 1
            else:
                frequencies[i] -= 1
    return [bit if frequencies[i] >= 0 else 1 - bit for i in range(len(frequencies))]


gamma_rate = get_least_most_common_bits(data)
epsilon_rate = get_least_most_common_bits(data, least=True)
print(gamma_rate)
print(epsilon_rate)

integer_gamma_rate = binary_arr_to_int(reversed(gamma_rate))
integer_epsilon_rate = binary_arr_to_int(reversed(epsilon_rate))

print(integer_epsilon_rate * integer_gamma_rate)
print("### Part Two ###")

def filter_elements_by_bit_at_position(arr, value, index):
    """Returns arr without elements that have `value` at `index`"""
    return [x for x in arr if x[index] == str(value)]

def filter_by_bit_criteria(data, least=False):
    for index in range(len(data[0])):
        criteria = get_least_most_common_bits(data, least)
        value = criteria[index]
        data = filter_elements_by_bit_at_position(data, value, index)
        #print("Filtered by criteria ", criteria, " kept numbers with ", value, " at index ", index)
        #print(data)
        if len(data) == 1:
            return data
        
oxygen = data[:]
co2 = data[:]
oxygen = filter_by_bit_criteria(oxygen)
co2 = filter_by_bit_criteria(co2, least=True)
oxygen = [int(x) for x in oxygen[0]]
co2 = [int(x) for x in co2[0]]
print(oxygen)
print(co2)

integer_oxygen = binary_arr_to_int(reversed(oxygen))
integer_co2 = binary_arr_to_int(reversed(co2))

print(integer_oxygen * integer_co2)
