def Bisection_Method(equation, a, b, given_error): # function, boundaries, Es

    li_a = deque() # a
    li_b = deque() # b
    li_c = deque() # x root -> c
    li_fc = deque() # f(xr)
    li_fa = deque() # f(a)
    li_fb = deque() # f(b)
    li_Ea = deque() # estimated error

    data = {
        'Xl': li_a,
        'Xu': li_b,
        'Xr': li_c,
        'f(Xl)': li_fa,
        'f(Xu)': li_fb,
        'f(Xr)': li_fc,
        'Ea%': li_Ea,
    }

    global c

    def f(x):
        F = eval(equation) # the x here when we f(a) a will be instead of x
        return F

    # substitute boundaries in function
    if f(a)*f(b) >= 0:
        print('Error', 'Bisection method is fail')
        quit()

    # elif we have a different sign
    else:
        Estimated_Error = 0

        while Estimated_Error/100 <= given_error:
            c = (a + b) / 2
            if Estimated_Error == 0:
                li_a.append(a)
                li_b.append(b)
                li_c.append(c)
                li_fa.append(f(a))
                li_fb.append(f(b))
                li_fc.append(f(c))
                li_Ea.append(None)
                pass

            if f(a)*f(c) < 0:
                b = c
                c1 = (a + b)/2
                Estimated_Error = abs((c1 - c)/c1) * 100 # b became the old root and c1 became the new root ((current - previous)/current) * 100

            elif f(b)*f(c) < 0:
                a = c
                c1 = (a + b) / 2
                Estimated_Error = abs((c1 - c) / c1) * 100

            else:
                print('Error', 'something is wrong!')

        else:
            while Estimated_Error/100 >= given_error:
                c = (a + b) / 2

                #append data to to the list

                li_a.append(a)
                li_b.append(b)
                li_c.append(c)
                li_fa.append(f(a))
                li_fb.append(f(b))
                li_fc.append(f(c))
                li_Ea.append('%.5f' % Estimated_Error+'%')

                if f(a) * f(c) < 0:
                    b = c
                    c1 = (a + b) / 2
                    Estimated_Error = abs((c1 - c) / c1) * 100  # b became the old root and c1 became the new root ((current - previous)/current) * 100
                elif f(b) * f(c) < 0:
                    a = c
                    c1 = (a + b) / 2
                    Estimated_Error = abs((c1 - c) / c1) * 100

                else:
                    print('Error', 'something is wrong!')
            else:
                c = (b + a)/2

                li_a.append(a)
                li_b.append(b)
                li_c.append(c)
                li_fa.append(f(a))
                li_fb.append(f(b))
                li_fc.append(f(c))
                li_Ea.append('%.5f' % Estimated_Error+'%')

                print(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=True))

if __name__ == '__main__':
    from tabulate import tabulate
    from collections import deque

    print('\n The first case👇 \n')

    Bisection_Method('(5 * x ** 3) - (5 * x ** 2) + 6 * x - 2', 0, 1, 10/100)

    print('\n The second case👇 \n')

    Bisection_Method('(5 * x ** 3) - (5 * x ** 2) + 6 * x - 2', 0, 5, 10 / 100)
