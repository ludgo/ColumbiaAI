
def swap(s, indexA, indexB):
	c = list(s)
	c[indexA], c[indexB] = c[indexB], c[indexA]
	return ''.join(c)

def writeFile(dic):
	with open('output.txt', 'w') as f:
		for key, value in dic.items():
			f.write('%s: %s\n' % (key, value))
