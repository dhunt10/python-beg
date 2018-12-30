

num = input("give a number")

if num>0:
	print(num, "is a positive number.")
elif num == 0:
	print(num, "is zero")
else:
	print 'Negative'

for x in range (1,100):
	if x%2==0:
		print "found an even number",x
		continue

