# Square Every Digit
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer 

def square_digits(number):
    user_input = str(input('Enter a number: '))
    num_list = list(user_input)

    def square_num(num): 
        return int(num) ** 2

    squared_list = map(square_num, num_list)
    s = [str(i) for i in squared_list]
    result = int(''.join(s))
    return result


# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    new_array = []
    
    if len(iterable) <= 1:
        if len(iterable) == 1:
            new_array.append(iterable)
            return new_array
        else:
            return new_array
    
    index = 1
    for item in iterable:
    
        if index > len(iterable) - 1:
            break
    
        if item != iterable[index]:
            new_array.append(item)
            index += 1
    
        else:
            index += 1
            continue

    new_array.append(iterable[len(iterable) - 1])
    return new_array
