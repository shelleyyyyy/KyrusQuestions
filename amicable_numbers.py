current_try = 10000

amicable_pairs = []


def get_sum(num):
    sum = 0
    divisor = 1

    for i in range(num - 1):
        attempt = num / divisor
        check = attempt.is_integer()
        if check:
            sum = sum + divisor

        divisor = divisor + 1

    return sum


def create_data(num1, num2):
    global amicable_pairs
    data = [num1, num2]
    amicable_pairs.append(data)


def get_total_with_perfect():
    global amicable_pairs
    final = 0
    for i in amicable_pairs:
        final = final + i[0]

    return final


def get_total():
    global amicable_pairs
    final = 0
    for i in amicable_pairs:
        if i[0] == i[1]:
            continue
        final = final + i[0]

    return final


while current_try > 0:
    attempt = get_sum(current_try)
    attempt_pt2 = get_sum(attempt)

    if current_try == attempt_pt2:
        create_data(current_try, attempt)

    current_try = current_try - 1

print("sum including perfect numbers: ", get_total_with_perfect())
print("sum without perfect numbers: ", get_total())
