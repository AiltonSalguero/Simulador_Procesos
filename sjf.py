from configManager import *

class Sjf:
    @staticmethod
    def arrangeArrival(num, mat):
        for i in range(num): 
            for j in range(num - i - 1): 
                if (mat[j][1] > mat[j + 1][1]):
                    for k in range(5):
                        temp = mat[j][k] 
                        mat[j][k] = mat[j + 1][k] 
                        mat[j + 1][k] = temp 

    @staticmethod
    def completionTime(num, mat): 
        val = -1 
        mat[0][3] = mat[0][1] + mat[0][2] 
        mat[0][5] = mat[0][3] - mat[0][1] 
        mat[0][4] = mat[0][5] - mat[0][2] 
  
        for i in range(1,num): 
            temp = mat[i - 1][3] 
            low = mat[i][2] 
            for j in range(i,num):
                if (temp >= mat[j][1] and low >= mat[j][2]):
                    low = mat[j][2] 
                    val = j 

            mat[val][3] = temp + mat[val][2] 
            mat[val][5] = mat[val][3] - mat[val][1] 
            mat[val][4] = mat[val][5] - mat[val][2] 
            for k in range(6):
                tem = mat[val][k]
                mat[val][k] = mat[i][k]
                mat[i][k] = tem

num = ConfigManager.getNumberOfProcessess()
processes = ConfigManager.getProcessesIds()
# Burst time of all processes  
burst_time = ConfigManager.getProcessesBurstTime()  
  
# Arrival time of all processes  
arrival_time = ConfigManager.getProcessesArrivalTime() 
mat = [ [ 0 for i in range(6) ] for j in range(num) ]
for i in range(num): 
    mat[i][0] = processes[i]
    mat[i][1] =  arrival_time[i]
    mat[i][2] = burst_time[i] 
print("Before Arrange...") 
print("Process ID\tArrival Time\tBurst Time") 
for i in range(num):
    print(" ", mat[i][0], "\t\t", mat[i][1], "\t\t", mat[i][2]) 
Sjf.arrangeArrival(num, mat) 
Sjf.completionTime(num, mat) 
print("Final Result...") 
print("Process ID\tArrival Time\tBurst" + 
                        " Time\tWaiting Time\tTurnaround Time") 
for i in range(num):
    print(" ", mat[i][0], "\t\t", mat[i][1], "\t\t", mat[i][2],  
                "\t\t",  mat[i][4], "\t\t ", mat[i][5]) 
