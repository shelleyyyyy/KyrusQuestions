ceiling = 20

floor = 1

a = floor
b = floor
c = floor
d = floor
e = floor
f = floor
g = floor

answer_1 = 5100
answer_2 = 33462
answer_3 = 17150
answer_4 = 914760


def check_answer(a_, b_, c_, d_, e_, f_, g_):
    equation_1 = pow(a_, 2) * b_ * pow(c_, 2) * g_
    equation_2 = a_ * pow(b_, 2) * e_ * pow(f_, 2)
    equation_3 = a_ * pow(c_, 2) * pow(d_, 3)
    equation_4 = pow(a_, 3) * pow(b_, 3) * c_ * d_ * pow(e_, 2)

    if equation_1 == answer_1 and equation_2 == answer_2 and equation_3 == answer_3 and equation_4 == answer_4:
        print("Success!!!!!! --------------------------------")
        show_try(a_, b_, c_, d_, e_, f_, g_)
        exit(0)


def show_try(a_, b_, c_, d_, e_, f_, g_):
    print(a_, ", ", b_, ", ", c_, ", ", d_, ", ", e_, ", ", f_, ", ", g_)


while True:
    check_answer(a, b, c, d, e, f, g)
    show_try(a, b, c, d, e, f, g)
    # time.sleep(.1)

    if a == ceiling:
        print("no values found to satisfy all equations :(")

    if b == ceiling:
        a = a + 1
        b = 1

    if c == ceiling:
        b = b + 1
        c = 1

    if d == ceiling:
        c = c + 1
        d = 1

    if e == ceiling:
        d = d + 1
        e = 1

    if f == ceiling:
        e = e + 1
        f = 1

    if g == ceiling:
        f = f + 1
        g = 1

    g = g + 1
