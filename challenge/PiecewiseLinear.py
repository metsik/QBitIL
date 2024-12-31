from classiq import *

import numpy as np
import matplotlib.pyplot as plt
import random
import math


numPointsPerVector = 50
valuesRange = [0, 2*math.pi] #edges of the range
segNum =  6#number of segments
nodeNum = segNum + 1 #number of noder to define segNum sements between the edges
delta = (valuesRange[1]-valuesRange[0])/segNum #the length of each segment
localDelta = delta/numPointsPerVector #length of each pieace in a single line

def generateComponentIndex(): #generate the input values in which the sin x will be aproximated
    nodeIndexVec = []
    for componentIndex in range(nodeNum):
        nodeIndexVec.append(componentIndex*delta)
    return nodeIndexVec

def generateNodeValueVec(nodeIndexVec): #generate the actual sine values at nodeIndexVec
    nodeValueVec = []
    for componentIndex in range(nodeNum):
        nodeValueVec.append(np.sin(nodeIndexVec[componentIndex]))
    return nodeValueVec

def calculateSlopes(nodeIndexVec, nodeValueVec): #for each segment, calculate the slope
    slopeVec = []
    for componentIndex in range(segNum):
        a = (nodeValueVec[componentIndex+1]- nodeValueVec[componentIndex])/delta
        slopeVec.append(a)
    return slopeVec

def calculateb(nodeIndexVec, nodeValueVec,a):
    bVec = []
    for componentIndex in range(segNum):
        b =  nodeValueVec[componentIndex] - a[componentIndex]*nodeIndexVec[componentIndex]
        bVec.append(b)
    return bVec

def calcSpecificLinearEqationVec(startNode, endNode, a, b): #calculate the values of the approximation of each segment between itsd respective edges
    
    funcVector = np.zeros(numPointsPerVector)
    lineInputs = np.zeros(numPointsPerVector)

    for valIndex in range(numPointsPerVector):
        x = startNode+valIndex*localDelta
        lineInputs[valIndex] = x
        funcVector[valIndex] = a*x+b
    return funcVector, lineInputs



nodeIndexVec = generateComponentIndex()
nodeValueVec = generateNodeValueVec(nodeIndexVec)
aVec = calculateSlopes(nodeIndexVec,nodeValueVec)
bVec = calculateb(nodeIndexVec, nodeValueVec, aVec)
y = np.empty((0,numPointsPerVector)) #init the y matrix. this mattix's rows will be the linear approximations of the sine function
x = np.empty((0,numPointsPerVector)) #init the x values matrix corresponding to the y values
for i in range(segNum):
    startNode = nodeIndexVec[i]
    endNode = nodeIndexVec[i+1]
    a = aVec[i]
    b = bVec[i]
    yVec, xVec = calcSpecificLinearEqationVec(startNode,endNode, a, b)
    y = np.vstack([y, yVec])
    x = np.vstack([x, xVec])

# Function to generate a random color 
def random_color():
    return (random.random(), random.random(), random.random())
colorPallet = ['red', 'green', 'blue', 'brown', (0.1, 0.2, 0.5)]
for i in range(y.shape[0]):  
    # colorPallette = ()random_color()
    plt.plot(x[i, :], y[i, :], color = colorPallet[i], label=f'Line {i+1}', linestyle=':')
plt.show()

    
# @qfunc
# def main(x:Output[QNum], y: Output[QNum]):
#     a = 2
#     b = 1
#     allocate_num(num_qubits=4,is_signed=False,fraction_digits=0,out=x)
#     hadamard_transform(x)
#     # linear_func(a,b,x,y)
#     sin()

# qmod = create_model(main)
# quantum_program = synthesize(qmod)
# show(quantum_program)
# job = execute(quantum_program)
# job.open_in_ide() # View the resulting histogram in the IDE