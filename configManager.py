import configparser
class ConfigManager:
    config = configparser.ConfigParser()  

    @staticmethod
    def getDataOfArray(group, key):
        ConfigManager.config.read('config.ini')
        processesKeys = ConfigManager.config[group][key]
        processes = []
        for i in range(0,len(processesKeys)):
            charKey = processesKeys[i]
            if(charKey != "[" and charKey != "]" and charKey != "," and charKey != " "):
                processes.append(int(charKey))
        return processes
    
    @staticmethod
    def getDataOfVariable(group, key):
        ConfigManager.config.read('config.ini')
        return ConfigManager.config[group][key]

    @staticmethod
    def getProcessesIds():
        return ConfigManager.getDataOfArray('Processes', 'id')
    
    @staticmethod
    def getSchedulersTypes():
        group = "Schedulers"
        key = "Types"
        ConfigManager.config.read('config.ini')
        processesKeys = ConfigManager.config[group][key]
        processes = []
        for i in range(0,len(processesKeys)):
            charKey = processesKeys[i]
            if(charKey != "[" and charKey != "]" and charKey != "," and charKey != " "):
                processes.append(charKey)
        return processes


    @staticmethod
    def getProcessesBurstTime():
        return ConfigManager.getDataOfArray('Processes','burst_time')

    @staticmethod
    def getProcessesArrivalTime():
        return ConfigManager.getDataOfArray('Processes','arrival_time')

    @staticmethod
    def getNumberOfProcessess():
        print(ConfigManager.getDataOfVariable('Processes','number_processes'))
        return int(ConfigManager.getDataOfVariable('Processes','number_processes'))

    @staticmethod
    def getProcessesMatrix():
        num = ConfigManager.getNumberOfProcessess()
        mat = [ [ 0 for i in range(6) ] for j in range(num) ]
        for i in range(num): 
            mat[i][0] = processes[i]
            mat[i][1] =  arrival_time[i]
            mat[i][2] = burst_time[i] 
        return mat

    @staticmethod
    def getAverageArribalTime():
        return int(ConfigManager.getDataOfVariable('Processes','average_arrival_time'))
    
    @staticmethod
    def getStandardDeviationArribalTime():
        return int(ConfigManager.getDataOfVariable('Processes','standard_deviation_arrival_time'))
    
    @staticmethod
    def getAverageBurstTime():
        return int(ConfigManager.getDataOfVariable('Processes','average_burst_time'))
    @staticmethod
    def getStandardDeviationBurstTime():
        return int(ConfigManager.getDataOfVariable('Processes','standard_deviation_burst_time'))

    @staticmethod
    def getQuantumTime():
        return int(ConfigManager.getDataOfVariable('Schedulers', 'quantum_time'))
    
    @staticmethod
    def getNumberSimulations():
        return int(ConfigManager.getDataOfVariable('Simulator', 'number_simulations'))