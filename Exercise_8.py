def SumOfThe(N, data):
	allPositiveNumSum = 0
	allNegativeNumSum = 0
	res = 0

	for i in range(N):
		if data[i] >= 0:
			allPositiveNumSum += data[i]
		else:
			allNegativeNumSum += data[i]

	res = (allPositiveNumSum + allNegativeNumSum) / 2

	return(int(res))
