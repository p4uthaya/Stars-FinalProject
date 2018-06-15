# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:36:39 2017

@author: Prabha
"""
import numpy as np
pi = np.pi
sqrt = np.sqrt
mp = 1.6726219e-27                        # Mass of proton
me = 9.10938356e-31                       # Mass of electron
hbar = 1.0545718e-34                      # Reduced Planck const
k = 1.38064852e-23                        # Boltzmann const
a = 7.5657e-16                            # Radiation const
G = 6.67408e-11                           # Gravitational const
Rsun = 6.967e8                            # Radius of Sun
Msun = 1.989e30                           # Mass of Sun
SB=5.67e-8                                # Stefan Boltzmann const
gamma=5.0/3.0                             # Gamma
c=2.998*(10.0**8.0)                       #Speed of Light


# Mass fractions
X = 0.7
Y = 0.28
Z = 0.02

# Mean Molecular Weight
mu = ((2*X) + (0.75*Y) + (0.5*Z) )**(-1)


# functions

def dTdr (r,M,T,P,p,L,tau,kappa):

    Tcon = (1.0-(1.0/gamma))*((T*G*M*p)/(P*(r**2.0)))
    Trad = (3.0*p*kappa*L)/(16*pi*a*c*(T**3.0)*(r**2.0))
    # if T < 0.0:
    #print 'In Function GOOF UP'
    #print 'Tcon: ', Tcon
    #print 'Trad: ', Trad
    # print 'Tcon, Trad: ', Tcon, Trad
    # print 'min(Tcon, Trad: )', min(Tcon,Trad)
    Tmin = min(Tcon,Trad)
    # print 'Tmin: ', Tmin
    dTdrvalue = (-1.0)*Tmin
    return dTdrvalue


def dpdr (r,M,T,P,p,L,tau,kappa):
    dPdp = (((3.0*(pi**2.0))**(2.0/3.0))/3.0*((hbar**2.0)/(mp*me))*((p/mp)**(2.0/3.0)))+((k*T)/(mu*mp))
    dPdT = ((p*k)/(mu*mp))+((4.0/3.0)*a*T**3.0)
    dpdrvalue = (-1.0)*((G*M*p/(r**2))+(dPdT*dTdr(r,M,T,P,p,L,tau,kappa)))/(dPdp)
    return dpdrvalue

def dMdr (r,M,T,P,p,L,tau,kappa,dr):
    dMdrvalue = 4.0*pi*(r**2.0)*p
    return dMdrvalue

def dLdr (r,M,T,P,p,L,tau,kappa):
    Epp = (1.07*(10.0**(-7.0)))*p*(10.0**(-5.0))*(X**2.0)*((T*(10.0**(-6.0)))**4.0)
    Ecno = (8.24*(10.0**(-26.0)))*(p*(10.0**(-5.0)))*0.03*(X**2.0)*((T*(10.0**(-6.0)))**19.9)
    E=Epp+Ecno
    dLdrvalue = 4.0*pi*(r**2.0)*p*E
    return dLdrvalue

def dtaudr (r,M,T,P,p,L,tau,kappa):
    dtaudrvalue = kappa * p
    return dtaudrvalue

def Pt(r,M,T,P,p,L,tau,kappa):
    Ptvalue = ((((3.0*(pi**2.0))**(2.0/3.0))/5.0)*((hbar**2.0)/me)*((p/mp)**(5.0/3.0)))+((p*k*T)/(mu*mp))+((1.0/3.0)*a*(T**4.0))
    return Ptvalue 

def dPdr(r,M,T,P,p,L,tau,kappa):
    dPdrvalue = -G*M*p/r**2.0
    return dPdrvalue

