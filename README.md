# Mock log generator
An application to generate logs of specific use cases for log analysis using machine learning. 

## Purpose 
This application is to simulate specific use cases of real-life traffic which can be fed into an ML model for training and testing purposes to detect anomalies in server, configuration, or user traffic and suggest appropriate counter measures.

The main focus of this application is to instantaneously generate logs which might occur over a long period of time in real-life. 

For example: 

- Authentication error for same user for 10 times in 2 days.
- Increasing trend in CPU usage.
 
## Preview

log.txt:
```
204.60.182.6 - - [20/Nov/2022 10:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 1555
204.60.182.6 - - [20/Nov/2022 15:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 3668
204.60.182.6 - - [20/Nov/2022 20:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 12225
204.60.182.6 - - [21/Nov/2022 02:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 17066
204.60.182.6 - - [21/Nov/2022 07:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 20473
204.60.182.6 - - [21/Nov/2022 12:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 21504
204.60.182.6 - - [21/Nov/2022 18:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 5514
204.60.182.6 - - [21/Nov/2022 23:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 9871
204.60.182.6 - - [22/Nov/2022 04:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 4326
204.60.182.6 - - [22/Nov/2022 10:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 16102
```

Logs are generated in [Apache NCSA](https://learn.microsoft.com/en-us/windows/win32/http/ncsa-logging) log format.