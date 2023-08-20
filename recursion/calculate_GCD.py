def calculate_GCD(first_number, second_number):
    assert int(first_number) == first_number and int(second_number) == second_number, "The numbers must be an integers only"
    if first_number < 0:
        first_number *= -1
    if second_number < 0:
        second_number *= -1
    if second_number == 0:
        return first_number
    new_second_number = int(first_number % second_number)
    return calculate_GCD(second_number, new_second_number)

print(calculate_GCD(-48,-18))