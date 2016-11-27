import numpy as np

# sigmoid function
def nonlin(x, deriv = False):
	if(deriv == True):
		return x * (1 - x)
	return 1/(1 + np.exp(-x))

def derivative(x, y):

	m, n = np.shape(x)
	#numIterations= 1000
	#alpha = 0.005
	np.random.seed(1)

	# initialise weights randomly
	syn0 = 2*np.random.random((n, 1)) - 1

	for iter in xrange(100):

		# forward propagation
		l0 = x
		l1 = nonlin(np.dot(l0, syn0))
		print l1
		print x
		print y
		# error
		l1_error = y - l1
	
		# multiply how much we missed by the
		# slope of the sigmoid at the values in l1
		l1_delta = l1_error * nonlin(l1, True)
	
		# update weights
		syn0 += np.dot(l0.T, l1_delta)
	
	return syn0[0];
	
	print "Output After Training:"
	print l1
