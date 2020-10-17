from os import getenv

WARNINGS = 'ignore'
DECODE = 'utf-8'

# App settings
APP_PREFIX = getenv('APP_PREFIX', 'exchange-rate')
APP_VERSION = 'v0.0.0'


# Fixer settings
FIXER_API_KEY = getenv('FIXER_API_KEY')