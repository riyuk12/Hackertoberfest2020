a=int(input("enter number"))
if (a>2) and a%2!=0:
	for x in range(2,a,2):
		if a%x==0:
			print("not prime")
			break
	else:
		print("prime")