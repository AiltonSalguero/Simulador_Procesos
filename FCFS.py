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

def cal(sum):
	sum = arriv[0]
	for i in range(count):
		sum = sum + burst[i]
		end.insert(i, sum)
	disp(end, 'Completion Time')

def waiting(sum):
	sum = 0
	for i in range(count):
		wait.insert(i, (turn[i] - burst[i]))
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
	



f = open("results_FCFS.txt", "w")
f.write("FCFS Results\n")	
sum_tr_simulation = 0
sum_ts_simulation = 0

number_simulations = ConfigManager.getNumberSimulations()
for i in range(number_simulations):
	f.write("")
	f.write("Simulation " + str(i+1) +"\n")
	sum = 0
	count = 0
	end = []
	wait = []
	turn = []
	arriv = []
	burst = []

	count = fileRead(arriv, burst, count)
	disp(arriv, 'Arrival Time')
	disp(burst, 'Burst Time')

	cal(sum)

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

f.write("FCFS TS Total Average  " + str(sum_ts_simulation/number_simulations) + "\n")
f.write("FCFS TR Total Average  " + str(sum_tr_simulation/number_simulations) + "\n")
f.close()