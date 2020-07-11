import sys
import numpy as np
from configManager import *

def disp(x, s):
	sys.stdout.write("\033[;1m")  #BOLD headings
	#print(s)
	sys.stdout.write("\033[0;0m") #RESET to normal(default)
	for i in range(count):
		print ('P' + str(i+1) + '\t' + str(x[i]))

def fileRead(arriv, burst, number_processes):
	sigma_burst = ConfigManager.getStandardDeviationBurstTime()
	mu_arrival = ConfigManager.getAverageArribalTime()
	sigma_arrival = ConfigManager.getStandardDeviationArribalTime()
	number_processes = ConfigManager.getNumberOfProcessess()
	mu_burst = ConfigManager.getAverageBurstTime()
    
	i = 0
	for arrival_time in np.random.normal(mu_arrival, sigma_arrival, number_processes):
		arriv.append(int(arrival_time))
		i += 1
	
	i = 0
	for burst_time in np.random.normal(mu_burst, sigma_burst, number_processes):
		burst.append(int(burst_time))
		i += 1
	return number_processes		

def minIndex(l):

	m = count - 1
	while True:
		if (l < arriv[m]):
			m -= 1
		else:
			break
	return m	

def minValue(cop, n):
	new = []
	for i in range(n+1):
		new.insert(i, cop[i])
	return min(new)
		
def cal():
	n = 0
	last = 0
	copy = []
	for i in range(count):
		copy.insert(i, burst[i])
		
	line = arriv[0]	
	
	while True:
		#print (line)
		
		n = minIndex(line)
		n = minValue(copy, n)

		index = copy.index(n)
		#print copy[index]
		copy[index] -= 1
		#print (copy)
		
		line += 1
		
		if copy[index] == 0:
			last += 1
			copy[index] = 999999;
		#print(copy)	
		if last == count: 
			break	

def waiting(sum):
	sum = 0
	for i in range(count):
		wait.insert(i, (turn[i] - burst[i]))
		sum += wait[i]
	disp(wait, '\nWaiting Time')
	return sum

def turnaround(sum):
	sum = 0
	for i in range(count):
		turn.append(end[i] - arriv[i])
		sum += turn[i]
	disp(turn, '\nTurnaround Time')
	return sum
	
sum = 0
line = 0
count = 0
end = []
wait = []
turn = []
arriv = []
burst = []

count = fileRead(arriv, burst, count)
disp(arriv, '\nArrival Time')
disp(burst, '\nBurst Time')

cal()

sum = turnaround(sum)
avg = float(sum)/count
avg_tr = avg
print('\nAverage Turnaround Time : ' + str(avg_tr))

sum = waiting(sum)
avg = float(sum)/count
avg_ts = avg
print('\nAverage Waiting Time : ' + str(avg_ts))