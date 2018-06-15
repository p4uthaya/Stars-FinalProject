import numpy as np 
from constants import * 

#Emma: This is the Runge-Kutta method, I saved the old Euler one under the name old_euler_starintegration

def starintegration(r,M,T,P,p,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc):#,dkappa):
    # print 'STAR INTEGRATION START'
    Radius = []
    Mass = []
    Temperature = []
    Pressure = []
    Density = []
    Luminosity = []
    Tau = []
    Kappa = []

    i=1
    count = 0
    while deltatau > 2.0/3.0: #or r<695000000 :# and L - 4*pi*SB*Rstar**2.0*T**4.0 : #((tauinfinity - tauRstar) - 2.0/3.0) < 0.01 and 
##    while r<400000000:  #Emma: This can be changed, this number is just so I get a graph without having deltatau reach 2/3
        count+=1
        i+=1
        r += dr
        p += dp 
        T += dT
        M += dM
        L += dL 
        tau += dtau
#       P += dP
        P=Pt(r,M,T,P,p,L,tau,kappa)
        # if T < 0.0: 
        #     print 'YOU DON GOOFED'
        #     print T, dT
        # #     print len(Temperature)
        #     print i
        #     print 'T before: ', Temperature[i-5]

#Emma: Big change not real need for dPdr, he said we only needed to solve 5 equations and we have one for P(p,T) directly.
        
        pk1 = dr*dpdr(r,M,T,P,p,L,tau,kappa)
        Tk1 = dr*dTdr(r,M,T,P,p,L,tau,kappa)
        Mk1 = dr*dMdr(r,M,T,P,p,L,tau,kappa,dr)
        Lk1 = dr*dLdr(r,M,T,P,p,L,tau,kappa)
        tauk1 = dr*dtaudr(r,M,T,P,p,L,tau,kappa)

        pk2 = dr*dpdr(r+0.5*dr,M+0.5*Mk1,T+0.5*Tk1,P,p+0.5*pk1,L+0.5*Lk1,tau+0.5*tauk1,kappa)
        Tk2 = dr*dTdr(r+0.5*dr,M+0.5*Mk1,T+0.5*Tk1,P,p+0.5*pk1,L+0.5*Lk1,tau+0.5*tauk1,kappa)
        Mk2 = dr*dMdr(r+0.5*dr,M+0.5*Mk1,T+0.5*Tk1,P,p+0.5*pk1,L+0.5*Lk1,tau+0.5*tauk1,kappa,dr)
        Lk2 = dr*dLdr(r+0.5*dr,M+0.5*Mk1,T+0.5*Tk1,P,p+0.5*pk1,L+0.5*Lk1,tau+0.5*tauk1,kappa)
        tauk2 = dr*dtaudr(r+0.5*dr,M+0.5*Mk1,T+0.5*Tk1,P,p+0.5*pk1,L+0.5*Lk1,tau+0.5*tauk1,kappa)
    
        pk3 = dr*dpdr(r+0.5*dr,M+0.5*Mk2,T+0.5*Tk2,P,p+0.5*pk2,L+0.5*Lk2,tau+0.5*tauk2,kappa)
        Tk3 = dr*dTdr(r+0.5*dr,M+0.5*Mk2,T+0.5*Tk2,P,p+0.5*pk2,L+0.5*Lk2,tau+0.5*tauk2,kappa)
        Mk3 = dr*dMdr(r+0.5*dr,M+0.5*Mk2,T+0.5*Tk2,P,p+0.5*pk2,L+0.5*Lk2,tau+0.5*tauk2,kappa,dr)
        Lk3 = dr*dLdr(r+0.5*dr,M+0.5*Mk2,T+0.5*Tk2,P,p+0.5*pk2,L+0.5*Lk2,tau+0.5*tauk2,kappa)
        tauk3 = dr*dtaudr(r+0.5*dr,M+0.5*Mk2,T+0.5*Tk2,P,p+0.5*pk2,L+0.5*Lk2,tau+0.5*tauk2,kappa)

        pk4 = dr*dpdr(r+dr,M+Mk3,T+Tk3,P,p+pk3,L+Lk3,tau+tauk3,kappa)
        Tk4 = dr*dTdr(r+dr,M+Mk3,T+Tk3,P,p+pk3,L+Lk3,tau+tauk3,kappa)
        Mk4 = dr*dMdr(r+dr,M+Mk3,T+Tk3,P,p+pk3,L+Lk3,tau+tauk3,kappa,dr)
        Lk4 = dr*dLdr(r+dr,M+Mk3,T+Tk3,P,p+pk3,L+Lk3,tau+tauk3,kappa)
        tauk4 = dr*dtaudr(r+dr,M+Mk3,T+Tk3,P,p+pk3,L+Lk3,tau+tauk3,kappa)
        
        dp = (pk1+2*pk2+2*pk3+pk4)/6.0
        dT = (Tk1+2*Tk2+2*Tk3+Tk4)/6.0
        dM = (Mk1+2*Mk2+2*Mk3+Mk4)/6.0
        dL = (Lk1+2*Lk2+2*Lk3+Lk4)/6.0
        dtau = (tauk1+2*tauk2+2*tauk3+tauk4)/6.0
        

        # if count == 100:
        #     count = 0
        #     print 'dr: ', dr, r
        #     print 'dM: ', dM, M
        #     print 'dT: ', dT, T
        #     print 'P: ', P
        #     print 'dp: ', dp, p
        #     print 'dL: ', dL, L
        #     print 'dtau: ', dtau, tau
        #     print 'deltatau: ', deltatau
            # print 'kappa: ', kappa
        #     if r > Rsun:
        #         print 'RADIUS FUCKED'
        
        kappaES=0.02*(1.0+X)
        kappaFF = (10.0**24.0)*(Z+0.0001)*((p*(10**(-3.0)))**0.7)*(T**(-3.5))
        kappaH = (2.5*(10.0**(-32.0)))*(Z/0.02)*((p*(10**(-3.0)))**0.5)*(T**9.0)
        maxkappa=max(kappaES,kappaFF)
        kappa = 1.0/((1.0/kappaH) + (1.0/maxkappa))
        
        deltatau = (kappa*(p**2.0))/(abs(dpdr(r,M,T,P,p,L,tau,kappa)))
        # if count == 1000:
        #     count = 0
        #     Radius.append(r)
        #     Mass.append(M)
        #     Temperature.append(T)
        #     Pressure.append(P)
        #     Density.append(p)
        #     Luminosity.append(L)
        #     Tau.append(tau)
        #     Kappa.append(kappa)
        Radius=r
        Mass=M
        Temperature=T
        Pressure=P
        Density=p
        Luminosity=L
        Tau=tau
        Kappa=kappa

        if kappa == 0.034:
            # print 'KAPPA BREAK'
            break

    Rstar = r
    LRstar = L
    TRstar = T

    # print 'LOOP BROKEN'
    # print 'r: ', r
    # print 'M: ', M
    # print 'T: ', T
    # print 'P: ', P
    # print 'p: ', p
    # print 'L: ', L
    # print 'tau: ', tau
    # print 'deltatau: ', deltatau

    trial=(LRstar-(4*pi*SB*Rstar**2*TRstar**4))/(sqrt(4*pi*SB*Rstar**2*TRstar**4*LRstar))
    # x=bisect(trial,0.3,500)
    # print x 

    # return r,M,T,P,p,L,tau,kappa,trial
    return Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial


        
