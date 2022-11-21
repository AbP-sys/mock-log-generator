import random
import time

def generate_spike_data(lastEntry,current_time):
    f = open("cpulogs.txt", "a")
    peak_chance = random.randint(0, 100)
    is_peak = False

    if peak_chance < 20:  # 20% chance for generating a spike
        cpu = random.randint(lastEntry[0]+4000,lastEntry[0]+5000)
        mem = random.randint(lastEntry[1]+4000, lastEntry[1]+5000) 
        is_peak = True
    else:
        cpu = random.randint(lastEntry[0]-500,lastEntry[0]+500) 
        mem = random.randint(lastEntry[1]-500, lastEntry[1]+500) 
    if cpu >= 10000 or cpu <= 0:
        cpu = lastEntry[0]
    if mem >= 10000 or mem <= 0:
        mem = lastEntry[1]
    f.write(time.strftime("%d %b %Y %H:%M:%S",
             time.gmtime(current_time))+" CPU: "+str(cpu/100)+" Memory: "+str(mem/100)+"\n")
    if is_peak:
        return lastEntry
    if cpu > 6000 or mem > 6000: #reset on increasing trend
        return[3000,2500]

    return [cpu,mem]

def generate_const_data(lastEntry,current_time):
    f = open("cpulogs.txt", "a")
    cpu = random.randint(lastEntry[0]-500,lastEntry[0]+500) 
    mem = random.randint(lastEntry[1]-500, lastEntry[1]+500) 
    f.write(time.strftime("%d %b %Y %H:%M:%S",
             time.gmtime(current_time))+" CPU: "+str(cpu/100)+" Memory: "+str(mem/100)+"\n")
    if cpu > 6000 or mem > 6000: #reset on increasing trend
        return[3000,2500]
    if cpu < 2000 or mem < 2000:
        return[3000,2500]
    return [cpu,mem]

current_time = time.time()
lastEntry = [3000,2500]
for i in range (1000): 
    lastEntry = generate_const_data(lastEntry,current_time)
    current_time += 300
