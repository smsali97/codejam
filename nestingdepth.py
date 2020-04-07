T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int,input()))
    balanced_string = ''
    max_no = -1
    for number in numbers:
        if max_no is -1:
            max_no = number
            balanced_string += max_no*'(' + str(number)
        elif number < max_no:
            balanced_string += (max_no - number)*')' + str(number) 
            max_no = number
        elif number > max_no:
            balanced_string += (number - max_no)*'(' + str(number)
            max_no = number

        else:
            balanced_string += str(number)
    if max_no is not -1:
        balanced_string += max_no*')'
    print("Case #{}: {}".format(t,balanced_string))
        



