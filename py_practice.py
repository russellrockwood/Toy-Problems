# Square Every Digit
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer 

user_input = str(input('Enter a number: '))
num_list = list(user_input)

def square_digits(num): 
    return int(num) ** 2

squared_list = map(square_digits, num_list)
s = [str(i) for i in squared_list]
result = int(''.join(s))

print(result)

