import requests

def http_request(max_retries):
    url = "https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1"
    retries = 0
    
    while retries < max_retries:
        try:
            response = requests.get(url, headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            })
            if response.status_code == 200:
                try:
                    json_response = response.json()
                    if "success" in json_response:
                        return json_response
                except ValueError:
                    print("Response is not valid JSON.")
            else:
                print(f"{response.status_code} Error")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        
        retries += 1
        print(f"Retrying ({retries}/{max_retries})...")
    
    raise Exception("Invalid Response!")

try:
    result = http_request(10)
    print("Request succeeded:", result)
except Exception as e:
    print("Error:", e)
