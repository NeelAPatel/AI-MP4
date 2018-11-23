'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
	print "Method not implemented: %s" % inspect.stack()[1][3]
	sys.exit(1)
	
	
def _print_array_state(state):
	for i in range(0, len(state)):
		print state[i]

'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
	features=[]
	
	_print_array_state(digit_data)
	
	for x in range(width):
		for y in range(height):
			features.append(digit_data[x][y])
	
	print (features)
	print (str(len(features)))
	
	#Features = 2d array with 1 and 0
	# Features2 = 1D array of 1 and 0, 28x28
	# Your code ends here #
	#_raise_not_defined()
	return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
	features=[]
	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()
	return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
	features=[]
	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()
	return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=1.0):
	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
	predicted = -1

	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()

	return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

	predicted=[]

	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()

	return predicted







	
	
