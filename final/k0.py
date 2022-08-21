
# answer
# 2, 3, 5, 7, 11, 13, 17

ceiling = 30

floor = 1

a = floor # state
b = floor # america
c = floor # cloud
d = floor # aws

answer_1 = 9
answer_2 = 2
answer_3 = 50


def check_answer(a_, b_, c_, d_):
    equation_1 = a * b + b
    equation_2 = c - a + b
    equation_3 = c * a * d

    if equation_1 == answer_1 and equation_2 == answer_2 and equation_3 == answer_3:
        print("Success!!!!!! --------------------------------")
        show_try(a_, b_, c_, d_)
        exit(0)


def show_try(a_, b_, c_, d_):
    print(a_, ", ", b_, ", ", c_, ", ", d_)
    print("state: ", a_)
    print("america: ", b_)
    print("cloud: ", c_)
    print("aws: ", d_)
    
    print("america * aws + state + cloud = ", b_ * d_ + a_ + c_)


while True:
    check_answer(a, b, c, d)
    # show_try(a, b, c, d)

    if a == ceiling and d == ceiling:
        print("no values found to satisfy all equations :(")
        exit(0)

    if b == ceiling:
        a = a + 1
        b = 1

    if c == ceiling:
        b = b + 1
        c = 1

    if d == ceiling:
        c = c + 1
        d = 1

    d = d + 1
