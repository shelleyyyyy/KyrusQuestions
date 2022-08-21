answer_1 = 5100
answer_2 = 33462
answer_3 = 17150
answer_4 = 914760


def check_answer(a_, b_, c_, d_, e_, f_, g_):
    equation_1 = pow(a_, 2) * b_ * pow(c_, 2) * g_
    equation_2 = a_ * pow(b_, 2) * e_ * pow(f_, 2)
    equation_3 = a_ * pow(c_, 2) * pow(d_, 3)
    equation_4 = pow(a_, 3) * pow(b_, 3) * c_ * d_ * pow(e_, 2)

    # equation_1 = 5100
    # equation_2 = 33462
    # equation_3 = 17150
    # equation_4 = 914760

    if equation_1 == answer_1 and equation_2 == answer_2 and equation_3 == answer_3 and equation_4 == answer_4:
        show_try(a_, b_, c_, d_, e_, f_, g_)
    else:
        print('fail')


def show_try(a_, b_, c_, d_, e_, f_, g_):
    print(a_, ", ", b_, ", ", c_, ", ", d_, ", ", e_, ", ", f_, ", ", g_)


check_answer(2, 3, 5, 7, 11, 13, 17)
