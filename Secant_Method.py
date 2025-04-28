def secant(f, a, b, N):
    a_n = a
    b_n = b
    print(f"Iteração 0: a = {a_n}, b = {b_n}")

    for n in range(1, N + 1):
        if f(b_n) - f(a_n) == 0:
            print("Divisão por zero detectada! Método da secante falhou.")
            return None

        m_n = b_n - f(b_n) * (b_n - a_n) / (f(b_n) - f(a_n))

        print(f"Iteração {n}: m = {m_n}, f(m) = {f(m_n)}")

        if abs(f(m_n)) < 1e-8:
            print("Solução exata ou suficientemente próxima encontrada.")
            return m_n

     
        a_n = b_n
        b_n = m_n

    return b_n


if __name__ == "__main__":
    f = lambda x: x ** 2 + x - 6
    a = 1.0
    b = 3.0
    n = 10
    raiz = secant(f, a, b, n)

    if raiz is not None:
        print(f"Raiz aproximada após {n} iterações: {raiz}")
