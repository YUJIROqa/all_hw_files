import requests
from datetime import datetime

start = datetime.now()
response = requests.get('https://www.qa-practice.com/')
print(response)
end = datetime.now()
print(end - start)



