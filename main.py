from configManager import *

if __name__ =="__main__": 

    types = ConfigManager.getSchedulersTypes()
    for i in types:
        if(i == "FCFS"):
            from FCFS import *
        if(i == "RR"):
            import RR
        if(i == "SJF"):
            import SJF

