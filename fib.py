def fib(x):
	a = 0
	b = 1
	for i in range(x):
		a,b = b, a+b 
		print(a)

	return a



#out = fib(4) 

#print (out)

fib_1 = 0
fib_2 = 1
fib = list()
i = 0
x = 20
while i < x :
	if fib_2 % 2 == 0:
		fib.append(fib_2)
	fib_sum = fib_1 + fib_2 
	fib_1 = fib_2
	fib_2 = fib_sum
	i +=1
	print(fib)