#!/usr/bin/env python3

import os
import json

# print out all env variables as plain text
# print("Content-Type: text/plain") # let the browser know to expect plain text
# print()
# print(os.environ)

# print env variables as json
# print("Content-Type: application/json") # let the browser know to expect json
# print()
# print(json.dumps(dict(os.environ), indent=2)) # print with nice formatting

# print query parameter data in HTML
print("Content-Type: text/html")
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")