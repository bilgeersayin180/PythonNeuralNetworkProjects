import math
import random as r
game_coef = 1
x0_vector = [1,2,3,5,6,7, 9,10,11,13,14,15,17,18,19]
x1_vector = [4,4,4,8,8,8,12,12,12,16,16,16,20,20,20]
outputList =[1,1,1,1,1,1,1 ,1, 1, 1, 1, 1, 1, 1, 1]
w0 = r.uniform(0.75 , 0.80)
w1 = r.uniform(0.75 , 0.80)
print("W0 before training: ",w0)
print(" ")
print("W1 before training: ",w1)
print(" ")
for training_before_16 in range(0,20000):
    for i in range(0,len(x0_vector)):
        x0 = x0_vector[i]
        x1 = x1_vector[i]
        training_output = outputList[i]
        net = math.tanh((x0 * w0) + (x1 * w1))
        error = (training_output - net)
        w0 += (error * x0 * net)
        w1 += (error * x1 * net)
print("----------------------")
print("W0 after training: ",w0)
print(" ")
print("W1 after training: ",w1)
print(" ")
#print("W1 after training: ",w1)
#print(" ")
num = 0
Num = 0
NNP = 0
Neural_Network_Prediction = 0
while((num <= 21) or (Neural_Network_Prediction <= 21)):
    #Enter a number between 1 and 21: 
    num = int(input("Enter: "))
    Neural_Network_Prediction = round(((num * w0) + (game_coef * w1)))
    print("Neural Network prediction = ", Neural_Network_Prediction)
    print(" ")
    if((num == 21) or (Num == 21)):
        print(" ")
        print("Neural Network won, you lost.")
        break
    elif((Neural_Network_Prediction >= 21) or (NNP >= 21)):
        print(" ")
        print("Neural Network lost, you won.")
        break
