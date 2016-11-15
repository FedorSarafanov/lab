from math import *
import matplotlib.pyplot as plt
import numpy as np
# vert=0
# L=0.016 			# Длина пластин
# d=0.0055 			# Расстояние между пластинами

L=0.163				# От анода до экрана
eta=1.758*(10**11)	# Известное e/m
U_a=1700			# Напряжение второго анода

Bz_g=0.186*10**(-5)
Bz_g=0.0000186
Bz=Bz_g/cos(70*pi/180)

# Bz_perp=Bz*sin(6*pi/180)
alpha=3*pi/180
# omega=eta*Bz_perp			# Циклотронная частота

def H(alpha):
	u=1000
	v0z=np.sqrt(eta*2*u)	# Скорость по вылете из пластин
	tau=L/v0z 			# Время пролета в трубке
	R=(v0z/np.cos(alpha))/(eta*Bz)

	h=L**2/(2*R)
	h=R-np.sqrt(R**2-L**2)
	print(h)
	v_l=v0z*np.sin(alpha)
	left=v_l*tau*np.cos(alpha)
	print(left)
	return np.sqrt(h**2+left**2)


def h(U):
	return Bz*np.sqrt(eta*(L**4)/(8*U))


# U=np.linspace(1000,2000,100)
# hh=H(U)
A=np.linspace(0.0001,pi/3,100)
aa=H(A)

plt.plot(A, aa, alpha=0.7,color='blue')
# plt.plot(U, h(U), alpha=0.7,color='blue')

# plt.plot(U, hh, alpha=0.7,color='red')
# plt.plot(1300, 0.007, marker="^", alpha=0.7,color='blue')
# plt.plot(1300, 0.006, marker="^", alpha=0.7,color='blue')
# plt.plot(1700, 0.005, marker="^", alpha=0.7,color='blue')
# plt.plot(1700, 0.0065, marker="^", alpha=0.7,color='blue')

# plt.plot(np.linspace(, hh, alpha=0.7,color='red')

plt.show()