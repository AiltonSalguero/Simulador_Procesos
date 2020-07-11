import sys
import numpy as np
from configManager import *

def disp(x, s):
	f.write("	"+s+ "\n")
	for i in range(count):
		f.write('		P' + str(i+1) + '\t' + str(x[i]) + "\n")

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

def cal(line):
	i = 0
	n = 0 
	copy = []
	line = arriv[0]
	for i in range(count):
		copy.insert(i, burst[i])

	while n != count:
		i = 0
		
		for i in range(count):
		
			if copy[i] != 999999:
				if copy[i] <= QT:
					line += copy[i]
					copy[i] = 999999;
					end.insert(i, line)
			
				elif copy[i] > QT:
					line += QT
					copy[i] -= QT
					#end.insert(i, line)			 			
			
				if copy[i] == 999999:
					n += 1
					#break
			#print i, copy	

def waiting(sum):
	sum = 0
	for i in range(count):
#		wait.insert(i, (turn[i] - burst[i]))
		wait.insert(i, (start[i] - arriv[i]))
		sum += wait[i]
	disp(wait, 'Waiting Time')
	return sum

def waiting(sum):
	sum = 0
	for i in range(count):
		wait.insert(i, (turn[i] - burst[i]))
#		wait.insert(i, (start[i] - arriv[i]))
		sum += wait[i]
	disp(wait, 'Waiting Time')
	return sum

def turnaround(sum):
	sum = 0
	for i in range(count):
		turn.insert(i, (end[i] - arriv[i]))
		sum += turn[i]
	disp(turn, 'Turnaround Time')
	return sum


f = open("results_RR.txt", "w")
f.write("RR Results\n")	
sum_tr_simulation = 0
sum_ts_simulation = 0

number_simulations = ConfigManager.getNumberSimulations()
for i in range(number_simulations):
	sum = 0
	line = 0
	count = 0
	end = []
	wait = []
	turn = []
	start = []
	arriv = []
	burst = []

	count = fileRead(arriv, burst, count)
	QT = ConfigManager.getQuantumTime()
	disp(arriv, 'Arrival Time')
	disp(burst, 'Burst Time')

	cal(line)

	disp(end, 'Completion Time')
	sum = turnaround(sum)
	avg = float(sum)/count
	avg_tr = avg
	f.write('	Average Turnaround Time : ' + str(avg_tr) + "\n")
	sum_tr_simulation += avg_tr

	sum = waiting(sum)
	avg = float(sum)/count
	avg_ts = avg
	f.write('	Average Waiting Time : ' + str(avg_ts) + "\n")
	sum_ts_simulation += avg_ts

	tpr = avg_tr/avg_ts
	f.write('	Average Retorn Time TR/TS : ' + str(tpr) + "\n")

f.write("SJF TS Total Average  " + str(sum_ts_simulation/number_simulations) + "\n")
f.write("SJF TR Total Average  " + str(sum_tr_simulation/number_simulations) + "\n")
f.close()
