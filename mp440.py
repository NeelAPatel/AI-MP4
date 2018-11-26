'''
Raise a "not defined" exception as a reminder 
'''
# import util
import sys
import inspect
import matplotlib as mpl
import numpy as np
import math


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
def getDomainList(mapList):
	uniqueList = []
	for x in mapList:
		if x not in uniqueList:
			uniqueList.append(x)
	
	return uniqueList

def compute_statistics(data, label, width, height, feature_extractor, percentage=1):
	# Your code starts here #
	sampleSize = int(float(percentage)*len(label))
	
	
	
	# === PRIOR PROBABILITY ===
	#arrIntegerFreq = counts how many time each integer appears in the sampleSize
	#arrIntegerIndex = lists all the indexes that the integer appears on. i.e label[10] is a 0,
	#                  so 10 would be part of arrIntegerIndex[0]'s list
	global arrIntegerFreq
	global arrIntegerIndex
	arrIntegerFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	arrIntegerIndex = [[], [], [], [], [], [], [], [], [], []]
	
	index = 0
	while index < sampleSize:
		if label[index] == 0:
			arrIntegerFreq[0] += 1
			arrIntegerIndex[0].append(index)
		elif label[index] == 1:
			arrIntegerFreq[1] += 1
			arrIntegerIndex[1].append(index)
		elif label[index] == 2:
			arrIntegerFreq[2] += 1
			arrIntegerIndex[2].append(index)
		elif label[index] == 3:
			arrIntegerFreq[3] += 1
			arrIntegerIndex[3].append(index)
		elif label[index] == 4:
			arrIntegerFreq[4] += 1
			arrIntegerIndex[4].append(index)
		elif label[index] == 5:
			arrIntegerFreq[5] += 1
			arrIntegerIndex[5].append(index)
		elif label[index] == 6:
			arrIntegerFreq[6] += 1
			arrIntegerIndex[6].append(index)
		elif label[index] == 7:
			arrIntegerFreq[7] += 1
			arrIntegerIndex[7].append(index)
		elif label[index] == 8:
			arrIntegerFreq[8] += 1
			arrIntegerIndex[8].append(index)
		elif label[index] == 9:
			arrIntegerFreq[9] += 1
			arrIntegerIndex[9].append(index)
	
		index += 1
	
	#print ("> Prior Probability Complete")
	
	# === CONDITIONAL PROBABILITY ===
	
	# Part 1: Count how many times 1 gets flagged for each integer.
	global imgFreq
	imgFreq= [[0] * (width*height) for i in range(10)] # 10 elems of width*height size

	curr = 0
	while curr <= 9:
		currIndexArr = arrIntegerIndex[curr]
		
		# for every occurance of 'curr' integer, get the image and count the 1s
		for index in currIndexArr:
			img = feature_extractor(data[index], width,height)
			for x in range(width*height):
				if (img[x] == 1):
					imgFreq[curr][x] += 1
			
		curr += 1
	
	# Part 2 : LAPLACE
	global logImg
	#logImg = [[0] * (width * height) for i in range(10)]
	logImg = []
	global laplaceSum
	laplaceSum = [0,0,0,0,0,0,0,0,0,0]
	
	
	curr = 0
	while curr <= 9:
		currMap = imgFreq[curr]
	
		mapDomain = getDomainList(currMap)
		
		# LAPLACE K VALUE
		#laplaceK =0.00000000000000000000000000000001 # 0.716
		laplaceK = 0.00000000000001 # minimum amt of 0s for 71.6%
		lSum = 0
		
		condProb = 0
		finalProb = 0
		currProbabilities = []
		#print ("CURR: " + str(curr))
		for j in range(0, len(currMap)):
			numerator = currMap[j]
			numerator += laplaceK
			
			denominator = sampleSize
			denominator += (len(mapDomain) * laplaceK)
			
			
			prob = np.log(float(numerator)/denominator)
			#print ("J:" + str(j) + " " + str( (numerator, denominator, prob) ))
			
			currProbabilities.append(prob)
			condProb += prob
		
		#print ("Prior Prob: " + str((arrIntegerFreq[curr], sampleSize,float(arrIntegerFreq[curr])/sampleSize )))
		priorProb = np.log(float(arrIntegerFreq[curr])/sampleSize)
		finalProb = condProb + priorProb
		
		logImg.append(currProbabilities)
		laplaceSum[curr] = finalProb
		#print mapDomain
		#print currMap
		curr += 1
		
	#outside loop
	# print ("LAPLACE TOTAL SUM")
	#print (arrIntegerFreq)
	#print (laplaceSum)
	# print (logImg[0])
	# print ()
	
	return 0


'''
For the given features for a single digit image, compute the class 
'''

def compute_class(features):

	predicted = -1
	#print ()
	#print features

	occurance = []
	for i in range(0, len(features)):
		if features[i] == 1:
			occurance.append(i)

	maxPred = -(sys.maxint - 1)
	curr = 0
	while curr <= 9:
		logSum = 0
		for x in occurance:
			logSum += logImg[curr][x]
		maxPred = max(maxPred, logSum)
		predicted = curr if maxPred == logSum else predicted
		curr+= 1
	
	
	return predicted


'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''


def classify(data, width, height, feature_extractor):
	predicted = []
	
	index = 0
	while index < len(data):
		img = feature_extractor(data[index],width,height)
		prediction = compute_class(img)
		predicted.append(prediction)
		#break
		index += 1
	
	
	#Your code starts here #
	#Your code ends here #
	
	return predicted
