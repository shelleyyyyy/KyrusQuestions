
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

        answer_1 = 9
        answer_2 = 11
        answer_3 = 50
        

        def check_answer(a_, b_, c_, d_, e_, f_, g_):
            equation_1 = a * b + b
            equation_2 = c - a + b
            equation_3 = c * a * d

            if equation_1 == answer_1 and equation_2 == answer_2 and equation_3 == answer_3:
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
