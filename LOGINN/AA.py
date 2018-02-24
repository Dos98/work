import requests
RegisterNumber = input("Enter the registration number : ")
password = input("Enter the password : ")

url = "http://phc.prontonetworks.com/cgi-bin/authlogin"

payload = {'Submit22':'Login','password': password,'serviceName':'ProntoAuthentication','userId':RegisterNumber}
headers = {
    'origin': "http://phc.prontonetworks.com",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'save-data': "on",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'dnt': "1",
    'referer': "http://phc.prontonetworks.com/cgi-bin/authlogin",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    }

response = requests.post(url, data=payload, headers=headers)

print(response.text)india
