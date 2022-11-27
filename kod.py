def calc_stat(listened):
    summ = 0
    for i in listened:
        summ += i
    mins = summ//60
    return (f'Вы прослушали {len(listened)}'
    f' песен общей продолжительностью {mins} минут.')
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))