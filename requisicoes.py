import requests

response = requests.get('https://www.walissonsilva.com/')

print(f'Response code: {response.status_code}')
print('\n↓↓ Header ↓↓\n')
print(response.headers)
print('\n↓↓ Content ↓↓\n')
print(response.content)

