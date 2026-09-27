import numpy as np
from math import floor

def A(k, x, y):
    first_part = x + np.cos(k**3 + 1/5)
    first_sine = np.sin((3 + 3*np.sin(k))*y + np.cos(2*k**4) + 1 )
    second_sine = np.sin(10*y + 2/5*np.sin(25*x) + 4*np.sin(5*x + 2*np.cos(k**2))*np.sin(2*y))
    second_part = 1/10*first_sine*second_sine
    return first_part + second_part

def G(x, y):
    s = 0
    for i in range(1, 51):
        exponente = 500*((A(i, x, y))**2 - 1/100*(1-y-1/10*np.sin(8*x))*(9/10 + np.sin(10*y + i**2 + 1)))
        exponente_seguro = np.clip(exponente, -2000, 2000)
        u = -np.exp(exponente_seguro)
        s += 2*np.exp(u)*(1/2000 + 2*abs(A(i, x, y))**(29/10))
    return 30*s


def R(x, y):
    s = 0
    for i in range(1, 51):
        exponente = 500*((A(i, x, y))**2 - 1/100*(1-y-1/10*np.sin(8*x))*(9/10 + np.sin(10*y + i**2 + 1)))
        exponente_seguro = np.clip(exponente, -2000, 2000)
        u = -np.exp(exponente_seguro)
        s += 2*np.exp(u)*(1/2000 + 2*abs(A(i, x, y))**(29/10))
    return 60*s

def F(x):
    return floor(255 * np.exp(-np.exp(-1000*x)) * abs(x)**(np.exp(-np.exp(1000*(x-1)))))

def primera(m, n):
    Dentro = R((m-900)/(500), (601-n)/(500))
    return F(Dentro)

def segunda(m, n):
    Dentro = G((m-900)/(500), (601-n)/(500))
    return F(Dentro)

#[[(F(R((m-900)/(500), (601-n)/(500))), F(G((m-900)/500, (601-n)/(500))),0) for n in range(1, 1201)] for m in range(1, 1801)]#
#[[(primera(m,n), segunda(m,n), 0) for n in range(1, 1201)] for m in range(1, 1801)]

R((1-900)/(500), (601-1)/(500))
