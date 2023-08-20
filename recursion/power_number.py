def power_number(base, exp):
    assert exp>=0 and int(exp) == exp, "The exponent must be positive integer number"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * power_number(base, exp-1)

print(power_number(-10,3))