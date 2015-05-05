"""
Author: Stephen Spivack
Created: Fri May 4 15:09:02 2015

"""
import cellular
import qlearn
import time
import sys
import cliff_Q
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


alphas = np.linspace(0, 1, 11) 
gammas = np.linspace(0, 1, 11)

ntrials = 100

success = np.zeros((len(alphas), len(gammas)))
#print(success)

def simulate(alpha, gamma):
	x = 0
	x = cliff_Q.begin(.1, alpha, gamma)
	return x

for i in xrange(len(alphas)):
    for j in xrange(len(gammas)):
        alpha = alphas[i]
        gamma = gammas[j]        
        
        print("alpha = {}, gamma = {}".format(alpha, gamma))    
        success[i,j] = simulate(alpha, gamma)
        print ("for alpha = %d gamma = %d success[i,j] = %d" % (i, j, success[i,j]))


np.savetxt('data.txt', success)

#######################retrieve data and plot it#########################

#success = np.loadtxt('data.txt')

#plt.figure()

#plt.imshow(success)
        
#plt.figure()
#ax = plt.gca(projection='3d')

#X, Y = np.meshgrid(alphas, gammas)

#ax.plot_surface(X, Y, success, cmap=plt.cm.coolwarm)