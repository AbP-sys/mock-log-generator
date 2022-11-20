def repeated_login():
    ip = "204.60.182.6"
    date = "20/Nov/2020"
    time = 1800
    with open("log.txt",'w',encoding = 'utf-8') as f:
        for i in range(10):
            f.write(ip+" - - ["+date+":"+str(time)+" +0000] \"PUT /en-us/account/login-gate/HTTP/1.0\" 200 14594\n")
            time = (time+530) % 2400 #5 is input parameter

repeated_login()