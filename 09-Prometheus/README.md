http_requests_total

http_requests_total{job=~".*etheus"}

http_requests_total{job=~".*etheus", method="get",code="200"}

http_requests_total{job=~".*etheus",handler="graph",method="get",code="200"}[5m]


Functions
==========>
rate(http_requests_total[5m])

sum(rate(http_requests_total[5m])) by (job)


Memory Consumption
===================>

( node_memory_MemTotal_bytes - node_memory_MemFree_bytes )

In MB 

(node_memory_MemTotal_bytes - node_memory_MemFree_bytes)/ 1024 / 1024

sum(rate(node_cpu_seconds_total[15m] )) by (job)



sum(rate(flask_request_latency_seconds_bucket{le="1.0"}[5m])) by (job) / sum(rate(flask_request_latency_seconds_count[5m])) by (job)

AppDex
=======>
( sum(rate(flask_request_latency_seconds_bucket{le="0.25"}[5m])) by (job) + sum(rate(flask_request_latency_seconds_bucket{le="1.0"}[5m])) by (job)  )/  2 / sum(rate(flask_request_latency_seconds_count[5m])) by (job)
