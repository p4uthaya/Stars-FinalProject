from starintegration_init import starintegration
from constants import *
import matplotlib.pyplot as plt
import datetime
from tauinterp import tau_interp


import csv


print 'Calling Star Integration'
i = 0

# TEMPLIST = range(15000000,35000000,1000000)
# for index in xrange(len(TEMPLIST)):
Tsun = 15000000
psun = 1.622e5

#Initial Conditions
##Tc = Tsun
##pc = psun
#Tc = 8.23*(10.0**6.0) 
# Tc = 7.41*(10.0**6.0)
Tc = 9e6#10.0e6
#pc = 58560
# pc = 100000#64120.4969564#64158.9788739#64416
pc = 300#351379.101547
 # 64120.4969564
# pc = np.linspace(0.3,500,1000)

# Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial = starintegration(r,M,T,P,p,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc)
ERRORS = []
STARS = []

# thefile = open('OUTPUT_CZ.txt', 'a')

# TEMPLIST = np.arange(1.0e7,3.1e7,0.05e7)
# TEMPLIST = [20000000]
# print TEMPLIST
# TEMPLIST = np.arange(1.0e7,2.0e7,0.1e7)
TEMPLIST=[1.5e7]#[2.4e7]

numstars = 0 
print "Number of Stars: ",  len(TEMPLIST)
for Temp in xrange(len(TEMPLIST)):
	numstars+=1
	print 'Star #: ', numstars
	print 'Stars left: ', len(TEMPLIST) - numstars
	Tc = TEMPLIST[Temp]
	# pc1 = 122411.799979

	# pc2 = 122411.859548
	T = Tc 
	# print T
	# print Tc


	# print 'Calculating 300'
	# Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial1 = starintegration(r,M,T,P,pc1,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc1)
	# print 'Calculating 500000'
	# Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial2 = starintegration(r,M,T,P,pc2,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc2)

	# print 'Entering Loop'
	# if trial1 < 0.0 and trial2 < 0.0:
	# 	print "!!!ERROR : BOTH NEGATIVE!!!!!!!!!!!!!"
	# 	change = (pc2-pc1)/2.0
	# 	pc3 = pc1+change
	# 	Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial3 = starintegration(r,M,T,P,pc3,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc3)
	# 	print trial1, trial2, trial3
	# 	ERRORS.append(Tc)
	# 	continue


	# if trial1 > 0.0 and trial2 > 0.0:
	# 	print "!!!ERROR: BOTH POSITIVE!!!!!!!!!!!!!!"
	# 	change = (pc2-pc1)/2.0
	# 	pc3 = pc1+change
	# 	Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial3 = starintegration(r,M,T,P,pc3,L,tau,kappa,deltatau,dr,dM,dT,dP,dp,dL,dtau,pc3)
	# 	print trial1, trial2, trial3
	# 	ERRORS.append(Tc)
	# 	continue
	trial1, trial2 = -1.0, 1.0
	pc1 = 300
	pc2 = 10000000
	while trial1 < 0.0 and trial2 > 0.0:
		print 'pc1: ',pc1, 'pc2: ', pc2
		print 'trial1: ', trial1,  'trial2: ', trial2
		change = (pc2-pc1)/2.0
		pc3 = pc1+change
		Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trial3, massbreak = starintegration(Tc,pc3)
		print 'trial3: ', trial3

		if trial3 < 0.0:
			pc1 = pc3
			trial1 = trial3

		if trial3 > 0.0:
			pc2 = pc3
			trial2 = trial3

		if massbreak == True:
			print 'CALLING TAU INTERP'
			Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trialavg, massbreak = tau_interp(Tau,pc2,Tc)
			print 'DONE TAU INTERP'
			break



		if (abs(pc1-pc2)/pc2) < 0.01:
		# if abs(pc1/pc2) < 0.05:
		# if abs(pc1-pc2) < 0.001:
		# if abs(trial1 - trial2) < 100.0:
			# pcavg = (pc1+pc2)/2.0
			# if trial1 > 0.0: 
			# 	pcavg = pc1
			# else: 
			pcavg = pc2
			Radius, Mass, Temperature, Pressure, Density, Luminosity, Tau, Kappa, trialavg, massbreak = starintegration(Tc,pcavg)
			# print 'trialavg: ', trialavg
			# print 'Radius: ', Radius[len(Radius)-1]
			# print 'Mass: ', Mass[len(Mass)-1]
			# print 'Tempurature: ', Temperature[len(Temperature)-1]
			# print 'Pressure: ', Pressure[len(Pressure)-1]
			# print 'Density: ', Density[len(Density)-1]
			# print 'Luminosity: ', Luminosity[len(Luminosity)-1]
			# print 'Tau: ', Tau[len(Tau)-1]
			# print 'Kappa: ', Kappa[len(Kappa)-1]
			# print 'pc1: ', pc1
			# print 'pc2: ', pc2
			break


	Star = []

	metadata = [Tc, pc1, pc2,(pc1+pc2/2.0), trial1, trial2, trial3]
	Star.append(metadata)
	Star.append(Radius)
	Star.append(Mass)
	Star.append(Temperature)
	Star.append(Pressure)
	Star.append(Density)
	Star.append(Luminosity)
	Star.append(Tau)	
	Star.append(Kappa)



	thefile = open('OUTPUT_CZ_adappc2.txt', 'a')
	thefile.write("%s \n" % Star)
	thefile.close()

	# print 'LEN STAR: ', len(Star)
	# print 'LEN STAR[0] "Radius": ', len(Star[0])
	# plt.plot(Star[0],Star[1])

	# STARS.append(Star)
# Star[0][len(Star[0])-1]

# plt.show()

# import json

# # LoL = [ range(5), list("ABCDE"), range(5) ]



# with open('StarsCZ.txt','w') as myfile:
#     json.dump(STARS,myfile)

# with open('ErrorsCZ.txt','w') as myfile:
	# json.dump(ERRORS,myfile)



# plt.plot(Mass)
# plt.title('Mass')
# plt.savefig('mass.png')
# plt.clf()

# plt.plot(Temperature)
# plt.title('Temperature')
# plt.savefig('tempurature.png')
# plt.clf()

# plt.plot(Pressure)
# plt.title('Pressure')
# plt.savefig('pressure.png')
# plt.clf()

# plt.plot(Density)
# plt.title('Density')
# plt.savefig('density.png')
# plt.clf()

# plt.plot(Luminosity)
# plt.title('Luminosity')
# plt.savefig('luminosity.png')
# plt.clf()

# plt.plot(Tau)
# plt.title('Tau')
# plt.savefig('tau.png')
# plt.clf()

# fig = plt.figure()
# ax = fig.add_subplot(2,1,1)
# # ax.set_yscale('log')
# plt.plot(Kappa)
# ax.set_yscale('log')
# plt.title('Kappa')
# plt.savefig('kappa.png')
# # plt.
# plt.clf()