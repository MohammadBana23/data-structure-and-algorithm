def sum_digits_in_integer(integer):
    assert integer>=0 and int(integer) == integer, "You must enter integer and positive number"
    first_remainder = integer % 10
    if integer == 0:
        return 0
    else:
        return int(first_remainder) + sum_digits_in_integer(int(integer/10))
    
print(sum_digits_in_integer(129))