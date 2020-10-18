# Exchange rate

This web service exposes the current exchange rate of USD to MXN.

## Prerequisites

1. Docker
2. Python 3.7
3. Banxico Token
4. Fixer API Key

## Technologies

* Python
* Redis

## Installing

### Creating a Banxico Token
You should get your token via this url: 
https://www.banxico.org.mx/SieAPIRest/service/v1/token

### Creating a Fixer API Key
You should follow the steps from this url: 
https://fixer.io/quickstart

### Environment variables
#### Fixer Credentials
- FIXER_API_KEY
#### Banxico Token
- BANXICO_TOKEN
#### Authentication settings
- EXPIRATION_TIME
#### Exchange controller settings
- USER_RATE_LIMIT
#### Cache Memory settings
- LIFETIME
- REDIS_URL
#### App settings
- APP_PORT

### Docker Compose for development and starting redis

```bash
docker-compose -f docker-compose-local.yml up
```

## Running the application

1. Set the previously described environment variables.
2. Execute `docker-compose up`to start Redis.
3. Execute `python3 app.py`.

## API Endpoints
In [this link](endpoints.md) you can read the documentation of endpoints


## Running the tests

Execute in the root folder of the project: `python3 -m unittest`

## Contributors
- Yosef Rodríguez
