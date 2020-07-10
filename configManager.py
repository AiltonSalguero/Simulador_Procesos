import configparser
class ConfigManager:
    config = configparser.ConfigParser()  

    @staticmethod
    def getDataOf(key):
        ConfigManager.config.read('config.ini')
        processesKeys = ConfigManager.config['Processes'][key]
        processes = []
        for i in range(0,len(processesKeys)):
            charKey = processesKeys[i]
            if(charKey != "[" and charKey != "]" and charKey != "," and charKey != " "):
                processes.append(int(charKey))
        return processes

    @staticmethod
    def getProcessesIds():
        return ConfigManager.getDataOf('id')

    @staticmethod
    def getProcessesBurstTime():
        return ConfigManager.getDataOf('burst_time')

    @staticmethod
    def getProcessesArrivalTime():
        return ConfigManager.getDataOf('arrival_time')

    @staticmethod
    def getNumberOfProcessess():
        return len(ConfigManager.getDataOf('id'))