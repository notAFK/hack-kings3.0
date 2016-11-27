import copy, numpy as np
from lin_reg import derivative
np.random.seed(0)

# compute sigmoid nonlinearity
def sigmoid(x):
	output = 1 / (1 + np.exp(-x))
	return output

# convert output of sigmoid function to its derivate#
def sigmoid_output_to_derivative(output):
	return output * (1 - output)
	

# training dataset generation
int2binary = {}
binary_dim = 4

largest_number = pow(2, binary_dim)
binary = np.unpackbits(
	np.array([range(largest_number)], dtype = np.uint8).T, axis = 1)
for i in range(largest_number):
	int2binary[i] = binary[i]
	
# input variables
alpha = 0.2
input_dim = 4
hidden_dim = 32
output_dim = 1

# initialise neural network weights
synapse_0 = 2 * np.random.random((input_dim, hidden_dim)) - 1
synapse_1 = 2 * np.random.random((hidden_dim, output_dim)) - 1
synapse_h = 2 * np.random.random((hidden_dim, hidden_dim)) - 1

synapse_0_update = np.zeros_like(synapse_0)
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)



# training logic
for j in range(1000):

		# generate a simple addition problem (a + b = c)
		# a_int = np.random.randint(largest_number / 2) # int version
		# a = int2binary[a_int] # binary encoding
	
		# b_int = np.random.randint(largest_number / 2) # int version
		# b = int2binary[b_int] # binary encoding
	
		# true answer
		# c_int = 2 * a_int
		# c = int2binary[c_int]


	
	# Generate sample data
	tweets = ([[0.0, 0.9, 0.5, 0.5], 
				[0.0, 0.9, 0.6, 0.7], 
				[0.1, 0.8, 0.6, 0.7],
				[0.1, 0.8, 0.6, 0.7],
				[0.2, 0.7, 0.6, 0.7],
				[0.2, 0.7, 0.6, 0.7],
				[0.3, 0.6, 0.6, 0.7],
				[0.3, 0.6, 0.6, 0.7],
				[0.4, 0.5, 0.6, 0.7],
				[0.4, 0.5, 0.6, 0.7],
				[0.5, 0.4, 0.6, 0.7],
				[0.5, 0.4, 0.6, 0.7],
				[0.6, 0.3, 0.6, 0.7],
				[0.6, 0.3, 0.6, 0.7],
				[0.7, 0.2, 0.6, 0.7],
				[0.7, 0.2, 0.6, 0.7],
				[0.8, 0.1, 0.6, 0.7],
				[0.8, 0.1, 0.6, 0.7],
				[0.9, 0.0, 0.6, 0.7],
				[0.9, 0.0, 0.6, 0.7]])

	time = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]).T
	share_price = np.array([[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]]).T

	# Get derivatives in each point
	for i in xrange(14) :

		X = np.array(tweets[2+i:7+i][:])
		#print X
		#print time
		#print share_price
		Y = derivative(time[i:i+5], share_price[i:i+5])
		#print "Y: " + str(Y)
		
		
	
	
		#a = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
		#c = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.35])
	
		# where we'll store our best guess in binary
		d = np.zeros_like(Y)
	
		overallError = 0
	
		layer_2_deltas = list()
		layer_1_values = list()
		layer_1_values.append(np.zeros(hidden_dim))
	
		# moving along the positions in the binary encoding
		for position in xrange(binary_dim):
	
			# generate IO			
			x = np.array([X[binary_dim - position - 1, :]])
			y = np.array([[Y[binary_dim - position - 1]]])
		
			# hidden layer (input ~+ prev_hidden)
			layer_1 = sigmoid(np.dot(x, synapse_0) + np.dot(layer_1_values[-1], synapse_h))
		
			#  output layer (new binary representation)
			layer_2 = sigmoid(np.dot(layer_1, synapse_1))
		
			# error
			layer_2_error = y - layer_2
			layer_2_deltas.append((layer_2_error) * sigmoid_output_to_derivative(layer_2))
			overallError += np.abs(layer_2_error[0])
		
			# decode estimate so we can print it out
			d[binary_dim - position - 1] = layer_2[0][0]
		
			# store hidden layer so we use it the next time
			layer_1_values.append(copy.deepcopy(layer_1))
		
		future_layer_1_delta = np.zeros(hidden_dim)
	
		for position in xrange(binary_dim):
	
			x = np.array([[X[position, :]]])
			layer_1 = layer_1_values[-position-1]
			prev_layer_1 = layer_1_values[-position-2]
		
			# error at output layer
			layer_2_delta = layer_2_deltas[-position-1]
			# error at hidden layer
			layer_1_delta = (future_layer_1_delta.dot(synapse_h.T) + layer_2_delta.dot(synapse_1.T)) * sigmoid_output_to_derivative(layer_1)
			#print "Layer_1:" + str(np.shape(layer_1))
			#print "Layer_2_delta:" + str(np.shape(layer_2_delta[:][:][0]))
			#print np.shape(np.atleast_2d(layer_1))
			# let's update all our weights so we can try again
			synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta[:][:][0])
			synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta[:][:][0])
			#print "x:" + str(np.shape(x))
			#print "Layer_1_delta: " + str(np.shape(layer_1_delta))
			synapse_0_update += x[0, :, :].T.dot(layer_1_delta[:][:][0])
		
			future_layer_layer_1_delta = layer_1_delta
		
		
		synapse_0 += synapse_0_update * alpha
		synapse_1 += synapse_1_update * alpha
		synapse_h += synapse_h_update * alpha
	
		synapse_0_update *= 0
		synapse_1_update *= 0
		synapse_h_update *= 0
	
		# print out progress
		if(j % 10 == 0):
			print "Error:" + str(overallError)
			print "Pred:" + str(d)
			print "True:" + str(y)
			print str(X) + " -> " + str(d[0])
			print "------------"



	
	


