import matplotlib.pyplot as plt
import ast
import json


# file = open('test.txt', 'r')

# data = file.read().split('END')

# print data

DATA = []
Star = []
with open('outputcz.txt') as f:
	for line in f:
		Star = [elt.strip() for elt in line.split('/n')]
		DATA.append(Star)


x = DATA

STARS = []


for i in xrange(len(x)):
	STARS.append(ast.literal_eval(x[i][0]))


print len(STARS)
print len(STARS[0])
print len(STARS[1][1])
print type(STARS)


# STARS[Which Star?][Which Parameter?][Which value?]
# STARS[5][6][len(STARS[5][6]-1)]


for i in xrange(len(STARS)):
	print STARS[i][0]

print STARS
print STARS[1][0][0]
plt.figure()
plt.plot(STARS[0][1],STARS[0][2])
plt.title('Mass')
plt.figure()
plt.plot(STARS[0][1],STARS[0][3])
plt.title('Temperature')
plt.figure()
plt.plot(STARS[0][1],STARS[0][4])
plt.title('Pressure')
plt.figure()
plt.plot(STARS[0][1],STARS[0][5])
plt.title('Density')
plt.figure()
plt.plot(STARS[0][1],STARS[0][6])
plt.title('Luminosity')

plt.show()