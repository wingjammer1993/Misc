
def rearrange(elements):
	binhash = {}
	binsorted = []
	for i in elements:
		binary = bin(i)[2:]
		count = binary.count('1')
		if count in binhash:
			ls = []
			if type(binhash[count]) == int:
				ls.append(binhash[count])
			else:
				ls.extend(binhash[count])
			ls.append(i)
			binhash[count] = ls
		else:
			binhash[count] = i

	sorted(binhash, key=binhash.get)
	for elem in binhash:
		if type(binhash[elem]) == int:
			binsorted.append(binhash[elem])
		else:
			binsorted.extend(sorted(binhash[elem]))

	return binsorted


k = rearrange([3, 1, 2, 3])
print(k)



