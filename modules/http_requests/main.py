# HTTP (HyperText Transfer Protocol) is a protocol used to send and receive
# data over the Internet. It operates in a client/server mode, where the client
# (your browser, for example) makes a request to the server
# (a website, for example), which responds with the appropriate data.
#
# The client's request message should include data such as:
# - The HTTP method
#     - read (safe) - GET, HEAD (headers), OPTIONS (supported methods)
#     - write - POST, PUT (replace), PATCH (update), DELETE
# - The address of the resource to be accessed (/users/)
# - The HTTP headers (Content-Type, Authorization)
# - The message body (if necessary, depending on the HTTP method)
#
# The server's response message should include data such as:
# - HTTP status code (200 success, 404 Not Found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - HTTP headers (Content-Type, Accept)
# - The message body (may be empty in some cases)

# requests for http requests
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:8000/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)

# IMPORTANT
# To watch -> https://youtu.be/Qd8JT0bnJGs
