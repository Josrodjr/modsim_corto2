from random import random

# valores de compra y venta de periodicos
valor_periodico = -1.50
valor_venta = 2.50
valor_devolucion = 0.50

# ventas(int, int)
# Calcula la ganancia de venta de periodicos vendidos dependiendo de
# la cantidad de periodicos comprados diariamente.
def ventas(periodicos, dias):
    dinero = 0

    for i in range(dias):
        luck = random()
        dinero += valor_periodico * periodicos

        if luck < 0.30 or periodicos < 10:
            dinero += valor_venta * 9
            dinero += valor_devolucion * (periodicos - 9)

        elif luck < 0.70 or periodicos < 11:
            dinero += valor_venta * 10
            dinero += valor_devolucion * (periodicos - 10)

        else:
            dinero += valor_venta * 11

    return dinero

# Impresion de datos
print("Ganancias comprando 9 periodicos")
print("1 mes:   " + str(ventas(9,31)))
print("1 año:   " + str(ventas(9,365)))
print("10 años: " + str(ventas(9,3650)))

print("Ganancias comprando 10 periodicos")
print("1 mes:   " + str(ventas(10,31)))
print("1 año:   " + str(ventas(10,365)))
print("10 años: " + str(ventas(10,3650)))

print("Ganancias comprando 11 periodicos")
print("1 mes:   " + str(ventas(11,31)))
print("1 año:   " + str(ventas(11,365)))
print("10 años: " + str(ventas(11,3650)))
