import numpy as np
import statistics as stt
import matplotlib.pyplot as plt

ATMs = [0, 0, 0]
Total_ST_ATMs = [0, 0, 0]

IAT =  np.random.exponential(1, 1000000)

ST_First = np.random.uniform(2, 4, 1000000)
ST_Second =  np.random.triangular(2,  3.3, 4, 1000000)
ST_Third = np.random.normal(3, 0.5 , 1000000)
Arrival_Time = list()
Start_Time = list()
Completion_Time = list()
Waiting_Time = list()

Arrival_Time.append(0)
Start_Time.append(0)
Completion_Time.append(0)
Waiting_Time.append(0)


Num_of_Waited = 0
Num_of_Waited_more1 = 0

for i in range (1,1000000):
    Arrival_Time.append(Arrival_Time[i-1]+IAT[i-1])
    index_min = np.argmin(ATMs)
    Start_Time.append(max(Arrival_Time[i],min(ATMs)))
    Waiting_Time.append(Start_Time[i]-Arrival_Time[i])
    if index_min == 0:
        Completion_Time.append(Start_Time[i]+ST_First [i-1])
        Total_ST_ATMs[0] += ST_First[i-1]
    elif index_min == 1:
        Completion_Time.append(Start_Time[i]+ST_Second[i-1])
        Total_ST_ATMs[1] += ST_Second[i-1]
    else:
        Completion_Time.append(Start_Time[i]+ST_Third [i-1])
        Total_ST_ATMs[2] += ST_Third[i-1]

    ATMs[index_min] = Completion_Time[i]

    if Waiting_Time[i] > 0:
        Num_of_Waited += 1
        if Waiting_Time[i] > 1:
            Num_of_Waited_more1 += 1


Utilization_First  = Total_ST_ATMs[0] / max(ATMs)
Utilization_Second = Total_ST_ATMs[1] / max(ATMs)
Utilization_Third  = Total_ST_ATMs[2] / max(ATMs)



print ("Average Waiting Time: ", stt.mean(Waiting_Time))
print ("Probability of Waiting: ", Num_of_Waited/1000000)
print ("Probability of Waiting more than 1 minute: ", Num_of_Waited_more1/1000000)
print ("Maximum Waiting Time: " , max(Waiting_Time))
print ("Utilization of the first ATM machine: ", Utilization_First)
print ("Utilization of the second ATM machine: ", Utilization_Second)
print ("Utilization of the third ATM machine: ", Utilization_Third)

print ("First 10 Customers: ")
for i in range(1,11):
    print (i, "- ")
    print ("AT:       ", Arrival_Time[i])
    print ("Start   : ", Start_Time[i])
    print ("Service : ", Completion_Time[i]-Start_Time[i])
    print ("Complete: ", Completion_Time[i])
    print ("----")
