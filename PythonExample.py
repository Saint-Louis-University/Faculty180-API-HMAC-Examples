import datetime
import hmac
from hashlib import sha1
import urllib2

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
encrypted_string = hmac.new(private_key, verb_request_string, sha1).digest()
signed_hash = encrypted_string.encode("base64").rstrip('\n')
authorization_header = "INTF " + public_key + ":" + signed_hash

# issue request
request = urllib2.Request(host + request_string)
request.add_header("TimeStamp", timestamp_string)
request.add_header("Authorization", authorization_header)
request.add_header("INTF-DatabaseID", database_id)
response = urllib2.urlopen(request)
print "TimeStamp: " + timestamp_string
print "Authorization: " + authorization_header
print "INTF-DatabaseID: " + database_id
if request_verb == "GET":
	print response.read()