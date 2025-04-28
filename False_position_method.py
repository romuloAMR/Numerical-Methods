def f(x):
    return x ** 2 + x - 6


def falsePosition(x0, x1, e):
    passo = 1
    while True:
        f0 = f(x0)
        f1 = f(x1)
        x2 = (x0 * f1 - x1 * f0) / (f1 - f0)
        f2 = f(x2)

        print(f"Iteração-{passo}, x2 = {x2:.10f}, f(x2) = {f2:.10f}")

        if abs(f2) < e:
            print(f"\nA raiz encontrada é: {x2:.10f}")
            break

        if f0 * f2 < 0:
            x1 = x2
        else:
            x0 = x2

        passo += 1


if __name__ == "__main__":
    x0 = 1.0
    x1 = 3.0
    h = 0.4
    e = 1e-8

    falsePosition(x0, x1, e)
