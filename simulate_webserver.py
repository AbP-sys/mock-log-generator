import random
import time

def repeated_login(num_logins,time_frame,same_user,ip):
    ip = ip
    current_time = time.time()
    for i in range(num_logins):
        with open("log.txt",'a',encoding = 'utf-8') as f:
            f.write(ip+" - balistreri1382 ["+time.strftime("%d/%b/%Y:%H:%M:%S",
             time.gmtime(current_time))+" +0000] \"PUT /account/loginPortal/ HTTP/1.0\" 401 "+
             str(random.randrange(100, 25000, 1))+"\n")
            current_time += time_frame
            time.sleep(0.5)

def random_logs():
    file = open('randlogs.txt')
    content = file.readlines()
    ptr = content[random.randrange(1000)]
    while(True):
        with open("log.txt",'a',encoding = 'utf-8') as f:
            f.write(ptr)
            ptr = content[random.randrange(1000)]
            time.sleep(0.2)    
