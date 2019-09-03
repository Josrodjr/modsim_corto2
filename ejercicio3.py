import math
from random import random

# hotel cashflow (tuples necesitan la normal)
hotel = [-800,(-800,50),(-800,100),(-700,150),(300,200),(400,200),(500,200),\
(200,8440)]

# centro comercial cashflow (tuples necesitan la normal)
center = [-900,(-600,50),(-200,50),(-600,100),(250,150),(350,150),(400,150),\
(1600,6000)]

# normal(int, int, float)
# se usa para calcular una variable aleatorea con distribucion normal.
def normal(mu, sigma, lamb):
    while True:
        y1 = -(1 / lamb)*math.log(random())
        y2 = -(1 / lamb)*math.log(random())
        if y2 -((y1-1)**2)/2 > 0:
            y = y2 -((y1-1)**2)/2
            u = random()
            if u <= 0.5:
                return mu + sigma * y1
            else:
                return mu - sigma * y1

# net present value (NPV)
# npv(array, float)
# calula el valor presente neto dado un cashflow y un rate.
def npv(cashflow, rate):
    final_npv = 0
    for i in range(len(cashflow)):
        final_npv += cashflow[i]/(1+rate)**(i+1)

    return final_npv

# total_npv_overtime(array, float, int)
# calcula el npv dado un cashflow de un proyecto y un rate para el npv, esto
# lo hace varias veces segun las repeticiones requeridadas y devuelve el npv
# promedio
def total_npv_overtime(proyect, npv_rate, reps):

    total_npv = 0
    for i in range(reps):

        cashflow = []
        for i in range(len(proyect)):
            if i == 0:
                cashflow.append(proyect[i])
            else:
                cashflow.append(normal(proyect[i][0], proyect[i][1], 1))

        total_npv += npv(cashflow, npv_rate)

    total_npv /= reps

    return total_npv

print("Pryecto Hotel")
print("NPV 10^2 reps: " + str(total_npv_overtime(hotel, 0.10, 100)))
print("NPV 10^3 reps: " + str(total_npv_overtime(hotel, 0.10, 1000)))
print("NPV 10^4 reps: " + str(total_npv_overtime(hotel, 0.10, 10000)))

print("Pryecto Centro Comercial")
print("NPV 10^2 reps: " + str(total_npv_overtime(center, 0.10, 100)))
print("NPV 10^3 reps: " + str(total_npv_overtime(center, 0.10, 1000)))
print("NPV 10^4 reps: " + str(total_npv_overtime(center, 0.10, 10000)))
