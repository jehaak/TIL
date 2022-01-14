#requsts 불러오기, 나이예측 api 사용, 
#특정 이름을 입력 했을 때, 무작위 나이 가져와서 ~의 나이는 ~입니다
import requests
name = input()
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()

age = response['age']
print(f'{name}의 나이는 {age}살 입니다.')