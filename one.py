import time

ceiling = 20

a = ceiling
b = ceiling
c = ceiling
d = ceiling
e = ceiling
f = ceiling
g = ceiling

counter = 0

a_counter = 0
b_counter = 0
c_counter = 0
d_counter = 0
e_counter = 0
f_counter = 0
g_counter = 1

matrix = []

answer_1 = 5100
answer_2 = 33462
answer_3 = 17150
answer_4 = 914760


def print_matrix():
    for i in matrix:
        print(i)


def check_answer(a_, b_, c_, d_, e_, f_, g_):
    equation_1 = pow(a_, 2) * b_ * pow(c_, 2) * g_
    equation_2 = a_ * pow(b_, 2) * e_ * pow(f_, 2)
    equation_3 = a_ * pow(c_, 2) * pow(d_, 3)
    equation_4 = pow(a_, 3) * pow(b_, 3) * c_ * d_ * pow(e_, 2)

    if equation_1 == answer_1 and equation_2 == answer_2 and equation_3 == answer_3 and equation_4 == answer_4:
        print("Success!!!!!! --------------------------------")
        show_try(a_, b_, c_, d_, e_, f_, g_)
        exit(0)
    # else:
    #     print('fail')


def show_try(a_, b_, c_, d_, e_, f_, g_):
    print(a_, ", ", b_, ", ", c_, ", ", d_, ", ", e_, ", ", f_, ", ", g_)


while True:
    check_answer(a, b, c, d, e, f, g)
    show_try(a, b, c, d, e, f, g)
    counter = counter + 1
    # time.sleep(.1)

    if a_counter == pow(ceiling, 6):
        if a <= 0:
            print("FAIL, No values satisfied all equations")
            exit(0)

        a = a - 1
        a_counter = 0

    if b_counter == pow(ceiling, 5):
        if b == 0:
            b = ceiling
            continue
        b = b - 1
        b_counter = 0

    if c_counter == pow(ceiling, 4):
        if c == 0:
            c = ceiling
            continue
        c = c - 1
        c_counter = 0

    if d_counter == pow(ceiling, 3):
        if d == 0:
            d = ceiling
            continue
        d = d - 1
        d_counter = 0

    if e_counter == pow(ceiling, 2):
        if e == 0:
            e = ceiling
            continue
        e = e - 1
        e_counter = 0

    if f_counter == pow(ceiling, 1):
        if f == 0:
            f = ceiling
            continue
        f = f - 1
        f_counter = 0

    if g_counter == pow(ceiling, 0):
        if g == 0:
            g = ceiling
            continue
        g = g - 1

    a_counter = a_counter + 1
    b_counter = b_counter + 1
    c_counter = c_counter + 1
    d_counter = d_counter + 1
    e_counter = e_counter + 1
    f_counter = f_counter + 1
