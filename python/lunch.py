# import시 주의할 점:
#import 는 가지고 오는 행위로 항상 최 상단에 작성하는게 좋다.
import random
#list: 대괄호로 묶음
menu = ['짜장면', '짬뽕', '탕수육']

print(menu)

choice = random.choice(menu)

print(choice)
