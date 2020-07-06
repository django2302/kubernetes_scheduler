import numpy as np

data = np.array([
                [10,20,10,10], 
                [10,3,2,3], 
                [30,10,30,10]                
                ])

weight =  [20, 15, 40, 25]

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

def Ideal_best (data):
    best = []
    best = np.amax(data, axis=0)
    print("Ideal Best Array Is : ")
    print(best)
    return best

def Ideal_worst (data):
    worst = []
    worst = np.amin(data, axis = 0)
    print("Ideal worst is :")
    print(worst)
    return worst


def Euclidian_best (data , Id_best):
    n, m = len(data), len(data[0])
    Euc_best = []
    Tmp = 0
    for i in range(n):
        for j in range(m):
            Tmp = Tmp + (data[i][j]-Id_best[i])**2
        Tmp = Tmp**(1/2)
        Euc_best.append(Tmp)
    print("Best Euclidiean Distance : ")
    print(Euc_best)
    return Euc_best

def Euclidian_worst (data , Id_worst):
    n, m = len(data), len(data[0])
    Euc_worst = []
    Tmp = 0
    for i in range(n):
        for j in range(m):
            Tmp = Tmp + (data[i][j]-Id_worst[i])**2
        Tmp = Tmp**(1/2)
        Euc_worst.append(Tmp)
    print("worst Euclidiean Distance : ")
    print(Euc_worst)
    return Euc_worst

def performance_score (Id_best, Id_worst):
    n = len(Id_best)
    per_score = []
    Tmp = 0
    for i in range(n):
        print((Id_best[i] + Id_worst[i]))
        Tmp = Id_worst[i]/(Id_best[i] + Id_worst[i])
        per_score.append(Tmp)
    print("Performance Score : ")
    print(per_score)
    return per_score

if __name__ == "__main__":
    print ("Input Data is : ")
    print(data)
    
    print("Weight Of the Matrix is : ")
    print(weight)
    
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

    print("Best alternate is : " + str(BestAlternate + 1 ))
