import numpy as np
data = np.array([
                [10,20,30,40,50], 
                [20,30,40,50,60], 
                [30,40,50,60,70], 
                [40,50,60,70,80]                
                ])

weight =  [25, 45, 10, 12, 8]

#Calculate Normalisation Matrix
def normalisation (data):      
    norm = np.linalg.norm(data)
    normal_array = data/norm
    print("Normalised Array :")
    print(normal_array)
    return normal_array

#Calculate Weighted Normalised matrix 
def weighNorm (NoramlArray):
    weighted = NormalArray * weight
    print("weighted Normalised Matrix :")
    print (weighted)
    return weighted

def concordance(data = data, weight = weight):
    
    
    n,m = len(data),len(data[0])
    res = []
    for i in range(n):
        ws = []
        for j in range(n):
            w = 0
            if i != j : 
                for k in range(m):
                        if data[i][k] >= data[j][k]:
                            w+=weight[k]
            ws.append(w)
        res.append(ws)
    return np.array(res) 

def PureConcordanceIndex (data):
    n,m = len(data),len(data[0])
    sumMatrix = 0
    for i in range(n):
        for j in range(m):
            sumMatrix = sumMatrix + data[i][j]
    TotalVal = (n * m) - n #total number of non zero values in matrix
    ConcordanceIndex =  sumMatrix / TotalVal
    #print (ConcordanceIndex)
    return (ConcordanceIndex) 

def PureConcordanceMatrix (data , index):   
    n,m = len(data),len(data[0])
    
    for i in range(n):
        for j in range(m):
            if data[i][j] > index:
                data[i][j] = 1
            
    return data



def diccordance(data = data, weight = weight):
    
    
    n,m = len(data),len(data[0])
    res = []
    for i in range(n):
        ws = []
        for j in range(n):
            w = 0
            if i != j : 
                for k in range(m):
                        if data[i][k] <= data[j][k]:
                            w+=weight[k]
            ws.append(w)
        res.append(ws)
    return np.array(res)          

def PureDiscordanceIndex (data):
    n,m = len(data),len(data[0])
    sumMatrix = 0
    for i in range(n):
        for j in range(m):
            sumMatrix = sumMatrix + data[i][j]
    TotalVal = (n * m) - n #total number of non zero values in matrix
    DiscordanceIndex =  sumMatrix / TotalVal
    #print (DiscordanceIndex)
    return DiscordanceIndex

def PureDiscordanceMatrix (data , index):   
    n,m = len(data),len(data[0])
    
    for i in range(n):
        for j in range(m):
            if data[i][j] > index:
                data[i][j] = 1
            
    return data


if __name__ == "__main__":
    print ("Input Data is : ")
    print(data)
    
    print("Weight Of the Matrix is : ")
    print(weight)
    
    NormalArray = normalisation(data) #Calculate Normalisation
    
    weightNormalArray  = weighNorm(NormalArray) #Calculate Weighted Normalised matrix 

    ConcordanceMatrix = concordance (weightNormalArray,weight)
    print("Concordance matrix is : ")
    print(ConcordanceMatrix)

    DiscordanceMatrix = diccordance (weightNormalArray,weight)
    print("discordance matrix is : ")
    print(DiscordanceMatrix)

    print("Pure Concordance Index is : ")
    ConcordanceIndex = PureConcordanceIndex(ConcordanceMatrix)
    print (ConcordanceIndex)

    print("Pure Discordance Index is : ")
    DiscordanceIndex = PureDiscordanceIndex(DiscordanceMatrix)
    print(DiscordanceIndex)

    print ("Pure Concordance Matrix is : ")
    ConcordanceMatrix  = PureConcordanceMatrix(ConcordanceMatrix , ConcordanceIndex)
    print(ConcordanceMatrix)

    
    print ("Pure Discordance Matrix is : ")
    DiscordanceMatrix  = PureDiscordanceMatrix(DiscordanceMatrix , DiscordanceIndex)
    print(DiscordanceMatrix)




