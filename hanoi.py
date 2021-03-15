# Python function to solve tower of hanoi
# I have moved the disks onto other rods, without the small disk being under a big disk
#  

def TowerOfHanoi(n , source, destination, auxiliary): 
	if n==1: 
		print("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination) 
	print("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source) 
		
# This is the driver code 
n = 4
TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods 
