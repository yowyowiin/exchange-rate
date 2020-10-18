from os import getenv

WARNINGS = 'ignore'
DECODE = 'utf-8'

# App settings
APP_PREFIX = getenv('APP_PREFIX', 'exchange-rate')
APP_VERSION = 'v0.0.0'
APP_PORT = int(getenv('PORT', 8085))


# Fixer settings
FIXER_API_KEY = getenv('FIXER_API_KEY')

# Banxico settings
BANXICO_TOKEN = getenv('BANXICO_TOKEN')

# Authentication settings
DUMMY_USER_ID = 123
EXPIRATION_TIME = int(getenv('EXPIRATION_TIME', 600))

# Exchange controller settings
USER_RATE_LIMIT = int(getenv('USER_RATE_LIMIT', 5))

# Cache Memory settings
LIFETIME = int(getenv('LIFETIME', 60))  # 60 secs as default
REDIS_URL = getenv('REDIS_URL', 'redis://localhost:6379')
