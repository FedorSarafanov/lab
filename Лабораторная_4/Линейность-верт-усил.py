# -*- coding: UTF-8 -*-

import numpy as np
from pylab import * 
from scipy.interpolate import UnivariateSpline

U_3,h_3=np.array([
    (3,26),  
    (3.5,30),  
    (4,34),    
    ]).T

U_4,h_4=np.array([
    (3,34),  
    (3.5,40),  
    (4,46),    
    ]).T

U_5,h_5=np.array([
    (3,44),  
    (3.5,52),  
    (4,60),    
    ]).T

U_err=2.5*0.01*5
h_err=1

for U,H in [[U_3,h_3],[U_4,h_4],[U_5,h_5]]:
    # func = UnivariateSpline( U, H, k=1)
    func = UnivariateSpline( [0,3.5], [0, H[1]], k=1)
    x=np.linspace(0,4.5,50)
    y = func(x)
    plot( x, y, "--", color='black')    
    # plot( [0,3.5], [0, H[1]], "--", color='black')
    plt.errorbar(U,H, xerr=U_err, yerr=h_err, color='red')
    plt.plot(U,H,color='blue', lw=1)


grid(True)

axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$U$, вольт')
ylabel(r'$h$, мм')

xlim(0)   
ylim(0)        

show()