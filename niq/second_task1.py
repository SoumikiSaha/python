import requests
import time
import logging

url = 'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Accept':'application/json',
    'Content-Type':'application/json'
}


def http_request():
    max_retries = 5
    retry_delay = 2

    for attempt in range(max_retries):
        response = requests.get(url)
       
        if response.status_code == 200:
            try:
                json_response = response.json()
                if 'success' in json_response:
                    return json_response
                else:
                    logging.WARNING('Success message not found in the response, retrying...')
            except ValueError:
                logging.WARNING('Response is not in JSON format, retrying...')
        else:
            logging.error(f'Request failed with status code {response.status_code}, retrying...')
       
        time.sleep(retry_delay)
   
    return {'error': 'Failed to get a successful response after multiple attempts'}


result = http_request()
if 'error' in result:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        if 'success' in json_response:
            print(json_response)
else:
    print(result)