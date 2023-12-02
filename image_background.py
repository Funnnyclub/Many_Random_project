# Requires "requests" to be installed (see python-requests.org)
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('19040552.jpeg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Ysre6p9qLrXAed4gsgbBV7Eu'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)