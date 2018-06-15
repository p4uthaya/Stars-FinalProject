from starintegration_init import starintegration
from constants import *
import matplotlib.pyplot as plt
import datetime



def tau_interp(tauinfinity,pc,Tc):
	print 'TAU INTERPOLATION'
	tau = 0.0
	   ###--- INITAL CONDITIONS ---###


	Epp0=(1.07*(10**(-12.0)))*pc*(X**2.0)*((Tc*10**(-6.0))**4.0)
	Ecno0=(8.24*(10.0**(-31.0)))*pc*0.03*(X**2.0)*((Tc*10**(-6.0))**19.9)
	E0=Epp0+Ecno0

	r0=0.0001
	L0=0.0
	M0=((4.0*pi)/3.0)*(r0**3.0)*pc
	L0 = ((4.0*pi)/3.0) * (r0**3.0)*pc*E0
	tau0 = 0.0


	Rstar = r0


	dr = 1000.0
	dp =-0.0001
	dT =-1
	dM =0.0001
	dL =0.0001
	dtau = 0.0001
	dP = 0.0001

	p0 = pc
	T0 = Tc

	kappaES0=0.02*(1.0+X)
	kappaFF0=(10.0**(24.0))*(Z+0.0001)*((p0*(10.0**(-3.0)))**0.7)*(T0**(-3.5))
	kappaH0=2.5*(10.0**(-32.0))*(Z/0.02)*((p0*(10.0**(-3.0)))**0.5)*(T0**9.0)
	maxkappa0=max(kappaES0,kappaFF0)
	kappa0 = 1.0/((1.0/kappaH0) + (1.0/maxkappa0))

	P0 = Pt(r0,M0,T0,1.0,p0,L0,tau0,kappa0)
	kappa = kappa0


	P = P0
	r = r0
	p = pc
	L = L0
	M = M0
	T = Tc
	tau = tau0
	P = P0
	deltatau = 1.0


	###--- END ---###



	Radius = []
	Mass = []
	Temperature = []
	Pressure = []
	Density = []
	Luminosity = []
	Tau = []
	Kappa = []

	adap = 0

	i=1
	count = 0
	massbreak = False
	# while deltatau > 2.0/3.0: 
	while abs((tauinfinity - tau) - 2.0/3.0) > 0.01:
		# print tauinfinity - tau
					# i = 0
		# if M > 3*Msun:
		#     tauinfinity = tau
		#     taur = tauinfinity - 2.0/3.0 
		#     # while tauinfinity - 2.0/3.0 > 0.01:
		#         # starintegration()
		#     massbreak = True
		#     Rstar = r
		#     LRstar = L
		#     TRstar = T
		#     print 'MASS BREAK'
		#     print 'Rstar: ', Rstar
		#     print 'LRstar: ', LRstar
		#     print 'TRstar: ', TRstar
		#     trial=(LRstar-(4*pi*SB*Rstar**2*TRstar**4))/(sqrt(4*pi*SB*Rstar**2*TRstar**4*LRstar))

		#     # print 'TRIAL: ', trial
		#     return Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial, massbreak
		# count+=1
		i+=1
		r += dr
		p += dp 
		T += dT
		M += dM
		L += dL 
		tau += dtau
		P=Pt(r,M,T,P,p,L,tau,kappa)
		
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
		
		if np.isnan(Lk4):
			break

		dp = (pk1+2*pk2+2*pk3+pk4)/6.0
		dT = (Tk1+2*Tk2+2*Tk3+Tk4)/6.0
		dM = (Mk1+2*Mk2+2*Mk3+Mk4)/6.0
		dL = (Lk1+2*Lk2+2*Lk3+Lk4)/6.0
		dtau = (tauk1+2*tauk2+2*tauk3+tauk4)/6.0
		

		if count == 10000: #and kappa != 0.034:
		    count = 0
		    print 'dr: ', r/Rsun, dr
		    print 'dM: ', M/Msun, dM
		    print 'dT: ', T, dT
		    print 'P: ', P
		    print 'dp: ', p, dp
		    print 'dL: ', L/Lsun, dL
		    print 'dtau: ', tau, dtau
		    print 'deltatau: ', deltatau
		    print 'kappa: ', kappa            # print 'kappa: ', kappa
		    # if r > Rsun:
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
			# break
			# dr = 10000.0
			adap += 1
			if adap == 10000: 
				dr = 10.0*dr
				# adap = 0
				# print r, dr
				# print 'dr: ', r/Rsun, dr
				# print 'dM: ', M/Msun, dM
				# print 'dT: ', T, dT
				# print 'P: ', P
				# print 'dp: ', p, dp
				# print 'dL: ', L/Lsun, dL
				# print 'dtau: ', tau, dtau
				# print 'deltatau: ', deltatau
				# print 'kappa: ', kappa
				adap = 0

		# if pc < 234667.98: 
			# if i == 10000:
			# print 'dL: ', L/Lsun, dL, Lk1, Lk2, Lk3, Lk4 


		# if p < 0.0: 
		#     print 'density break'
		#     print p, dr 
		# if T < 0.0:
		#     print 'temperature break'
		#     print T, dT

	Rstar = r
	LRstar = L
	TRstar = T
	Mstar = M
	print 'Rstar: ', Rstar/Rsun
	print 'LRstar: ', LRstar/Lsun
	print 'Mstar: ', Mstar/Msun
	print 'TRstar: ', TRstar
	trial=(LRstar-(4*pi*SB*Rstar**2*TRstar**4))/(sqrt(4*pi*SB*Rstar**2*TRstar**4*LRstar))
	return Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial, massbreak


			
