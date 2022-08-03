#! /usr/bin/python3.10

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/ubuntu/ExampleFlask/ExampleFlask')
from app import app as application
application.secret_key = 'cookiescookies'
