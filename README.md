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
Relevant logs for user authentication failure have been highlighted with '🔴'

```
250.143.115.77 - - [20/Nov/2022:07:26:05 +0000] "GET /orchestrate/out-of-the-box/strategize/infrastructures HTTP/1.0" 503 28770
142.168.186.242 - christiansen4636 [20/Nov/2022:07:26:05 +0000] "HEAD /iterate HTTP/1.1" 504 19491
16.7.216.130 - - [20/Nov/2022:07:26:05 +0000] "HEAD /b2c/visionary/models HTTP/1.1" 401 11953
🔴 204.60.182.6 - - [20/Nov/2022 10:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 1555
119.14.50.254 - ullrich3175 [20/Nov/2022:07:26:05 +0000] "POST /value-added/bricks-and-clicks HTTP/1.0" 205 26916
62.180.185.38 - yost3844 [20/Nov/2022:07:26:05 +0000] "DELETE /world-class/markets HTTP/1.1" 401 8789
🔴 204.60.182.6 - - [20/Nov/2022 15:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 3668
🔴 204.60.182.6 - - [20/Nov/2022 20:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 12225
225.56.63.130 - - [20/Nov/2022:07:26:05 +0000] "POST /compelling/plug-and-play/syndicate HTTP/1.0" 503 5562
221.71.17.182 - - [20/Nov/2022:07:26:05 +0000] "PATCH /synthesize HTTP/2.0" 501 577
65.240.186.118 - balistreri1382 [20/Nov/2022:07:26:05 +0000] "PATCH /infrastructures/engage/e-markets/incentivize HTTP/2.0" 401 15791
🔴 204.60.182.6 - - [21/Nov/2022 02:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 17066
111.74.120.125 - - [20/Nov/2022:07:26:05 +0000] "POST /roi/supply-chains/brand HTTP/2.0" 405 83
🔴 204.60.182.6 - - [21/Nov/2022 07:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 20473
🔴 204.60.182.6 - - [21/Nov/2022 12:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 21504
210.111.98.68 - crona4151 [20/Nov/2022:07:26:05 +0000] "PATCH /rich/value-added/back-end HTTP/1.0" 504 11802
83.129.154.129 - - [20/Nov/2022:07:26:05 +0000] "GET /evolve/models HTTP/2.0" 200 24507
🔴 204.60.182.6 - - [21/Nov/2022 18:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 5514
🔴 204.60.182.6 - - [21/Nov/2022 23:20:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 9871
199.5.29.36 - jast8280 [20/Nov/2022:07:26:05 +0000] "POST /vertical HTTP/1.0" 201 15796
211.127.72.81 - nikolaus6238 [20/Nov/2022:07:26:05 +0000] "GET /exploit HTTP/1.1" 200 4558
🔴 204.60.182.6 - - [22/Nov/2022 04:40:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 4326
45.79.2.32 - feil2513 [20/Nov/2022:07:26:05 +0000] "PUT /metrics/redefine HTTP/1.0" 401 9965
🔴 204.60.182.6 - - [22/Nov/2022 10:00:50 +0000] "PUT /en-us/account/login-gate/HTTP/1.0" 200 16102
```

Logs are generated in [Apache NCSA](https://learn.microsoft.com/en-us/windows/win32/http/ncsa-logging) log format.