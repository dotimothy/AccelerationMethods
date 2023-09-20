import threading
import time

def square(a): 
	return a ** 2 

def squareTest(end=100000):
	squareList = []
	for i in range(end):
		squareList.append(square(i+1))
	return squareList
if __name__ =="__main__":
	start = time.time()
	print(squareTest())
	print(f'Completed in {time.time()-start} Seconds')