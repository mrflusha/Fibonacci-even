def fib(x):
	fib_1 = 0
	fib_2 = 1
	fib_even = [0]


	while len(fib_even) < x:
		if fib_2 % 2 == 0:
			fib_even.append(fib_2)
		fib_sum = fib_1 + fib_2 
		fib_1 = fib_2
		fib_2 = fib_sum
		#print(fib_even)

	return fib_even
