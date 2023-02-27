#auc
import random
import time

ff_list = 'У вас купили слот за указанную цену!', 'У вас никто ничего не купил'
auc_object = input('Что выставим на аукцион?:  ')
auc_price = int(input('Введите цену: '))

print(f'Вы выставили {auc_object} на акуцион за {auc_price} рублей! Ждем пока кто то купит ваш слот')
time.sleep(3)

print (random.choice(ff_list))