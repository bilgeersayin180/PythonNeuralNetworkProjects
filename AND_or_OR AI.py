import math
import random as r
x0_list =     [1,0,1,0,1,0,1,0] #input_1
x1_list =     [0,1,1,0,0,1,1,0] #input_2
x2_list =     [0,0,0,0,1,1,1,1] #Logic_Gate
output_list = [0,0,1,0,1,1,1,0] #Results
w0 = r.random()
w1 = r.random()
w2 = r.random()
for training in range(0,20000):
    for j in range(0,len(output_list)):
        x0 = x0_list[j]
        x1 = x1_list[j]
        x2 = x2_list[j]
        output = output_list[j]
        neuron = math.sin((x0 * w0) + (x1 * w1) + (x2 * w2))
        #print("--------------------------")
        #print("Training output: ",neuron)
        error_value = output - neuron
        w0 += (error_value * x0 * math.asin(neuron))
        w1 += (error_value * x1 * math.asin(neuron))
        w2 += (error_value * x2 * math.asin(neuron))

while (True):
    X0 = int(input("Enter x0 value: (It should be 0 or 1)"))
    X1 = int(input("Enter x1 value: (It should be 0 or 1)"))
    X2 = int(input("Enter gate key value: (It should be 0 or 1)"))
    result = math.sin((X0 * w0) + (X1 * w1) + (X2 * w2))
    print("Result: ",result)
        
    


