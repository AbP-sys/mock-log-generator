import pandas as pd
import numpy
#import win32com.client as win32
from datetime import datetime as dt
import pandas as pd
from dateutil import parser
import re
import warnings
warnings.filterwarnings("ignore")
import random

def finaldata():
    f = open("log.txt",'r')
    LOG_LINE_REGEX = r'^(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<timestamp>.*)\]\s"(?P<verb>[A-Z]+)\s(?P<path>[\w\/]+)\s+(?P<protocol>[\w\/\.]+)"\s(?P<status_code>\d+)\s(?P<response_size>\d+).*'
    pattern = re.compile(LOG_LINE_REGEX)
    count=0
    l=[]
    for line in f:
        m = pattern.match(line)
        if m:
            l.append(m.groupdict())
    df1 = pd.DataFrame(l)
#     print(df1)
#    df = df1.to_csv("logs.csv")
    df=df1
#     print(df)
    for i in range(0,len(df)):
        df["timestamp"][i]=parser.parse(df["timestamp"][i].replace(':', ' ',1))
        df["timestamp"][i]=str(df["timestamp"][i])[:-6]
    df['status_code'] = pd.to_numeric(df['status_code'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['response_size'] = pd.to_numeric(df['response_size'])
    df['Duration'] = 0
    df['Duration'] = df['Duration'].astype(float)
    
    """ for i in range(0,len(df)):
        df['Duration'][i] = round(random.uniform(0.0, 519611.231), 3) """
    return(df)
    
def function1_authentication():
    data=finaldata()
    data['status_code'] = pd.to_numeric(data['status_code'])
    data['timestamp'] = pd.to_datetime(data['timestamp'])
 
    myhash_time = {}
    myhash_count={}
    store=[]
    for i in range(0,len(data)):
        ip=data["IP"][i]
        t=data["timestamp"][i]
        if ip in myhash_time.keys():
            dif=(dt.strptime(str(t),"%Y-%m-%d %H:%M:%S")-dt.strptime(str(myhash_time.get(ip)),"%Y-%m-%d %H:%M:%S")).days
            if (dif) >2:
                myhash_time[ip]=t
            else:
                if data["status_code"][i]==401:
                    if ip in myhash_count.keys():
                        myhash_count[ip]=myhash_count[ip]+1
                        if myhash_count[ip]>=10:
                            store.append(ip)
                    else:
                        myhash_count[ip]=1
        else:
            myhash_time[ip]=t
            if data["status_code"][i]==401:
                    if ip in myhash_count.keys():
                        myhash_count[ip]=myhash_count[ip]+1
                        if myhash_count[ip]>=10:
                            store.append(ip)
                    else:
                        myhash_count[ip]=1
    ips=[]
    count=[]
    timestamp=[]
    for key in store:
        ips.append(key)
        count.append(myhash_count.get(key))
        timestamp.append(myhash_time.get(key))
    summary = pd.DataFrame({'IP': ips, 'timestamp': list(timestamp),'count': list(count)}, columns=['IP', 'timestamp','count'])
    return summary
    #send_mail(summary)