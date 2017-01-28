def swap(s, indexA, indexB):
	c = list(s)
	c[indexA], c[indexB] = c[indexB], c[indexA]
	return ''.join(c)

