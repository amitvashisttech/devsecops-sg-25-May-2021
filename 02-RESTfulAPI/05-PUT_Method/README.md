```
   74  curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Hey Rest"}' http://localhost:8081/todo/api/v1.0/tasks/1
   75  curl localhost:8081/todo/api/v1.0/tasks | jq
   76  curl -i -H "Content-Type: application/json" -X PUT -d '{"done":"true"}' http://localhost:8081/todo/api/v1.0/tasks/2
   77  curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:8081/todo/api/v1.0/tasks/2
   78  curl localhost:8081/todo/api/v1.0/tasks | jq

```
