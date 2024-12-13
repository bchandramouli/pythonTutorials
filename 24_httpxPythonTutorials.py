#!/usr/bin/env python3

# https://docs.python.org/3/library/logging.config.html

import httpx

# similar to requests but a bit more powerful

r = httpx.get("https://api.github.com/user", auth=("user", "pass"))
print(r.status_code)

print(r.content)

print(r.headers["content-type"])

print(r.encoding)

print(r.json())

r = httpx.get("https://httpbin.org/get")

r = httpx.post("https://httpbin.org/post", data={"key": "value"})
r = httpx.put("https://httpbin.org/put", data={"key": "value"})
r = httpx.delete("https://httpbin.org/delete")
r = httpx.head("https://httpbin.org/get")
r = httpx.options("https://httpbin.org/get")

params = {"key1": "value1", "key2": "value2"}
r = httpx.get("https://httpbin.org/get", params=params)

# custom headers
headers = {"user-agent": "my-app/0.0.1"}
r = httpx.get("https://httpbin.org/headers", headers=headers)

# send JSON encoded data
data = {"integer": 123, "boolean": True, "list": ["a", "b", "c", "d"]}
r = httpx.post("https://httpbin.org/post", json=data)

# cookies
r = httpx.get("https://httpbin.org/cookies/set?chocolate=chip")
print(r.cookies["chocolate"])

# authentication
httpx.get("https://example.com", auth=("my_user", "password123"))

# set timeout default = 5
httpx.get("https://github.com/", timeout=1)


# advanced usage - httpx_client
# client uses http connection pooling
with httpx.Client() as client:
    r = client.get("https://example.com/")
    # r = httpx.get('https://example.com/')

print(r.status_code)


# async calls
import asyncio


async def clientGet():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.example.com/")
        print(response)


asyncio.run(clientGet())
