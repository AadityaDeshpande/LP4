import numpy as np


setA = [1/2,0.3/4,0.5/6,0.2/8]
setB = [0.5/2,0.4/4,0.1/6,1/8]
setC = []
setD = []
setCompA = []
setCompB = []
setDiffAB = []
setDiffBA = []
maxmin = []



def union():
    for i in range(len(setA)):
        setC.append(max(setA[i], setB[i]))
    return setC



print('UNION: ',union())




def intersection():
    for i in range(len(setA)):
        setD.append(min(setA[i], setB[i]))
    return setD



print('INTERSECTION: ',intersection())



def complement():
    for i in range(len(setA)):
        setCompA.append(1 - (setA[i]))
        setCompB.append(1 - (setB[i]))
    return setCompA, setCompB


print('COMPLEMENT: ',complement())



def diff():
    for i in range(len(setA)):
        setDiffAB.append(setA[i] - (1 - setB[i]))
        setDiffBA.append(setB[i] - (1 - setA[i]))
    return setDiffAB, setDiffBA   

print('DIFFERENCE: ',diff())


def findCardinality():
    return pow(2,len(setA))

print('CARDINALITY: ',findCardinality())



def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

setA = np.array([[1, 0, .7],[.3, .2, 0],[0, .5, 1]])
setB = np.array([[.6, .6, 0],[0, .6, .1],[0, .1, 0]])


print('R1oR2 => Max-Min : ',str(maxMin(setA, setB))) 

