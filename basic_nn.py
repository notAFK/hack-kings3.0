import numpy as math

# sigmoid function
def nonlin(x, deriv = False):
	if(deriv == True):
		return x * (1 - x)
	return 1/(1 + math.exp(-x))
	
# input dataset
X = math.array([[0, 0, 1],
				[0, 1, 1],
				[1, 0, 1],
				[1, 1, 1]])
				
# output dataset
y = math.array([[0, 0, 1, 1]]).T

def derivative(x, y):

	m, n = np.shape(x)
	#numIterations= 1000
	#alpha = 0.005
	syn0 = np.ones([n, 1])

	for iter in xrange(10000):

		# forward propagation
		l0 = X
		l1 = nonlin(math.dot(l0, syn0))
	
		# error
		l1_error = y - l1
	
		# multiply how much we missed by the
		# slope of the sigmoid at the values in l1
		l1_delta = l1_error * nonlin(l1, True)
	
		# update weights
		syn0 += math.dot(l0.T, l1_delta)

	print "Output After Training:"
	print l1
