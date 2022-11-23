import requests


path = ''
host = 'http://10.10.169.100:3000'

while(host is not ''):
    path=''
    response = requests.get(host + path)
    print(response)
    #json_response = response.json()
    #print(json_response)
    #converted_response=json_response.encdode('ascii')
    #print(converted_response)
    text = response.text
    print(text)
    status_code = response.status_code
    print(status_code)