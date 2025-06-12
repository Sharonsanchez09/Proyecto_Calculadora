def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def potencia(base, exponente):
    resultado = 1
    for _ in range(abs(exponente)):
        resultado *= base
    return resultado if exponente >= 0 else 1 / resultado

def exp(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        resultado += potencia(x, n) / factorial(n)
    return resultado

def sin(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        signo = -1 if n % 2 else 1
        resultado += signo * potencia(x, 2 * n + 1) / factorial(2 * n + 1)
    return resultado

def cos(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        signo = -1 if n % 2 else 1
        resultado += signo * potencia(x, 2 * n) / factorial(2 * n)
    return resultado

def arcsin(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        numerador = factorial(2 * n) * potencia(x, 2 * n + 1)
        denominador = potencia(4, n) * potencia(factorial(n), 2) * (2 * n + 1)
        resultado += numerador / denominador
    return resultado

def arccos(x, terminos=20):
    from funciones import pi
    return pi()/2 - arcsin(x, terminos)

def sinh(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        resultado += potencia(x, 2 * n + 1) / factorial(2 * n + 1)
    return resultado

def cosh(x, terminos=20):
    resultado = 0
    for n in range(terminos):
        resultado += potencia(x, 2 * n) / factorial(2 * n)
    return resultado

def pi(terminos=1000):
    resultado = 0
    for k in range(terminos):
        resultado += (-1)**k / (2 * k + 1)
    return 4 * resultado
