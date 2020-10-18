
Currently, there are the following endpoints:

# Token

### Get a temporary token:
- GET - /api/exchange-rate/token
```
curl --location --request GET 'http://localhost:8085/api/exchange-rate/token'
```

# Exchange rate

### Get exchange rate USD to MXN
- GET - /api/exchange-rate
```
curl --location --request GET 'http://localhost:8085/api/exchange-rate' \
--header 'token: 'generated_token' \
--header 'user: 'any_user'
````