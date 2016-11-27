import numpy as np
import random

# sigmoid function
def nonlin(x):
	return 1/(1 + np.exp(-(x/3)))

# m denotes the number of examples here, not the number of features
def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        #print "Theta:" + str(theta)
        #print "X:" + str(np.shape(x))
        #print "Hypo:" + str(np.shape(hypothesis))
        #print "Y:" + str(np.shape(y))
        loss = hypothesis - y
        #print "Loss:" + str(loss)
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        #print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        #print gradient
        # update
        theta = theta - alpha * gradient
        #print theta
    return theta
    

def derivative(x, y):

	m, n = np.shape(x)
	numIterations= 1000
	alpha = 0.005
	theta = np.ones([n, 1])
	
	#print theta
	theta = gradientDescent(x, y, theta, alpha, m, numIterations)
	#print "Theta:" + str(theta)
	#print "X:" + str(x)
	#print "Y:" + str(y)
	theta = nonlin(theta)
	#print "Theta:" + str(theta)
	return theta * np.ones_like(y)
	#print m
	#print n

	
# gen data
x = np.array([[0],
				[1],
				[2],
				[3]])
y = np.array([[0, 2, 4, 8]]).T
