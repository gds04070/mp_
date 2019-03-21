import requests
import json


mp_key = 'vX3qj9n41k9hWBxFLJPU'

request_type = 'materials'
identifier = 'Fe2O3' #찾고 싶은 거
data_type = 'vasp'
mp_property = 'energy'



identifier = input("찾고 싶은 원소를 입력해주세요")

params = {'API_KEY' : mp_key} #GET타입 넘겨줄거

url = 'https://www.materialsproject.org/rest/v2/'+request_type+'/'+identifier+'/'+data_type #나중에 수정 필요


data = requests.get(url, params = params)
#data = requests.get(url)

print(data.status_code)

if data.status_code != 200:
	print("통신 에러"+data.status_code)


dict = json.loads(data.text)


print("find energy...")

for i in dict["response"]:
	print(i["energy"])
