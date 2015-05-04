import cellular
import qlearn
import time
import sys

count = 0
alpha = .1

for x in range(0, 110):
	if x >= 0 and x <10:
		cliff_Q.main(.1, .1, 0)
	
	if x >= 10 and x < 20:
		cliff_Q.main(.1, .1, .1)
	
	if x >= 20 and x < 30:
		cliff_Q.main(.1, .1, .2)

	if x >= 30 and x < 40:
		cliff_Q.main(.1, .1, .3)

	if x >= 40 and x < 50:
		cliff_Q.main(.1, .1, .4)

	if x >= 50 and x < 60:
		cliff_Q.main(.1, .1, .5)

	if x >= 60 and x < 70:
		cliff_Q.main(.1, .1, .6)

	if x >= 70 and x < 80:
		cliff_Q.main(.1, .1, .7)

	if x >= 80 and x < 90:
		cliff_Q.main(.1, .1, .8)

	if x >= 90 and x < 100:
		cliff_Q.main(.1, .1, .9)

	if x >= 100 and x < 110:
		cliff_Q.main(.1, .1, 1)


gamma = .9
for x in range(0, 110):
	if x >= 0 and x <10:
		cliff_Q.main(.1, 0, .9)

	if x >= 10 and x < 20:
		cliff_Q.main(.1, .1, .9)

	if x >= 20 and x < 30:
		cliff_Q.main(.1, .2, .9)

	if x >= 30 and x < 40:
		cliff_Q.main(.1, .3, .9)

	if x >= 40 and x < 50:
		cliff_Q.main(.1, .4, .9)

	if x >= 50 and x < 60:
		cliff_Q.main(.1, .5, .9)

	if x >= 60 and x < 70:
		cliff_Q.main(.1, .6, .9)

	if x >= 70 and x < 80:
		cliff_Q.main(.1, .7, .9)

	if x >= 80 and x < 90:
		cliff_Q.main(.1, .8, .9)

	if x >= 90 and x < 100:
		cliff_Q.main(.1, .9, .9)

	if x >= 100 and x < 110:
		cliff_Q.main(.1, 1, .9)
