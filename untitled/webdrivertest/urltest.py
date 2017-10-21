import urllib

request = urllib.Request("https://www.baidu.com")
request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
response = urllib.urlopen(request)
print(response.getcode())
print (response.geturl())
print(response.read())