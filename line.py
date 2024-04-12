import math

def line():

    a = float(input("Ingrese el coeficiente A:"))
    b = float(input("Ingrese el coeficiente B:"))
    x1 = float(input("Ingrese el coeficiente X1:"))
    x2 = float(input("Ingrese el coeficiente X2:"))

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")

    equacion = f"\nPara la siguiente ecuación:\n\tY = {a}X + {b}"
    print(equacion)

    y1 = a*x1 + b
    y2 = a*x2 + b

    P1 = {x1, y1}
    P2 = {x2, y2}

    print(f"\nDados los siguientes puntos:\n\tP1 ({x1}, {y1})\n\tP2 ({x2}, {y2})")

    dist = (math.dist(P1, P2))
    print(f"\nLa distancia entre ellos es: {dist}")
