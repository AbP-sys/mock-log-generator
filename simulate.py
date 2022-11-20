import random
import time

def repeated_login(num_logins,time_frame,same_user):
    ip = "204.60.182.6"
    current_time = time.time()
    with open("log.txt",'w',encoding = 'utf-8') as f:
        for i in range(num_logins):
            f.write(ip+" - - ["+time.strftime("%d/%b/%Y %H:%M:%S",
             time.gmtime(current_time))+" +0000] \"PUT /en-us/account/login-gate/HTTP/1.0\" 200 "+
             str(random.randrange(100, 25000, 1))+"\n")
            current_time += time_frame

repeated_login(10,19200,True)