
# answer
# 2, 3, 5, 7, 11, 13, 17

import sys
import threading

start_a = 1
g_ceiling = 20


class thread_(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        global start_a, g_ceiling

        ceiling = g_ceiling

        floor = 1

        a = start_a
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
                sys.exit(0)

        def show_try(a_, b_, c_, d_, e_, f_, g_):
            print(a_, ", ", b_, ", ", c_, ", ", d_, ", ", e_, ", ", f_, ", ", g_)

        while True:
            check_answer(a, b, c, d, e, f, g)
            # show_try(a, b, c, d, e, f, g)

            if a == ceiling:
                print("no values found to satisfy all equations :(")

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


for i in range(1, g_ceiling):
    new_thread = thread_(i)
    
    new_thread.start()

    start_a += 1
