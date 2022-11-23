#Simple API Requests
import requests

req = requests.get("http://www.google.com")
print("Web site response", req.status_code,"Which means", req.reason) 