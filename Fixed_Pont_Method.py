def f(x):
    return x * x + x - 6

def g(x):
    return 6 / (x + 1)

def fixedPointIteration(x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteração-%d, x1 = %0.10f e f(x1) = %0.10f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nA raiz aproximada é: %0.10f' % x1)
    else:
        print('\nNão convergiu.')

if __name__ == "__main__":

    start = 1.0
    end = 3.0
    h = 0.4
    e = 1e-8
    N = 1000
    x = start
    while x <= end:
        print("\nIniciando iteração do ponto fixo com chute inicial x0 = %.1f" % x)
        fixedPointIteration(x, e, N)
        x += h
