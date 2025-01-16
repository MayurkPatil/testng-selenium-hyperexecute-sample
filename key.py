import http.client
import sys

conn = http.client.HTTPSConnection("api-hyperexecute.lambdatest.com")
payload = ''
headers = {
  'Authorization': 'Basic ' + sys.argv[1]
}
conn.request("GET", "/sentinel/v1.0/jobs?&limit=1&is_cursor_base_pagination=true", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
