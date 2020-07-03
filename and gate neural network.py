import math
import random as r
x0_list = [1,0,1,0]
x1_list = [0,1,1,0]
output_list = [0,0,1,0]
w0 = r.random()
w1 = r.random()
for i in range(0,100):
    for j in range(0,len(output_list)):
        x0 = x0_list[j]
        x1 = x1_list[j]
        output = output_list[j]
        neuron = math.tanh((x0 * w0) * (x1 * w1))
        print("--------------------------")
        print("Training output: ",neuron)
        error_value = output - neuron
        w0 += (error_value * x0 * math.atanh(neuron))
        w1 += (error_value * x1 * math.atanh(neuron))
        
        



