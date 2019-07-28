# Part 2 of the Python Review lab.

def encode(x, y):
	if 1<y<250 and 500<x<1000:
		return y*x
	else:
		print("invalid input:outside range")
		for i in range(2, x):
			if (x%i) == 0:
				print("not prime")
				return False 

	
		# 	if (x%i) == 0:
		# 		print("this is not prime")
		# 	else:
		# 		print("this is prime")
		# for i in range(2,y//2):
		# 	if (y%i) == 0:
		# 		print("this is not prime")
		# 	else:
		# 		print("this is prime")



def decode(coded_message):
	pass

def is_prime(x):
	not_prime = True
	while not_prime:
		for i in range(2, x):
			if (x%i) == 0:
				print("not prime")
				x+= 1 
		else:
			not_prime = False 
	return x		


