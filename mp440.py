'''
Raise a "not defined" exception as a reminder 
'''
# import util
import sys
import inspect


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
	features = []
	
	# _print_array_state(digit_data)
	#print (digit_data)
	
	for x in range(width):
		for y in range(height):
			#print ("Val: " + str(digit_data[x][y]))
			if (digit_data[x][y] > 0):
				features.append(1)
			else:
				features.append(0)
		
		# if (digit_data[x][y] == 0):
		# 	features.append(0)
		# else:
		# 	features.append(1)
	
	# features = util.Counter()
	# for x in range(width):
	# 	for y in range(height):
	# 		if digit_data.getPixel(x, y) > 0:
	# 			features[(x, y)] = 1
	# 		else:
	# 			features[(x, y)] = 0
	#print ("EXtract features")
	#print (features)
	#print (str(len(features)))
	#
	# print ()
	# print ()
	
	# Features = 2d array with 1 and 0
	# Features2 = 1D array of 1 and 0, 28x28
	# Your code ends here #
	# _raise_not_defined()
	return features


'''
Extract advanced features that you will come up with 
'''


def extract_advanced_features(digit_data, width, height):
	features = []
	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()
	return features


'''
Extract the final features that you would like to use
'''


def extract_final_features(digit_data, width, height):
	features = []
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


def compute_statistics(data, label, width, height, feature_extractor, percentage=1):
	# Your code starts here #
	
	# data = Training data = contains all the numbers in image form
	
	# 1. Take TrainingData => extract basic features => all images converted to 0s and 1s only, in 1D array
	# 2. find len(data) => find % of len(data) = sample
	# 3. Save first Sample amt of data (and first Sample amt of labels too)
	# 4. use <some formula> to calculate for each sample
	# 5. Store results in global array
	
	# Q1: What are labels? What are its purpose?
	# Q2: What values do we map to the variables in the given formula
	
	arrIntegerFreq = [0,0,0,0,0,0,0,0,0,0]
	arrIntegerIndex = [[],[],[],[],[],[],[],[],[],[]]
	
	index = 0
	while index < len(label):
		
		if (label[index] == 0):
			arrIntegerFreq[0] += 1
			arrIntegerIndex[0].append(index)
		elif (label[index] == 1):
			arrIntegerFreq[1] += 1
			arrIntegerIndex[1].append(index)
		elif (label[index] == 2):
			arrIntegerFreq[2] += 1
			arrIntegerIndex[2].append(index)
		elif (label[index] == 3):
			arrIntegerFreq[3] += 1
			arrIntegerIndex[3].append(index)
		elif (label[index] == 4):
			arrIntegerFreq[4] += 1
			arrIntegerIndex[4].append(index)
		elif (label[index] == 5):
			arrIntegerFreq[5] += 1
			arrIntegerIndex[5].append(index)
		elif (label[index] == 6):
			arrIntegerFreq[6] += 1
			arrIntegerIndex[6].append(index)
		elif (label[index] == 7):
			arrIntegerFreq[7] += 1
			arrIntegerIndex[7].append(index)
		elif (label[index] == 8):
			arrIntegerFreq[8] += 1
			arrIntegerIndex[8].append(index)
		elif (label[index] == 9):
			arrIntegerFreq[9] += 1
			arrIntegerIndex[9].append(index)
	
		index += 1
	#print arrIntegerFreq
	# print arrIntegerIndex
	
	# currIndexArr = arrIntegerIndex[0]
	# img = extract_basic_features(data[currIndexArr[0]], width, height)
	#
	# print (img)
	
	
	
	imgFreq = [[0] * (width*height) for i in range(10)]

	curr = 0
	while curr <= 9:

		currIndexArr = arrIntegerIndex[curr]
		
		#print ("CURR: " + str(curr))
		#print (str(currIndexArr))
		
		count = 1
		for index in currIndexArr:
			
			img = extract_basic_features(data[index], width,height)

			for x in range(width*height):
				if (img[x] == 1):
					imgFreq[curr][x] += 1
			
			
			if count == 2:
				break
			count += 1
		curr += 1
	
	print ()
	print ()
	print ()
	print imgFreq
	# for curr = 0
	# 	- get array of indexes
	# 	for index in array
	# 		img = extract (data[index])
	#
	# 		for x,y in width height
	# 			if img[x][y] == 1
	# 				imgFreq[curr][x][y] += 1
	#
	# 	- calculate based on frequencies, might need your help on this
	
	
	return 0


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
	predicted = []
	
	# Your code starts here #
	# Your code ends here #
	_raise_not_defined()
	
	return predicted
