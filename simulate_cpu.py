import random
import time

def generate_spike_data(lastEntry,current_time):
    f = open("cpulogs.txt", "a")
    peak_chance = random.randint(0, 100)
    is_peak = False

    if peak_chance < 2:  # 2% chance for generating a spike
        cpu = random.randint(lastEntry[0]+4000,lastEntry[0]+5000)
        mem = random.randint(lastEntry[1]+4000, lastEntry[1]+5000) 
        is_peak = True
    else:
        cpu = random.randint(lastEntry[0]-200,lastEntry[0]+200) 
        mem = random.randint(lastEntry[1]-200, lastEntry[1]+200) 
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
    cpu = random.randint(lastEntry[0]-200,lastEntry[0]+200) 
    mem = random.randint(lastEntry[1]-200, lastEntry[1]+200) 
    f.write(time.strftime("%d %b %Y %H:%M:%S",
             time.gmtime(current_time))+" CPU: "+str(cpu/100)+" Memory: "+str(mem/100)+"\n")
    if cpu > 5000 or mem > 5000: #reset on increasing trend
        return[3000,2500]
    if cpu < 2000 or mem < 2000:
        return[3000,2500]
    return [cpu,mem]

def generate_grad_data(lastEntry,current_time):
    f = open("cpulogs.txt", "a")
    dip_chance = random.randint(0, 100)
    is_dip = False

    if dip_chance < 20:  # 20% chance for generating a dip
        cpu = random.randint(lastEntry[0]-100,lastEntry[0])
        mem = random.randint(lastEntry[1]-100, lastEntry[1]) 
        is_dip = True
    else:
        cpu = random.randint(lastEntry[0],lastEntry[0]+100) 
        mem = random.randint(lastEntry[1], lastEntry[1]+100) 
    if cpu >= 10000 or cpu <= 0:
        cpu = lastEntry[0]
    if mem >= 10000 or mem <= 0:
        mem = lastEntry[1]
    f.write(time.strftime("%d %b %Y %H:%M:%S",
             time.gmtime(current_time))+" CPU: "+str(cpu/100)+" Memory: "+str(mem/100)+"\n")
    return [cpu,mem]

def generate_graph(graph_type):
    current_time = time.time()
    lastEntry = [3000,2500]
    while True:
        if graph_type.value == 0: 
            lastEntry = generate_const_data(lastEntry,current_time)
        elif graph_type.value == 1:
            lastEntry = generate_spike_data(lastEntry,current_time)
        elif graph_type.value == 2:
            lastEntry = generate_grad_data(lastEntry, current_time)
        current_time += 1
        time.sleep(0.1)