import requests

url = 'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept':'application/json',
    'Content-Type':'application/json'
}


def http_request():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        if 'success' in json_response:
            return json_response
        
print(http_request())

"""
Required Curl command:

curl -X GET "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1" \
     -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" \
     -H "Accept: application/json" \
     -H "Content-Type: application/json"

"""
