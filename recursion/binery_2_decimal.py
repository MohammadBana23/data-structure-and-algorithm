def binary_to_decimal(number):
    assert int(number) == number, "You must enter a integer number"
    if number == 0:
        return 1
    else:
        return number%2 + 10*binary_to_decimal(int(number/2))


print(binary_to_decimal(1))