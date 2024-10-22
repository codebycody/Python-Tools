import requests

def repeater():
    print("HTTP Request Repeater - Simulating Burp Suite Repeater")

    # Get user input for HTTP method, URL, headers, and data
    method = input("Enter HTTP method (GET, POST, PUT, DELETE, etc.): ").upper()
    url = input("Enter the URL: ")
    
    # Option to add headers
    headers_input = input("Enter headers (key:value) format, separated by commas, or leave blank: ")
    headers = {}
    if headers_input:
        headers = dict(h.split(':') for h in headers_input.split(','))

    # Option to add data for POST, PUT requests
    data = None
    if method in ['POST', 'PUT', 'PATCH']:
        data = input("Enter the data (for JSON, wrap with {}): ")

    try:
        # Send the HTTP request based on method and input
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            print(f"Unsupported HTTP method: {method}")
            return

        # Print response details
        print(f"\n=== Response ===")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Content: {response.text}\n")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    repeater()
