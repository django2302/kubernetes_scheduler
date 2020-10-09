import numpy as np
import sys
import os
import paramiko
import math
#data = np.array([[10,20,10,10],[10,3,2,3],[30,10,30,10]])

weight =  [40, 20, 20, 10, 10]
#[20, 15, 15, 20, 10, 10, 10]


def normalisation (data):
    sqrMtrx = np.square(data)
    sumMatrx = np.sum(sqrMtrx , axis=0)
    sqRoot = np.sqrt(sumMatrx)
    sqRoot = np.around(sqRoot , decimals=2)
    divideArray = np.divide(data , sqRoot)
    #print("Normalised Array is :")
    #print(divideArray)

    return divideArray


#Calculate Weighted Normalised matrix 
def weighNorm (NoramlArray):
    weighted = NormalArray * weight
    #print("weighted Normalised Matrix :")
    #print (weighted)
    return weighted

def Ideal_best (data):
    best = []
    best = np.amax(data, axis=0)
    #print("Ideal Best Array Is : ")
    #print(best)
    return best

def Ideal_worst (data):
    worst = []
    worst = np.amin(data, axis = 0)
    #print("Ideal worst is :")
    #print(worst)
    return worst


def Euclidian_best (data , Id_best):
    n, m = len(data), len(data[0])
    Euc_best = []
    Tmp = 0
    for i in range(n):
        for j in range(m):
            Tmp = Tmp + (data[i][j]-Id_best[j])**2
        Tmp = math.sqrt(Tmp)
	#Tmp = Tmp**(1/2)
        Euc_best.append(Tmp)
    #print("Best Euclidiean Distance : ")
    #print(Euc_best)
    return Euc_best

def Euclidian_worst (data , Id_worst):
    n, m = len(data), len(data[0])
    Euc_worst = []
    Tmp = 0
    for i in range(n):
        for j in range(m):
            Tmp = Tmp + (data[i][j]-Id_worst[j])**2
        Tmp = math.sqrt(Tmp)
	#Tmp = Tmp**(1/2)
        Euc_worst.append(Tmp)
    #print("worst Euclidiean Distance : ")
    #print(Euc_worst)
    return Euc_worst

def performance_score (Id_best, Id_worst):
    n = len(Id_best)
    per_score = []
    Tmp = 0
    for i in range(n):
        #print((Id_best[i] + Id_worst[i]))
        Tmp = Id_worst[i]/(Id_best[i] + Id_worst[i])
        per_score.append(Tmp)
    #print("Performance Score : ")
    #print(per_score)
    return per_score

def connect (host):	
	    #system values in order of CPU , RAM, Storage, Network
	    system_values = []

            # Connect to remote host
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username='admin', key_filename='/home/admin/.ssh/id_rsa')

            # Setup sftp connection and transmit this script
            #sftp = client.open_sftp()
            #sftp.put(__file__, '/tmp/CPU.py')
            #sftp.close()

            
            # SSHClient.exec_command() returns the tuple (stdin,stdout,stderr)
            stdout = client.exec_command('python /home/admin/systemConfiguration.py')[1]
            for line in stdout:
                # Process each line in the remote output
                system_values.append(line)

            client.close()
            system_values = [int(i) for i in system_values]
            return (system_values)
	    sys.exit(0)
            

if __name__ == "__main__":
    hosts = ['192.168.56.102','192.168.56.103','192.168.56.104']
    systemValues = []
    for h in hosts:
		systemValues.append(connect(h))
	#systemValues = list(map(int, systemValues))
	
    data = np.array(systemValues)
    #print ("Input Data is : ")
    #print(data)

    
    #print(data)
    
    #print("Weight Of the Matrix is : ")
    #print(weight)
    
    NormalArray = normalisation(data) #Calculate Normalisation
    
    weightNormalArray  = weighNorm(NormalArray) #Calculate Weighted Normalised matrix 

    #calculate Ideal Best
    BestArray = Ideal_best(weightNormalArray) 

    #calculate Ideal Worst array 
    WorstArray = Ideal_worst(weightNormalArray)

    #calculate Euclidian distance 
    EucBest = Euclidian_best(weightNormalArray, BestArray)

    #calculate Worst Eucledean distance
    EucWorst = Euclidian_worst(weightNormalArray, WorstArray)

    #calculate Performance Score
    PerScore = performance_score(EucBest , EucWorst)

    BestAlternate = PerScore.index(max(PerScore))

    print(hosts[BestAlternate])


