def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def lcm(x, y):
    return x * y // gcd(x, y)

def add_fractions(a, b, c, d):
    common_denominator = lcm(b, d)
    numerator_sum = a * (common_denominator // b) - c * (common_denominator // d)
    common_divisor = gcd(numerator_sum, common_denominator)
    result_numerator = numerator_sum // common_divisor
    result_denominator = common_denominator // common_divisor
    return result_numerator, result_denominator

a = int(input("Введите числитель первой дроби a: "))
b = int(input("Введите знаменатель первой дроби b: "))
c = int(input("Введите числитель второй дроби c: "))
d = int(input("Введите знаменатель второй дроби d: "))
result_numerator, result_denominator = add_fractions(a, b, c, d)
print(f'Разность дробей: {result_numerator}/{result_denominator}')