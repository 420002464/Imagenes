import numpy as np
from math import floor

def W(x, y):
    s = 0
    for i in range(1, 41):
        superficial = -3*(np.cos(28**(i)*25**(-i)*(np.cos(2*i)*x+np.sin(2*i)*y)+2*np.sin(5*i))**2 * np.cos(28**(i) * 25**(-i) * (np.cos(2*i)*y - np.sin(2*i)*x) + 2*np.sin(6*i))**2 - 97/100)
        medio = - np.exp(superficial)
        base = np.exp(medio)
        s += base
    return s

def Q(s, x, y):
    return np.arctan(np.tan(2*(np.cos(5*s)*x + np.sin(5*s)*y + 2*np.cos(4*s)) + (3*np.cos(18*x + 15*y + 4*s))/(200)))

def P(s, x, y):
    return np.arctan(np.tan(2*np.sin(5*s)*x - 2*np.cos(5*s)*y + 3*np.cos(5*s) + (3*np.cos(14*x -19*y + 5*s))/(200)))

def E(t, s, x, y):
    return (1000)/(np.sqrt(20)) * Q(s, x, y) * np.sqrt(5 * abs(20 - 20*(1 - 2*t)*P(s, x, y) - 27*t)) * pow(1 + 50*np.sqrt(abs(4*(200-(20*(1-2*t)*P(s, x, y)+27*t)**2))),-1)

def R(t, s, x, y):
    superficial = - np.exp(1000 * (abs(E(t, s, x, y)) - 1))
    return E(t, s, x, y) * np.exp(superficial)

def N(s, x, y):
    primer_sumando = -np.exp(100*(P(s, x, y) -37/50 - (3/20 + (np.cos(8*Q(s, x, y)+5*s))/(10))*np.cos((10+3*np.cos(16*s))*np.arccos(R(1, s, x, y)) + 3/10*np.cos(38*x-47*y+np.cos(19*x)) + 2*np.cos(4*s))))
    segundo_sumando = -np.exp(-1000 * (P(s, x, y) - 71/100 - pow(3/2 * Q(s, x, y),8)))
    base_exponente = primer_sumando + segundo_sumando
    return np.exp(base_exponente)

def M(s, x, y):
    return np.exp(
            -np.exp(
                -100*(
                    P(s, x, y) - 57/100 -(
                                            3/20 + (np.cos(7*Q(s, x, y) + 2*s))/(10)
                    ) * np.cos((10 + 3*np.cos(14*s))*np.arccos(R(0, s, x, y)) + 3/10*np.cos(45*x + 47*y + np.cos(17*x)) + 2*np.cos(5*s)
            )
        )
    )
            -np.exp(
                1000*(
                    P(s, x, y) - 18/25 + pow(3/2*Q(s, x, y),8)
                )
            )
    )
