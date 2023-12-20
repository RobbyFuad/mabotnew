import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://pia.telkomsigma.co.id',
    'Referer': 'https://pia.telkomsigma.co.id/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'email': 'robby.fuady@sigma.co.id',
    'password': 'GREEDworse14*',
}

response = requests.post('https://apigw.telkomsigma.co.id/pia/apiPrd/auth/', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"email":"robby.fuady@sigma.co.id","password":"GREEDworse14"}'
#response = requests.post('https://apigw.telkomsigma.co.id/pia/apiPrd/auth/', headers=headers, data=data)
print(response.text)