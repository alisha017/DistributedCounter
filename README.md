# Distributed Counter
Implemented distributed counter using Python, Kafka and Docker

## Ideal directory structure
DistributedCounter/  
│  
├── docker-compose.yml  
├── Dockerfile  
├── requirements.txt  
│  
├── app/  
│   ├── \_\_init\_\_.py  
│   ├── counter.py  
│   └── app.py  
│  
├── tests/  
│   └── test_counter.py  
│  
└── config/  
    └── settings.py  


## Run Commands
Docker build and run:  
`docker-compose up --build`  
To increment the counter:  
`curl -X POST -H "Content-Type: application/json" -d '{"value": 5}' http://localhost:5000/increment`  
To get the value of the counter:  
`curl http://localhost:5001/value`

To observe logs:  
`docker-compose logs flask-app1`  
`docker-compose logs flask-app2`     
`docker-compose logs kafka` 

