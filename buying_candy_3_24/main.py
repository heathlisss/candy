# ---------------------------------------------------------------------------------------------------------------------
# В магазине продаются различные конфеты. Конфеты описываются названием и ценой за килограмм. У вас есть N денег.
# Вы хотите купить максимальное количество различных конфет на указанную сумму (по килограмму каждого вида).
# Однако если можно купить различные конфеты, вы предпочитаете более дорогие, полагая, что они более хорошие.
# Какие конфеты вы выберите, сколько денег у вас останется?
#
# 	 Примечание: предположим, вы выяснили, что максимально можете купить K кг конфет,
# 	 тогда первый кг вы выберете самых дорогих конфет при условии,
# 	 что вам хватит денег на K-1 кг каких-то других конфет (также вы действуете для 2-го вида конфет и т.д.).
# ---------------------------------------------------------------------------------------------------------------------
from candy import Candy


# Чтение данных из файла
def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        N = int(file.readline())
        candies = []
        for line in file:
            candy_data = line.strip().split()
            name = candy_data[0]
            price = int(candy_data[1])
            candies.append(Candy(name, price))
        return N, candies


def write_to_file(purchase, remainder):
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write('остаток ' + str(remainder))
        file.write('\n')
        file.write('покупка:')
        for candy in purchase:
            file.write('\n')
            file.write(str(candy))


N, candies = read_from_file('test.txt')
# Сортировка объектов по возрастанию цены
candies = sorted(candies, key=lambda x: x.price, reverse=False)

# Нахождение максимального возможного колличества конфет на данную сумму
purchase = []
summ = 0
for candy in candies:
    if summ + candy.price <= N:
        purchase.append(candy)
        summ += candy.price
    else:
        break

# Выбор на известную сумму и колличество самых дорогих конфет
j = len(purchase) - 1
for candy in reversed(candies):
    if (summ - purchase[j].price + candy.price) <= N and candy.price > purchase[j].price:
        summ = summ - purchase[j].price + candy.price
        purchase[j] = candy
        j -= 1
    elif candy.price <= purchase[j].price:
        break

write_to_file(purchase, N - summ)