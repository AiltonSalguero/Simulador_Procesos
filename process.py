import numpy as np
from configManager import *

class Process:

    @staticmethod
    def generateProcesses():
        number_processes = ConfigManager.getNumberOfProcessess()
        
        mu_arrival = ConfigManager.getAverageArribalTime()
        sigma_arrival = ConfigManager.getStandardDeviationArribalTime()

        mu_burst = ConfigManager.getAverageBurstTime()
        sigma_burst = ConfigManager.getStandardDeviationBurstTime()
        
        processes = [[ 0 for i in range(6)] for j in range(number_processes)]
        for i in range(number_processes):
            processes[i][0] = i+1 #ID
        i = 0 
        for arrival_time in np.random.normal(mu_arrival, sigma_arrival, number_processes):
            processes[i][1] = int(arrival_time)
            i += 1

        i = 0
        for burst_time in np.random.normal(mu_burst, sigma_burst, number_processes):
            processes[i][2] = int(burst_time)
            i += 1
        return processes    


