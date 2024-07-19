driving = input('你有沒有開過車:')
car = input('請問你幾歲:')
car = int(car)
if driving == '有':
    if car >= 20:
        input('你合法喔') 
    else:
        input('你犯法了喔')
elif driving == '沒有':
    if car >= 20:
        print('去考駕照辣')
    else:
        print('那你在, 18 - car, 就可以考駕照囉')
else:
    print('只能輸入有或沒有')

