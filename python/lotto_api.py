# requests 불러오기
import requests
import random
# requests 사용해서 로또 api 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
# http: 하이퍼 텍스트~~ , 뒤에는 주소값,
#  ?뒤에 작성되는 값은 요청시 같이 보내는 값
# (? 키 = 값 & 키 =값) 이런 식
response = requests.get(url).json()
#요청 보내서 응답 받은 문서를 출력
#print(response)
# response = requests.get(url) 결과로 나타나는 Response [200]: 요청 성공적으로 수행
# 대괄호 안 숫자가 4로 시작하면 요청자가 잘못 요청한 것
# 5로 시작하면 서버측에 문제가 발생했을 때

# 당첨번호를 담을 list
winners = []

# 받아온 딕셔너리에서 필요한 값만 사용
for num in range(1, 7):
    # f스트링: 문자열 안에 변수를 넣는 방법
    #print(response [f'drwtNo{num}'])
    
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)
numbers = list(range(1,46))

#비복원 추출로 6개 뽑기
for i in range(10):
    lotto = random.sample(numbers, 6)
    count = 0
    for num in lotto:
        #print(num)
        if num in winners:
            count = count + 1
    if count == 6:
        print('1등 당첨!!!!')