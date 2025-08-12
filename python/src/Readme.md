#### Services 
---
- `Auth` service: Validates request and sends back a JWT for access to the rabbitmq service
    Endpoints: 
        `validate`:
            - performs validation of credentials and returns a json webtoken if valid 
        `login`: 
            - 
- `Gateway` service: 
	- Endpoints: 
		- `login`:  
			- Sends incoming requests to the `Auth` service Performs validation of credentials given by the user 
		- `upload`: adds video files to the rabbimq queue to be consumed by the converter service 
		- `download`: 
- `RabbitMQ` service: 
    - Endpoints: 
    
- `Consumer` service: 
    - Endpoints: 
        - 