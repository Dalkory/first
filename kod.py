def calc_stat(listened):
    return len(listened)
    summ = 0
    for i in listened:
        summ += i
    mins = summ//60
    return mins
print(
    f'Вы прослушали {calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198])}'
    f'песен общей продолжительностью {mins}.')