# 202102908

from bs4 import BeautifulSoup

from requests import get

data_get = get('https://omgtu.ru/s1c2/Ranzhirovannyye_Spiski_bachelor.html').text


data_refresh = BeautifulSoup(data_get, 'html.parser').find_all('table')

n_o_w = input("Input name of way: ")    # Вводим № или название направления (не то и другое одновременно)

data_end = []   # Все отрасли направлений

for i in data_refresh:
    x = list()
    n = i.find_all('tr')[4].text.encode('ISO-8859-1').decode('utf-8').split('\n')[1].split(", ")
    if n_o_w == n[0] or n_o_w == n[1]:
        x.append(n)
        for i2 in i.find_all(class_='R7'):
            z = i2.text.encode('ISO-8859-1').decode('utf-8').split('\n')
            x.append([z[2], z[10]])
        data_end.append(x)

enemy = list()      # предположительные (не подавшие согласие) противники
true_enemy = list()     # реальные (подавшие согласие) противники

ur_id = input("Input your id: ")    # Вводим ваш ID

for i in data_end:
    z = 0   # Переменная отслеживающая попадение вашего ID
    for i3 in range(1, len(i)):
        if i[i3][0] != ur_id:
            enemy.append(i[i3])
            if i[i3][1] == '✓':
                true_enemy.append(i[i3])
        else:   # попадение вашего ID прерывает цикл
            z = 1
            break
    if z == 0:
        enemy = list()
        true_enemy = list()
    else:
        break


print(len(enemy), enemy)
print(len(true_enemy), true_enemy)
