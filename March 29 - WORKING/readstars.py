import matplotlib.pyplot as plt
import ast
import json
from constants import Temp_by_hand, Lsun
import numpy as np


# file = open('test.txt', 'r')

# data = file.read().split('END')

# print data

DATA = []
Star = []
with open('OUTPUT_CZ.txt') as f:
	for line in f:
		Star = [elt.strip() for elt in line.split('/n')]
		DATA.append(Star)


x = DATA

STARS = []


for i in xrange(len(x)):
	STARS.append(ast.literal_eval(x[i][0]))


# print len(STARS)
# print len(STARS[0])
# print len(STARS[1][1])
# print type(STARS)


# STARS[Which Star?][Which Parameter?][Which value?]
# STARS[5][6][len(STARS[5][6]-1)]


# for i in xrange(len(STARS)):
# 	print STARS[i][0]

# print STARS
star = len(STARS) - 3
star = 5 

LMAIN_SEQ = []
TMAIN_SEQ = []

TcLIST = []
errors = 0

for n in xrange(len(STARS)):
	star = n
	Lfinal = STARS[star][6]
	Rfinal = STARS[star][1]
	# Tfinal = STARS[star][3] 
	# if Tfinal > 1.0e6:
	Tfinal = Temp_by_hand(Rfinal,Lfinal)
	if Tfinal < 1000.0 or Tfinal > 40000:
		errors+=1
		continue
	print 'Tc: ', STARS[star][0][0]
	print 'pc: ', STARS[star][0][3]
	print 'Lfinal: ', Lfinal
	print 'Rfinal: ', Rfinal
	print 'Tfinal: ', Tfinal
	print '--------------------'
	LMAIN_SEQ.append(Lfinal/Lsun)
	TMAIN_SEQ.append(Tfinal)
	TcLIST.append(STARS[star][0][0])


print 'NUMBER OF STARS: ', len(STARS)
print 'NUMBER OF ERRORS: ', errors
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_yscale('log')
# ax.set_xscale('log')

plt.scatter(TMAIN_SEQ,LMAIN_SEQ)
plt.title('Main Sequence')
plt.xlabel('Temperature')
plt.ylabel('Luminosity/Lsun')
# plt.xlim(0,200000) 
# plt.xlim(0,50000) 
# plt.ylim(10**-3,10**6)
plt.ylim()
plt.gca().invert_xaxis()
plt.show()

TcLIST.sort()
print TcLIST
# fig = plt.figure()
# plt.plot(STARS[star][1],STARS[star][2])
# plt.title('Mass')
# plt.figure()
# plt.plot(STARS[star][1],STARS[star][3])
# plt.title('Temperature')
# plt.figure()
# plt.plot(STARS[star][1],STARS[star][4])
# plt.title('Pressure')
# plt.figure()
# plt.plot(STARS[star][1],STARS[star][5])
# plt.title('Density')
# plt.figure()
# plt.plot(STARS[star][1],STARS[star][6])
# plt.title('Luminosity')

# star1 = len(STARS) -1
# # star2 = len(STARS) - 2
# # print STARS[star1]
# plt.plot(STARS[star1][1],STARS[star1][3])
# # print STARS
# # plt.plot(STARS[star2][1],STARS[star2][3])
# # plt.savefig('fuckedupTs.png')
# plt.show()
# # print 'LEN: ', len(STARS[1][6])

# # for n in xrange()

# plt.figure()
# for star in xrange(len(STARS)):
# 	plt.scatter(STARS[star][3][len(STARS[star][1])-1],STARS[star][6][len(STARS[star][6])-1])



# plt.show()







