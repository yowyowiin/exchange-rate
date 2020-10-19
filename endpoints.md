
Currently, there are the following endpoints:

# Token

### Get a temporary token:
- GET - /api/exchange-rate/token
```
curl --location --request GET 'http://localhost:8085/api/exchange-rate/token'
```
The token expiration time is 10 minutes and this can me changed with the `EXPIRATION_TIME` env variable

# Exchange rate

### Get exchange rate USD to MXN
- GET - /api/exchange-rate
```
curl --location --request GET 'http://localhost:8085/api/exchange-rate' \
--header 'token: 'generated_token' \
--header 'user: 'any_user'
````
This endpoint has a rate limit by user of 5 requests per minute by default,
the number of request and the rate time can be changed with the 
`USER_RATE_LIMIT` and `LIFETIME` env variables respectively