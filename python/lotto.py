# 1~45 중에 6개만 뽑아서 리스트에 담아서 출력
# 비 복원 추출: 겹치는것 없이 추출
import random
#1~45의 숫자 범위 만들고 리스트로 만들기
winners = [4, 7, 14, 16, 24, 44]
numbers = list(range(1,46))
 
#비복원 추출로 6개 뽑기
for i in range(1000000):
    lotto = random.sample(numbers, 6)
    count = 0
    for num in lotto:
        #print(num)
        if num in winners:
            count = count + 1
    if count == 6:
        print('1등 당첨!!!!')