# Python3 program for implementation of FCFS  
# scheduling with different arrival time  
from configManager import *
from fifo import *
# Function to find the waiting time 
# for all processes  


# Driver code  
if __name__ =="__main__": 
    
    # Process id's  
    processes = ConfigManager.getProcessesIds()
    n = ConfigManager.getNumberOfProcessess()
  
    # Burst time of all processes  
    burst_time = ConfigManager.getProcessesBurstTime()  
  
    # Arrival time of all processes  
    arrival_time = ConfigManager.getProcessesArrivalTime() 
    
    Fifo.findavgTime(processes, n, burst_time, arrival_time) 
  
# This code is contributed 
# Shubham Singh(SHUBHAMSINGH10) 