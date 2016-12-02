# -*- coding: UTF-8 -*-

import numpy as np
from pylab import * 
from scipy.interpolate import UnivariateSpline

def divide(a,b):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide(a,b)
        c[c == np.inf] = 0
        c = np.nan_to_num(c)
        return c

hp_1,tp_1=np.array([
    (0, 7.219),
    (5, 8.011), 
    (10,8.703),
    (15,9.428),
    (20,10.096),
    (25,10.829),
    (30,11.520),
    (35,12.197),
    (40,12.989),
    (45,13.651),
    (50,14.327),
    (55,15.033),
    (60,15.791),
    (65,16.549),
    (70,17.307),
    ]).T

hp_2,tp_2=np.array([
    (0, 5.432),
    (5, 6.297),  
    (10,7.031),
    (15,7.697),
    (20,8.397), 
    (25,9.063),
    (30,9.730),
    (35,10.429),
    (40,11.063),
    (45,11.829),
    (50,12.529),
    (55,13.262),
    (60,14.028),
    (65,14.795),
    (70,15.594)
    ]).T

hp_3,tp_3=np.array([
    (0, 4.365),
    (5, 5.198),
    (10,5.898),
    (15,6.631),
    (20,7.297),
    (25,7.930),
    (30,8.597),
    (35,9.296),
    (40,10.030),
    (45,10.763),
    (50,11.462),
    (55,12.229),
    (60,12.995),
    (65,13.728),
    (70,14.495)
    ]).T

hp_4,tp_4=np.array([
    (0, 7.397),
    (5, 8.230),
    (10,8.963),
    (15,9.696),
    (20,10.396),
    (25,11.063),
    (30,11.696),
    (35,12.395),
    (40,13.062),
    (45,13.762),
    (50,14.495),
    (55,15.194),
    (60,15.961),
    (65,16.727),
    (70,17.494)
    ]).T

hs_1,ts_1=np.array([
    (0, 10.596),
    (5, 10.896),
    # (10,),
    (15,11.429),
    (20,11.629),
    (25,11.829),
    (30,12.029),
    (35,12.296),
    (40,12.529),
    (45,12.795),
    (50,13.029),
    (55,13.295),
    (60,13.575),
    (65,13.828),
    (68,13.995)
    ]).T

hs_2,ts_2=np.array([
    (0, 0.066),
    (5, 0.433),
    (10,0.699),
    (15,0.933),
    (20,1.166),
    (25,1.399),
    (30,1.642),
    (35,1.879),
    (40,2.132),
    (45,2.365),
    (50,2.612),
    (55,2.875),
    (60,3.132),
    (65,3.398),
    (70,3.632)
    ]).T

hs_3,ts_3=np.array([
    (0, 6.597),
    (5, 6.911),
    (10,7.164),
    (15,7.430),
    (20,7.664),
    (25,7.897),
    (30,8.130),
    (35,8.363),
    (40,8.597),
    (45,8.830),
    (50,9.096),
    (55,9.330),
    (60,9.596),
    (65,9.830),
    (70,10.096)
    ]).T

hs_5,ts_5=np.array([
    (0, 5.831),
    (1, 5.898),
    (2, 5.964),
    (3, 6.019),
    (4, 6.064),
    (5, 6.121),
    (10,6.364),
    (15,6.611),
    (20,6.864),
    (25,7.097),
    (30,7.340),
    (35,7.587),
    (40,7.830),
    (45,8.064),
    (50,8.330),
    (55,8.563),
    (60,8.815),
    (65,9.063),
    (70,9.296)
    ]).T

hp_6,tp_6=np.array([
    (0, 3.968),
    (1, 4.165),
    (2, 4.331),
    (3, 4.475),
    (4, 4.631),
    (5, 4.765),    
    (6, 4.898),
    (7, 5.064),
    (8, 5.198),
    (9, 5.364),
    (10,5.498),
    (15,6.197),
    (20,6.897),
    # (25,),
    # (30,),
    # (35,),
    # (40,),
    # (45,),
    # (50,),
    # (55,),
    # (60,),
    # (65,),
    # (70,)
    ]).T

style="-"

def v(t,pl,eta):
    pass
    g=981
    R=4.63
    if pl:
        r=5.95/2/10
        m=0.24
    else:
        r=4.02/2/10
        m=0.265
    rho_pl=0.24/(4/3*pi*r**3)
    rho_st=7.8#0.265/(4/3*pi*r**3)
    rho_sr=1.26   

    if pl:
        rho=rho_pl
    else:
        rho=rho_st  

    a=2.72**(-6*pi*eta*t*r/m)
    return 2/9*g*(r**2)*(rho-rho_sr)/eta*(1-a)*(1/(1+2.45*r/R))

vp_1=divide(hp_1,(tp_1-tp_1[0]))
vp_2=divide(hp_2,(tp_2-tp_2[0]))
vp_3=divide(hp_3,(tp_3-tp_3[0]))
vp_4=divide(hp_4,(tp_4-tp_4[0]))

vp_6=divide(hp_6,(tp_6-tp_6[0]))

vs_1=divide(hs_1,(ts_1-ts_1[0]))
vs_2=divide(hs_2,(ts_2-ts_2[0]))
vs_3=divide(hs_3,(ts_3-ts_3[0]))
vs_5=divide(hs_5,(ts_5-ts_5[0]))

t=np.linspace(0,12,1000)
plot(t,v(t, 1,2.13),'--',color='black', lw=2)
plot(t,v(t, 0,2.55),'--',color='blue', lw=2)
#{1+2.4\frac{r}{R}}
# \eta=\frac{2}{9}r^2g\frac{\rho_\text{ш}-\rho_\text{ср}}{v}\cdot\frac{1}

def k(d,v,pl):
    r=(d/2)/10
    R=4.63
    rho_pl=0.24/(4/3*pi*r**3)
    rho_st=0.265/(4/3*pi*r**3)
    rho_sr=1.26
    # print(pl,r/R)
    if pl:
        rho=rho_pl
    else:
        rho=rho_st
    # print(v)
    return 2/9*981*(r**2)*(rho-rho_sr)/v
summ=0
for i in range(1,15):
    a=(k(5.95,vp_1[i],1))
    c=(k(4,vs_2[i],0))
    b=a/c*2.13/2.55
    d=-(50*(-1 + b))/(-217 + 318*b)
    summ+=abs(d)
print(summ/15)
# plot(tp_1-tp_1[0],hp_1, color="blue", label='Пластмасса')
# plot(tp_2-tp_2[0],hp_2, color="red", label='Пластмасса')
# plot(tp_3-tp_3[0],hp_3, color="black", label='Пластмасса')
# plot(tp_4-tp_4[0],hp_4, color="yellow", label='Пластмасса')

# plot(tp_6-tp_6[0],hp_6, 'o-', color="#f1c40f", label='Пластмасса')

# plot(ts_1-ts_1[0],hs_1, style, color="#1abc9c", label='Сталь')
# plot(ts_2-ts_2[0],hs_2, style, color="#f1c40f", label='Сталь')
# plot(ts_3-ts_3[0],hs_3, style, color="#c0392b", label='Сталь')
# plot(ts_5-ts_5[0],hs_5, style, color="#2c3e50", label='Сталь')

plot(tp_1-tp_1[0],vp_1, color="blue", label='Пластмасса')
plot(tp_2-tp_2[0],vp_2, color="red", label='Пластмасса')
plot(tp_3-tp_3[0],vp_3, color="black", label='Пластмасса')
plot(tp_4-tp_4[0],vp_4, color="yellow", label='Пластмасса')

# plot(tp_6-tp_6[0],hp_6, 'o-', color="#f1c40f", label='Пластмасса')
plot(tp_6-tp_6[0],vp_6, '-', color="#f1c40f", label='Пластмасса')


plot(ts_1-ts_1[0],vs_1, style, color="#1abc9c", label='Сталь')
plot(ts_2-ts_2[0],vs_2, style, color="#f1c40f", label='Сталь')
plot(ts_3-ts_3[0],vs_3, style, color="#c0392b", label='Сталь')
plot(ts_5-ts_5[0],vs_5, style, color="#2c3e50", label='Сталь')

# func = UnivariateSpline( hs_5, ts_5-ts_5[0], k=1)
# x=np.linspace(0,70,10)
# y = func(x)
# plot( y, x, "--", color='black')  

# plot([0,ts_5[-1]-ts_5[0]],[0,hs_5[-1]], style, color="red", label='Сталь')

# plot(ts_4-ts_4[0],hs_4, style, color="yellow", label='Сталь')
# legend(loc=0)
# grid(True)

# axhline(y=0, color='black')
# axvline(x=0, color='black')

# rc('text', usetex=True)
# rc('font', family='Droid Sans')
# rc('text.latex',unicode=True)
# rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble=r'\usepackage[russian]{babel}')

# xlabel(r'$t$, с')
# ylabel(r'$h$, см')

# xlim(0,1.5)   
# ylim(0,10)        
savefig(r'two.png')
show()
