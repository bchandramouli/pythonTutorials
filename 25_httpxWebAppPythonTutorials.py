#!/usr/bin/env python3

# https://docs.python.org/3/library/logging.config.html

"""
Calling into python web apps

via httpx client

"""

from flask import Flask
import httpx

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome World!"


"""
# XXXX - this part does not work
# recheck please
#
with httpx.Client(base_url="http://testserver") as client:
    r = client.get("/")
    print(r.text)
    assert(r.status_code == 200)
    assert(r.text == "Welcome World!")

"""
