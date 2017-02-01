# swap items at indexes and return copy of array
def swap(arr, indexA, indexB):
	c = list(arr)
	c[indexA], c[indexB] = c[indexB], c[indexA]
	return c

# separate array items by ,
def commaHash(l):
	return str(l).strip('[]')

# output output.txt for dictionary
def writeFile(dic):
	with open('output.txt', 'w') as f:
		for key, value in dic.items():
			f.write('%s: %s\n' % (key, value))
