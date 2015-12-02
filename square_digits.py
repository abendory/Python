def square_digits(num):
    if num < 10: return num**2
    temp = num
    counter = 0
    while temp > 10:
        temp = temp/10
        counter += 1
    digits = []
    digits.append(num % 10)
    i = 10
    while i <= 10**counter:
        digits.append(num % (10*i) / i)
        i *= 10
    for i in range(len(digits)):
        digits[i] = digits[i]**2
    return int(''.join(map(str, reversed(digits))))

print square_digits(9119)
print square_digits(123)
print square_digits(2045)
print square_digits(3299)
print square_digits(1)
print square_digits(0)