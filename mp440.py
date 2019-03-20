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
	# converts into a 1D array of 0s and 1s
	for x in range(width):
		for y in range(height):
			if digit_data[x][y] > 0:
				features.append(1)
			else:
				features.append(0)
	
	return features


'''
Extract advanced features that you will come up with
'''
def removeDots(currRow):
	# If the left and right side are both non-zeros and the current value is a 0,
	# change sandwiched value to zero
	index = 0
	while index < len(currRow) - 1:
		
		if index > 0:
			prevVal = currRow[index - 1]
			nextVal = currRow[index + 1]
			
			if prevVal != 0 and nextVal != 0 and currRow[index] == 0:
				currRow[index] = int((prevVal + nextVal) / 2)
		
		index += 1
	return currRow

def deepcopy(digit_data, width, height):
	newDigit = [[0 for c in range(width)] for r in range(height)]
	for r in range(width):
		for c in range(height):
			newDigit[r][c] = digit_data[r][c]
	
	return newDigit
	
def featuresV1(newDigit, width, height):
	# Noise clean up

	# Check all 8 spots around current position, if there is only 1 nonzero, remove current pixel
	
	
	for r in range(width):
		for c in range(height):
			line = []
			if (r > 0 and r < width - 1 and c > 0 and c < height - 1):
				if newDigit[r - 1][c - 1] != 0:
					line.append(1)
				if newDigit[r - 1][c] != 0:
					line.append(1)
				if newDigit[r - 1][c + 1] != 0:
					line.append(1)
				if newDigit[r][c - 1] != 0:
					line.append(1)
				if newDigit[r][c + 1] != 0:
					line.append(1)
				if newDigit[r + 1][c - 1] != 0:
					line.append(1)
				if newDigit[r + 1][c] != 0:
					line.append(1)
				if newDigit[r + 1][c + 1] != 0:
					line.append(1)

			if (len(line) < 2):
				newDigit[r][c] = 0

	for row in range(width):
		currRow = newDigit[row]

		# remove singular random 0s
		newDigit[row] = removeDots(currRow)

		# extraneous values at edge
		newDigit[row][0] = 0
		newDigit[row][width - 1] = 0

	return newDigit

def featuresV2(newDigit, width, height):
	# only 1s, exceptions made if theres a line of just 2s

	for x in range(width):
		for y in range(height):
			# exception for 2s
			if (newDigit[x][y] == 2) and (not 1 in newDigit[x]):
				newDigit[x][y] = 1
			elif (newDigit[x][y] == 1):
				newDigit[x][y] = 1
			else:
				newDigit[x][y] = 0

			# no exception for 2s
			# if (digit_data[x][y] == 1):
			# 	digit_data[x][y] = 1
			# else:
			# 	digit_data[x][y] = 0

	return newDigit

def featuresV3(set1, set2, width, height, newDigit):
	
	
	for r in range(height):
		for c in range(width):
			v1Val = set1[r][c]
			v2Val = set2[r][c]
			newDigit[r][c] = (float(v1Val) + float(v2Val))/2
	
	return newDigit
	

def extract_advanced_features(digit_data, width, height):

	# Feature v1: clean up noise
	features = []
	
	newDigit = deepcopy(digit_data, width, height)
	
	set1 = featuresV1(newDigit, width, height)  # 80.6 alone
	
	set2 = featuresV2(newDigit, width, height)  # 80.7 alone
	set3 = featuresV3(set1, set2, width, height, newDigit)
	
	
	# V1 + V2 = 80.0 %
	for x in range(width):
		for y in range(height):
			if set3[x][y] == 1:
				features.append(1)
			else:
				features.append(0)

	return features


'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
	
	# #Assuming this method means choose which of the two extract methods to use
	# featuresBasic = extract_basic_features(digit_data, width, height)
	# featuresAdvanced = extract_advanced_features(digit_data, width, height)
	# featuresFinal = []
	#
	#
	# for index in range(width*height):
	# 	basVal = featuresBasic[index]
	# 	advVal = featuresAdvanced[index]
	# 	finalVal = (float(basVal) + float(advVal)) / 2
	# 	featuresFinal.append(finalVal)
		
	return extract_basic_features(digit_data,width,height)


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
def compute_statistics(data, label, width, height, feature_extractor, percentage= 100.0):
	sampleSize = int(float(percentage / 100) * len(label))
	
	# === Get Statistics
	global labelFreq  # Counts how many times a specific label occurs
	global labelFreqIndex
	labelFreq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	labelFreqIndex = [[], [], [], [], [], [], [], [], [], []]
	
	for index in range(sampleSize):
		if label[index] == 0:
			labelFreq[0] += 1
			labelFreqIndex[0].append(index)
		elif label[index] == 1:
			labelFreq[1] += 1
			labelFreqIndex[1].append(index)
		elif label[index] == 2:
			labelFreq[2] += 1
			labelFreqIndex[2].append(index)
		elif label[index] == 3:
			labelFreq[3] += 1
			labelFreqIndex[3].append(index)
		elif label[index] == 4:
			labelFreq[4] += 1
			labelFreqIndex[4].append(index)
		elif label[index] == 5:
			labelFreq[5] += 1
			labelFreqIndex[5].append(index)
		elif label[index] == 6:
			labelFreq[6] += 1
			labelFreqIndex[6].append(index)
		elif label[index] == 7:
			labelFreq[7] += 1
			labelFreqIndex[7].append(index)
		elif label[index] == 8:
			labelFreq[8] += 1
			labelFreqIndex[8].append(index)
		elif label[index] == 9:
			labelFreq[9] += 1
			labelFreqIndex[9].append(index)
	
	# === PRIOR PROBABILITY P(Y) = c(y) / n
	global priorProb
	priorProb = []
	for i in range(0, 10):
		prior = np.log(float(labelFreq[i]) / sampleSize)
		priorProb.append(prior)
	
	# === CONDITIONAL PROBAILITY
	
	global freqMapTrue, freqMapFalse
	
	freqMapTrue = [[[0 for c in range(width)] for r in range(height)] for l in range(10)]
	freqMapFalse = [[[0 for c in range(width)] for r in range(height)] for l in range(10)]
	
	# Frequency map for true and false
	for imgIndex in range(0, sampleSize):
		img = feature_extractor(data[imgIndex], width, height)
		corresLabel = label[imgIndex]
		currTrueMap = freqMapTrue[corresLabel]
		currFalseMap = freqMapFalse[corresLabel]
		
		xIndex = 0
		for row in range(0, height):
			for col in range(0, width):
				if (img[xIndex] > 0):
					currTrueMap[row][col] += 1
				else:
					currFalseMap[row][col] += 1
				xIndex += 1
	
	
	global condTrue, condFalse
	condTrue = [[[0 for c in range(width)] for r in range(height)] for l in range(10)]
	condFalse = [[[0 for c in range(width)] for r in range(height)] for l in range(10)]
	
	laplaceK =  0.00001 # 0.00001 gives 0.825 basic and 0.82 advanced
	
	# Conditional Calculation
	for lIndex in range(0, 10):
		currCondTrue = condTrue[lIndex]
		currCondFalse = condFalse[lIndex]
		for r in range(height):
			for c in range(width):
				numTrue = float(freqMapTrue[lIndex][r][c] + laplaceK)
				numFalse = float(freqMapFalse[lIndex][r][c] + laplaceK)
				domain = 2 # 0 and 1
				denom = float(labelFreq[lIndex] + domain * laplaceK)
				
				currCondTrue[r][c] = np.log(numTrue / denom)
				currCondFalse[r][c] = np.log(numFalse / denom)


'''
For the given features for a single digit image, compute the class
'''
def compute_class(features):
	predicted = -1
	
	# Log of prior probabilities summed with conditional probabilities where pixel = true
	logSums = list(priorProb)
	
	# sum up priors and conditional
	for label in range(0, len(condTrue)):
		xIndex = 0
		for row in range(0, len(condTrue[0][0])):
			for col in range(0, len(condTrue[0][0])):
				if features[xIndex] == 1:
					logSums[label] += condTrue[label][row][col]
				else:
					logSums[label] += condFalse[label][row][col]
				xIndex += 1
	
	# check for best value
	maxPred = float("-inf")
	for i in range(0, len(logSums)):
		if logSums[i] > maxPred:
			maxPred = logSums[i]
			predicted = i
			
	return predicted


def classify(data, width, height, feature_extractor):
	predicted = []
	
	index = 0
	while index < len(data):
		img = feature_extractor(data[index], width, height)
		prediction = compute_class(img)
		predicted.append(prediction)
		# break
		index += 1
	
	return predicted
