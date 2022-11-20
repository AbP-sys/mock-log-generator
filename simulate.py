import random
import time

def repeated_login():
    ip = "204.60.182.6"
    current_time = time.time()
    with open("log.txt",'w',encoding = 'utf-8') as f:
        for i in range(10):
            f.write(ip+" - - ["+time.strftime("%d/%b/%Y %H:%M:%S",
             time.gmtime(current_time))+" +0000] \"PUT /en-us/account/login-gate/HTTP/1.0\" 200 "+
             str(random.randrange(100, 25000, 1))+"\n")
            current_time += 18000 #user input

repeated_login()