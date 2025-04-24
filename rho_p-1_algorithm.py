import math
import sympy

def pollard(n):
	a = 2
	i = 2
	
	while(True):
		a = (a**i) % n
		d = math.gcd((a-1), n)	
		if (d > 1):
			return d
			break
		i += 1

n = 21 #exmaple 
	
num = n
ans = []
	
while(True):	
	d = pollard(num)	
	ans.append(d)
	
	r = int(num/d)
	
	if(sympy.isprime(r)):	
		ans.append(r)
		break
	
	else:
		num = r

print("Prime factors of", n, "are", *ans)
