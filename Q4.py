def buggy_function(x):
    is_even = (x % 2 == 0)

    if type(x) != int:
        return False

    if x <= 10:
        if is_even:
            return True
    if x > 10:
        if not is_even:
            return True
    return False

      
test = buggy_function(14)
print(test)
