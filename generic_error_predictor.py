import pandas as pd
import numpy as np
import pickle
import re
from dateutil import parser
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

def function2_Error():
    
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

    
    for i in range(0,len(df1)):
        df1["timestamp"][i]=parser.parse(df1["timestamp"][i].replace(':', ' ',1))
        df1["timestamp"][i]=str(df1["timestamp"][i])[:-6]
        
    df1['status_code'] = pd.to_numeric(df1['status_code'])
    df1['timestamp'] = pd.to_datetime(df1['timestamp'])
    df1['response_size'] = pd.to_numeric(df1['response_size'])
    
    df_new=df1[["timestamp","response_size","status_code","verb"]]

    
    for i in range(0,len(df_new)):
        df_new['timestamp'][i]=int(df_new['timestamp'][i].strftime("%Y%m%d%H%M%S"))

    
    df_new["status"]=""
    for i in range(0,len(df_new)):
        if (df_new["status_code"][i] >=100 and df_new["status_code"][i]<200):
            df_new["status"][i]="informational"
        elif (df_new["status_code"][i] >=200 and df_new["status_code"][i]<300):
            df_new["status"][i]="successful"
        elif (df_new["status_code"][i] >=300 and df_new["status_code"][i]<400):
            df_new["status"][i]="redirection"
        elif (df_new["status_code"][i] >=400 and df_new["status_code"][i]<500):
            df_new["status"][i]="client"
        elif (df_new["status_code"][i] >=500 and df_new["status_code"][i]<600):
            df_new["status"][i]="server"

    
    df_new.drop(["status_code"],axis=1,inplace=True)
    col = ["verb","status"]
    enc = LabelEncoder()
    for col_name in col:
        df_new[col_name]=enc.fit_transform(df_new[col_name])
    df_lagged = df_new.copy()
    trailing_window_size = 10

    for window in range(1, trailing_window_size + 1):
        shifted = df_new.shift(window)
        shifted.columns = [x + "_lag" + str(window) for x in df_new.columns]
        df_lagged = pd.concat((df_lagged, shifted), axis=1)
    df_lagged = df_lagged.dropna()

    x = df_lagged.iloc[:,4:]
    y = df_lagged.iloc[:,3]

    y = enc.inverse_transform(y)
    y[y=="informational"]="successful"
    y[y=="redirection"]="successful"
    y[y=="client"]="error"
    y[y=="server"]="error"

#     print(df_lagged.shape)

    y=enc.fit_transform(y)
    y = pd.DataFrame(y,columns=["status"])
    model = pickle.load(open('file.pkl','rb'))
    prediction = model.predict(x)
#     print(prediction)
#     print(prediction.shape)
    res=[]
    ips=[]
    timestamp=df_lagged.iloc[:,0]
#     print(timestamp)
    response_size=df_lagged.iloc[:,1]
#     print(response_size)
    for i in range(0,len(y)):
        if(prediction[i]==0):
            res.append("error")
        else:
            res.append("susuccessful")
        ips.append(df1["IP"][i])
    print(len(ips))
    summary1 = pd.DataFrame({'IP': ips, 'timestamp':timestamp,'response size':response_size, 'result': list(res)}, columns=['IP','timestamp','response size', 'result'])
    values, counts = np.unique(prediction, return_counts=True)
    error=counts[0]
    successful=counts[1]
    summary2=[["error","successful"],[error,successful]]
    summary2=pd.DataFrame(summary2)
    return summary1
    #print(summary2)
    #send_mail(summary1)