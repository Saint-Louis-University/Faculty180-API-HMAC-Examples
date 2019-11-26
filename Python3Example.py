# -*- coding: utf-8 -*-
"""
Working port of https://faculty180.interfolio.com/swagger/swagger_hmac/files/PythonExample.py from v2 to v3
"""

import base64
import datetime
import hashlib
import hmac
import urllib

# configuration
public_key = "Y5aNy8OZRYFKlTxNzXuSxzz64M8YLQB3vrcUP1zk7wQ="
private_key = "uEvu95GRt8fYw8dZkOyQGsOLy5yuB9vcUEK5cAcNuB4X6D6pTJegoIp/yRa7GaP/Lf6CQIA/xI/oP//YkayuAByx0nieazUEqp3DR7FtNf43="
database_id = "TestUniv"

# HTTP request details
request_verb = "GET"
host = "https://faculty180.interfolio.com/api.php"
request_string = "/units"
timestamp_string = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# format for HMAC
verb_request_string = request_verb + "\n\n\n" + timestamp_string + "\n" + request_string
encrypted_string = hmac.new(bytes(private_key, "UTF-8"), 
                            bytes(verb_request_string, "UTF-8"), 
                            hashlib.sha1).digest()
signed_hash = str(base64.b64encode(encrypted_string), "UTF-8")
authorization_header = "INTF " + public_key + ":" + signed_hash

# issue request
headers = { 'TimeStamp' : timestamp_string, 
            'Authorization' : authorization_header, 
            'INTF-DatabaseID' : database_id }
req = urllib.request.Request(host + request_string, headers = headers)
with urllib.request.urlopen(req) as response: 
    response = response.read()

print("TimeStamp:       " + timestamp_string)
print("Authorization:   " + authorization_header)
print("INTF-DatabaseID: " + database_id)
print("Response:        " + str(response, "UTF-8"))
