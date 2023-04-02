import math
bias = float(input("enter the value for bias : "))
n = int(input("Enter the number of input neurons : "))

print("Bias value is : ",bias)
print("U decided to go with ",n," input neurons.")

weights = []
inputs = []

for i in range(0,n):
    a = float(input("Enter input value : "))
    inputs.append(a)

    b = float(input("Enter weight value : "))
    weights.append(b)

print("Weights are : ")
print(weights)

print("Inputs are : ")
print(inputs)

net_inp = bias

for i in range(0,n):
    net_inp = net_inp + (weights[i] * inputs[i])

print("Net Input is : ",net_inp)

##Calculating output using Binary sigmoidal activation function

binary_op = 1 / (1 + math.exp(-net_inp))

print("Output using Binary sigmoidal activation function : ",round(binary_op,3))


#Calculating output using Bi-polar sigmoidal activation function

bipolar_op = (1 - math.exp(-net_inp)) / (1 + math.exp(-net_inp))

bipolar_op_2 = -1 + ( 2/(1 + (math.exp(-net_inp))))

print("Output using Bi-polar sigmoidal activation function : ",round(bipolar_op,3))

print("Output using Bi-polar sigmoidal activation function 2 : ",round(bipolar_op_2,3))


    
